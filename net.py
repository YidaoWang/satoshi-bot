#!/usr/bin/env python
# coding: utf-8
import bs4
import urllib.request, urllib.error

url = "https://game8.jp/pokemon-sword-shield/272607"

htmldata = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(htmldata, "html.parser")

table_elms = soup.find_all("table", {"class": "a-table a-table a-table tablesorter"},)


for t in table_elms:
    tr_elms = t.find_all("tr")
    for tr in tr_elms:
        td_elms = tr.find_all("td")
        if len(td_elms) == 3:
            number = td_elms[0].renderContents()
            img_elm = td_elms[1].find("img")
            print(str({"name":img_elm["alt"].replace("の画像",""),"image":img_elm["src"]})+",")