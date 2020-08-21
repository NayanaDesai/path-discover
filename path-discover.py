import requests
import sys


def path_finder(url):
    extensions = ['php', 'html']
    fp = open('paths.txt', 'r')
    paths = fp.readlines()
    paths = [x.strip() for x in paths]
    print('\n\n*********************** SCANNING FOR HIDDEN PATHS ****************************\n\n')
    for p in paths:
        query = url + p
        res = requests.get(query)
        
        if res.status_code == 200:
            print('Found path:', query)
        
        p_php = p + '.' + 'php'
        query_php = url + p_php
        res_php = requests.get(query_php)

        if res_php.status_code == 200:
            print('Found path:', query_php)

        p_html = p + '.' + 'html'
        query_html = url + p_html
        res_html = requests.get(query_html)

        if res_html.status_code == 200:
            print('Found path:', query_html)

def missing_headers(url):

        security_headers = ['X-Content-Type-Options', 'Strict-Transport-Security', 'X-Frame-Options']
        response = requests.get(url) 
        print('\n\n******************** CHECKING FOR MISSING HTTP RESPONSE HEADERS ********************** \n\n')
        for h in security_headers:
            if h not in response.headers or h.lower() not in response.headers:
                print("Missing header", h)

if __name__ == "__main__":
    url = sys.argv[1]
    path_finder(url)
    missing_headers(url)
    

    

