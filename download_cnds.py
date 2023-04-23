# coding:utf-8

import json
import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def saveHtml(file_name, file_content):
    with open('./openstack/' + file_name.replace('/','_')+'.html',"wb") as f:
        f.write(file_content)

# html = getHtml(url)

# saveHtml("1",html)


def open_json_file(path='./content.json'):
    with open(path, 'r') as f:
        json_str = json.load(f)
    data = json_str['data']['urls']
    return data

data = open_json_file()

for item in data:
    html = getHtml(item.get('targetUrl'))
    saveHtml(item.get('title'),html)
