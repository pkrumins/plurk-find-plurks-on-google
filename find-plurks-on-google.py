#!/usr/bin/python
#
# A program by Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# I wrote it because I had plurked too much nonsense which I was not comfortable
# with. I used this program in combination with delete-plurks GreaseMonkey
# script that I also wrote (see link (2) below) to delete all the plurks that I
# didn't like.
#
# (1) http://www.catonmat.net/blog/python-library-for-google-search/
# (2) http://github.com/pkrumins/plurk-delete-plurks
#
# See http://github.com/pkrumins/find-plurks-on-google for full readme.txt
#

from xgoogle.search import GoogleSearch
from xgoogle.browser import Browser, BrowserError
from time import sleep
import re

queries = ["site:www.plurk.com/p/ pkrumins", "site:www.plurk.com pkrumins",
           "site:www.plurk.com peteris",     "site:www.plurk.com krumins",
           "site:www.plurk.com catonmat",    "site:plurk.com pkrumins"]

username = "pkrumins"

results = []
for query in queries:
    print "Getting Google results for '%s'." % query

    gs = GoogleSearch(query)
    gs.results_per_page = 100

    while True:
        temp_res = gs.get_results()
        if not temp_res: break
        results.extend(temp_res)
        print "Got %d, sleeping 5 seconds and getting more." % len(results)
        sleep(5)

print "Got %d results." % len(results)

ignore_ids = set()
seen_ids = set()

def get_id(url):
    # http://www.plurk.com/p/d8cyp/Good-Night-Plurkland
    m = re.search(url, "/p/([a-z0-9]+)")
    if m: return m.group(1)
    return None

browser = Browser()
for nr, result in enumerate(results):
    nr = nr + 1
    try:
        page = browser.get_page(result.url)
        if page.find('href="/user/%s" class="user"' % username) != -1:
            id = get_id(result.url)
            if id in ignore_ids:
                continue
            if id not in seen_ids:
                print "%s      (%d of %d)" % (result.url, nr, len(results))
                seen_ids.add(id)
    except BrowserError, error:
        if "404" not in error.error:
            print "%s (%s)" % (error.error, error.url)

