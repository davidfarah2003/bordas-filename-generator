import urllib.request
import urllib.error

with open("links.txt", 'r') as file:
    urls = []
    url_list = file.readlines()
    for url in url_list:
        if "\n" in url:
            url = url.rstrip("\n")
        urls.append(url)
    print(urls)

try:
    r = urllib.request.urlopen("https://biblio.editions-bordas.fr/epubs/BORDAS/bibliomanuels/ressources/9782047337639/733763_ESPACE_Tle_LDP_integral.pdf")
    print(r.code)
except urllib.error.HTTPError as e:
    print(e.code)