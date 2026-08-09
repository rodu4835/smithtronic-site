"""Stamp the stylesheet <link> URLs in every page with a content hash.

Why this exists: GitHub Pages serves assets/site.css with Cache-Control:
max-age=600. If a deploy changes both the markup and the stylesheet, a browser
holding the previous CSS renders the new markup against it for up to ten
minutes. That happened once and it looked broken -- an unsized 1024px logo,
no centering, unstyled sections. Versioning the URL makes the pair atomic:
new markup requests a stylesheet URL the browser has never cached.

Run this after ANY edit to assets/*.css, before committing:

    python tools/cachebust.py

It rewrites href="...assets/site.css?v=<hash>" across all HTML and then
verifies no page was left with a stale or missing stamp.
"""
import glob
import hashlib
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

STYLESHEETS = ("site.css", "fonts.css")

ver = {}
for name in STYLESHEETS:
    digest = hashlib.sha256(open(os.path.join("assets", name), "rb").read()).hexdigest()
    ver[name] = digest[:8]
    print("  %-10s -> v=%s" % (name, ver[name]))

# href="<any number of ../>assets/<sheet>.css<optional existing ?v=...>"
LINK = re.compile(r'(href="(?:\.{1,2}/)*assets/(site|fonts)\.css)(\?v=[0-9a-f]+)?(")')


def stamp(m):
    return "%s?v=%s%s" % (m.group(1), ver[m.group(2) + ".css"], m.group(4))


changed = 0
for path in sorted(glob.glob("**/*.html", recursive=True)):
    text = io.open(path, encoding="utf-8").read()
    new = LINK.sub(stamp, text)
    if new != text:
        io.open(path, "w", encoding="utf-8", newline="").write(new)
        changed += 1

print("\nstamped %d html file(s)" % changed)

stale = []
for path in sorted(glob.glob("**/*.html", recursive=True)):
    text = io.open(path, encoding="utf-8").read()
    for name, digest in ver.items():
        if "assets/" + name in text and ("%s?v=%s" % (name, digest)) not in text:
            stale.append((path, name))

if stale:
    print("STALE OR UNSTAMPED:")
    for path, name in stale:
        print("  %s -> %s" % (path, name))
    raise SystemExit(1)
print("verified: every page links the current hash")
