import requests
import re
from urllib.parse import urlparse, urlunparse
import re
import requests
from bs4 import BeautifulSoup

def getData(url):
    response = requests.get(url)
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(response.content, 'html.parser') # lấy html
    links = soup.find_all('a')
    accessible_links = []
    html_links = []
    list_final=[]
    for link in links:
        try:
            href =link.get('href')
            suffix = href.split("/")[-1]
            href2 =url+suffix

            if href2.startswith('http'):
                try:
                    response = requests.get(href2)
                    if response.status_code == 200:
                            accessible_links.append(href2)
                except:
                    pass
        except:
            pass
    for link in accessible_links:
        html_links.append(loc_html(link))
        #print(link)
    unique_links = list(set(html_links))
    for i in unique_links:
        # print(i)
        try:
            i=add_html_extension(i)
            if i.startswith('http'):
                response = requests.get(i)
                if response.status_code == 200:
                        x=layhtml_con(i)
                        # print(x)
                        list_final.extend(x)
        except:
            i=add_html_extension_htm(i)
            if i.startswith('http'):
                response = requests.get(i)
                if response.status_code == 200:
                        x=layhtml_con(i)
                        # print(x)
                        list_final.extend(x)
    return list_final

def add_html_extension(url):
    parsed_url = urlparse(url)
    if not parsed_url.path.endswith('.html'):
        path_with_extension = parsed_url.path + '.html'
        new_url_parts = (parsed_url.scheme, parsed_url.netloc, path_with_extension, 
                         parsed_url.params, parsed_url.query, parsed_url.fragment)
        url = urlunparse(new_url_parts)
    return url
def add_html_extension_htm(url):
    parsed_url = urlparse(url)
    if not parsed_url.path.endswith('.htm'):
        path_with_extension = parsed_url.path + '.htm'
        new_url_parts = (parsed_url.scheme, parsed_url.netloc, path_with_extension, 
                         parsed_url.params, parsed_url.query, parsed_url.fragment)
        url = urlunparse(new_url_parts)
    return url

def loc_html(url):
    if re.findall(r'\.html$', url):
            dx = url.split(".html")[0]
            url=dx
    else:
        if re.findall(r'\.htm$', url):
            dx2 = url.split(".htm")[0]
            url=dx2
    return url

def layhtml_con(url):
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href1 = link.get('href')
        try:
            href=href1.split("/")[-1]
            if href is not None:
                xxx=url.split(".html")[0]+'/'+href
                links.append(xxx)
        except:
            pass
    links=list(set(links))
    return links