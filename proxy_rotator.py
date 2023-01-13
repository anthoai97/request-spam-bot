import os
import sys
import subprocess

import socket
import requests
import ipaddress
from bs4 import BeautifulSoup as BS
from random import choice as rand_list

import re
import json
import pandas as pd


def proxy_generator(ordered_countries: list=['vn', 'sg', 'id', 'kh', 'cn']):
    proxy_page = 'https://sslproxies.org/'
    proxies_soup = BS(requests.get(proxy_page).content, 'html5lib')

    # Extract
    data = []
    for proxy_row in proxies_soup.find('tbody').findAll('tr'):
        proxy_data = [e.text for e in proxy_row.findAll('td')]
        data.append(proxy_data)
    df = pd.DataFrame(data, columns=['ip', 'port', 'country_code', 'country', 
                                     'anonimity', 'google_enability', 'https_enability', 'last_check',])

    def validate_ip_address(address):
        try:
            ip = ipaddress.ip_address(address)
            return address
        except ValueError:
            return None

    def generate_proxy(ip, port):
        return f'{ip}:{port}'
    
    df['country_code'] = df['country_code'].str.lower()
    df['ip'] = df['ip'].apply(validate_ip_address)
    df.dropna(subset=['ip', 'port'], inplace=True)
    df['proxy'] = df[['ip', 'port']].apply(lambda x: generate_proxy(x.ip, x.port), axis=1)

    df_ordered = pd.DataFrame()
    while (len(df_ordered) == 0) and (len(ordered_countries) > 0):
        country = ordered_countries.pop(0)
        df_ordered = pd.concat([df_ordered, df[df.country_code==country]], ignore_index=True)

    # print(df_ordered[['proxy', 'ip', 'port', 'country']])
    proxies = df_ordered['proxy'].values.tolist()
    return rand_list(proxies)


def get_ip_and_hostname():
    hostname =  socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr, hostname


if __name__ == "__main__":
    proxy = proxy_generator(["us"])
    print(proxy)
    ip_addr, hostname = get_ip_and_hostname()
    print(ip_addr)
    print(hostname)



