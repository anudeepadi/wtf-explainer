#!/usr/bin/env python3
"""Find and download freely licensed photos from Wikimedia Commons.

search:   python3 commons.py search "data center racks" [n]
download: python3 commons.py get "File:Some name.jpg" out.jpg [width]

Prints license + author so the page can credit each image.
"""
import json, re, sys, urllib.error, urllib.parse, urllib.request

UA = "explainer-skill/1.0 (educational explainer pages)"
API = "https://commons.wikimedia.org/w/api.php"
OK = ("CC0", "Public domain", "CC BY", "CC BY-SA", "PD")


def fetch(url):
    # Commons rate-limits bursts (HTTP 429); back off and retry.
    import time
    for wait in (0, 5, 15, 40):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("Commons kept rate-limiting; try again in a minute")


def call(params):
    return json.loads(fetch(API + "?" + urllib.parse.urlencode(params)))


def info(pages, width):
    out = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        artist = re.sub("<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()
        out.append({
            "title": p["title"], "license": lic, "artist": artist[:80],
            "thumb": (ii.get("thumburl") or "").split("?")[0],
            "page": ii.get("descriptionurl", ""),
            "size": f'{ii.get("width")}x{ii.get("height")}',
            # Skip AI-generated images: the point of a photo is that it is real.
            "usable": lic.startswith(OK) and not re.search(r"DALL|Midjourney|AI[- ]generated|Stable Diffusion", p["title"], re.I),
        })
    return out


def search(q, n=6, width=960):
    d = call({"action": "query", "generator": "search", "gsrsearch": q + " filetype:bitmap",
              "gsrnamespace": 6, "gsrlimit": n, "prop": "imageinfo",
              "iiprop": "url|extmetadata|size", "iiurlwidth": width, "format": "json"})
    return info(d.get("query", {}).get("pages", {}), width)


def get(title, out, width=960):
    d = call({"action": "query", "titles": title, "prop": "imageinfo",
              "iiprop": "url|extmetadata|size", "iiurlwidth": width, "format": "json"})
    meta = info(d["query"]["pages"], width)[0]
    # Commons only serves standard thumbnail widths; use the URL the API returns.
    open(out, "wb").write(fetch(meta["thumb"]))
    meta["file"] = out
    return meta


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        for r in search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6):
            print(json.dumps(r, ensure_ascii=False))
    elif cmd == "get":
        w = int(sys.argv[4]) if len(sys.argv) > 4 else 960
        print(json.dumps(get(sys.argv[2], sys.argv[3], w), ensure_ascii=False))
