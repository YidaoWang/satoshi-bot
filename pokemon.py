import json
import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

with open("data/pokedex.json") as f:
    pokedex = json.load(f)
with open("data/moves.json") as f:
    moves = json.load(f)
with open("data/items.json") as f:
    items = json.load(f)
with open("data/types.json") as f:
    types = json.load(f)
#with open("data/pokedata.yaml") as f:
#    pokedex_swsh = yaml.load(f)
#with open("data/pokemon_swsh_img.json") as f:
#    swsh_imgs = json.load(f)

exeption_poke = []
# 名前中に他のポケモンを含む
for poke1 in pokedex:
    for poke2 in pokedex:
        if poke1['id'] == poke2['id']:
            continue
        if poke1['name']['japanese'] in poke2['name']['japanese'] \
        or poke1['name']['english'] in poke2['name']['english']:
            exeption_poke.append(poke2)

def pokemon(name):
    for poke in pokedex:    
        if poke["name"]["japanese"] == name \
        or poke["name"]["english"] == name:
            return poke

def pokemon_by_id(id):
    for poke in pokedex:    
        if poke["id"] == id:
            return poke

def pokemon_in_content(content):
    res = []
    # 例外ポケ処理
    for e in exeption_poke:
        if e['name']['japanese'] in content:
            res.append(e)
            content = content.replace(e['name']['japanese'], "")
        elif e['name']['english'] in content:
            res.append(e)
            content = content.replace(e['name']['english'], "")
    # その他
    for poke in pokedex:
        if  '（' in poke["name"]["japanese"]:
            name_s = poke["name"]["japanese"].split('（')[0]
            if name_s in content:
                res.append(poke)
        elif poke["name"]["japanese"] in content:
            res.append(poke)
        elif poke["name"]["english"] in content:
            res.append(poke)
    return res

def moves_in_content(content):
    res = []
    for move in moves:    
        if move["ename"] in content \
        or move["jname"] in content:
            res.append(move)
    return res

def items_in_content(content):
    res = []
    for item in items:    
        if item["name"]["japanese"] in content \
        or item["name"]["english"] in content:
            res.append(item)
    return res

def types_in_content(content):
    res = []
    for type in types:    
        if type["japanese"] in content \
        or type["english"] in content:
            res.append(type)
    return res

def pokemon_image(id, type="image"):
    if type == "image":
        if id < 810:
            return "data/images/{:03}.png".format(id)
        else:
            return "data/thumbnails/{:03}.png".format(id)
    if type == "sprite":
        return "data/sprites/{:03}MS.png".format(id)
    if type == "thumbnail":
        return "data/thumbnails/{:03}.png".format(id)

def find_type(key, lang):
    for t in types:
        if key == t['english'] or key == t['chinese'] or key == t['japanese']:
            return t[lang]
