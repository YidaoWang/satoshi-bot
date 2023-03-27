#!/usr/bin/env python
# coding: utf-8
import bs4
import urllib.request, urllib.error
import re

dic_url = {"wiki": "https://ja.wikipedia.org/wiki/", "niko": "http://dic.nicovideo.jp/a/",
           "uncy": "http://ja.ansaikuropedia.org/wiki/"},


def get_summary(keyword, dictionary="wiki"):
    url = dic_url[dictionary] + urllib.parse.quote(keyword)
    try:
        htmldata = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(htmldata, "html.parser")
        elem = soup.p.text
    except:
        return ""
    try:
        ntag = soup.p.nextSibling.nextSibling.name
        if ntag == "ul" or ntag == "ol" or ntag == "dl":
            elem += soup.p.nextSibling.nextSibling.text
        elem = re.sub("\[\d+\]", "", elem)
        elem = re.sub(u"\[注 \d+\]", u"", elem)
        return elem
    except:
        elem = re.sub("\[\d+\]", "", elem)
        elem = re.sub(u"\[注 \d+\]", u"", elem)
        return elem


def get_niko(keyword):
    url = dic_url["niko"] + urllib.parse.quote(keyword)
    try:
        htmldata = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(htmldata, "html.parser")
        meta = soup.find("meta",{"name":"description"},)
        elem = meta["content"]
    except:
        return ""
    elem = re.sub("\[\d+\]", "", elem)
    elem = re.sub(u"\[注 \d+\]", u"", elem)
    return elem


def get_summary1(keyword,dictionary="wiki"):
    url = dic_url[dictionary] + urllib.parse.quote(keyword)
    try:
        htmldata = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(htmldata, "html.parser")
        elem = soup.p.text
    except:
        return ""
    try:
        ntag = soup.p.nextSibling.nextSibling.name
        if ntag == "ul" or ntag == "ol" or ntag == "dl":
            n = soup.p.nextSibling.nextSibling.next.next
            elem = n.text
        elem = re.sub("\[\d+\]", "", elem)
        elem = re.sub(u"\[注 \d+\]", u"", elem)
        return elem
    except:
        elem = re.sub("\[\d+\]", "", elem)
        elem = re.sub(u"\[注 \d+\]", u"", elem)
        return elem

print(get_niko("けいおん"))