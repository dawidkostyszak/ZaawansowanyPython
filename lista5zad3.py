from sets import Set
import re
import urllib2


class Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def wczytaj_strone(url):
    try:
        response = urllib2.urlopen(url, timeout=1)
        html_file = response.read()
        response.close()
    except Exception as e:
        raise Error('Strona nie istnieje')

    return html_file


def policz_wystapienie_slowa(url, slowo):
    try:
        html_file = wczytaj_strone(url)
        return html_file.count(slowo)
    except Error as e:
        return 'Strona nie istnieje'


def znajdz_odnosniki(url):
    try:
        html_file = wczytaj_strone(url)

        regex = re.compile('http://' + '([a-zA-Z]+\.)+[a-zA-Z]+')
        urls = Set(
            u.group() for u in regex.finditer(html_file) if u.group() != url
        )
        return urls
    except Error as e:
        return []


def idz_glebiej(url, slowo, wynik):
    urls = znajdz_odnosniki(url)
    global ile
    if ile < glebokosc:
        ile += 1
        for u in urls:
            wynik = idz_glebiej(u, slowo, wynik)
            try:
                wynik[url] = policz_wystapienie_slowa(url, slowo)
                return wynik
            except Error as e:
                wynik[u] = 'Strona nie istnieje'
                return wynik

        wynik[url] = 'Strona nie istnieje'
        return wynik

    else:
        try:
            wynik[url] = policz_wystapienie_slowa(url, slowo)
            return wynik
        except Error as e:
            wynik[url] = 0
            return wynik


def start(slowo):
    global glebokosc
    glebokosc = 2
    wynik = {}
    url = 'http://python.rk.edu.pl'

    try:
        urls = znajdz_odnosniki(url)
    except urllib2.URLError as err:
        raise Error("Strona nie istnieje")

    for u in urls:
        global ile
        ile = 0
        wynik = idz_glebiej(u, slowo, wynik)

    for k, v in wynik.items():
        print k, v

    print '<--------------'


start('Python')


# def start2(slowo):
#     try:
#         urls = znajdz_odnosniki('http://python.rk.edu.pl')
#     except urllib2.URLError as err:
#         raise Error("Strona nie istnieje")
#
#     for url in urls:
#         try:
#             html_file = wczytaj_strone(url)
#             print url, html_file.count(slowo)
#         except Error as e:
#             print url, e.value
#
# start2('Python')