#!/usr/bin/env python
# coding: utf-8

from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials
import urllib

# Replace with your subscription key.
subscription_key = "7f7d2c72ab9b41eeb526e3a43b62d639"

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = "https://satoshisearch.cognitiveservices.azure.com/bing/v7.0")
keyword = "てす"
# Make a request. Replace Yosemite if you'd like.
web_data = client.web.search(query=urllib.parse.quote(keyword))


def get_keyword(text):
    text = text.replace(u'“', '\"')
    text = text.replace(u'”', '\"')
    text = text.replace("```",'\"')
    if text.find("\"") != text.rfind("\""):
        return text[text.find("\"") + 1:text.rfind("\"")]


print(web_data)
