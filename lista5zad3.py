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


def znajdz_odnosniki(url):
    try:
        html_file = wczytaj_strone(url)

        regex = re.compile('http://' + '([a-zA-Z]+\.)*[a-zA-Z]+')
        urls = [url.group() for url in regex.finditer(html_file)]
        return urls
    except Error as e:
        return []


def idz_glebiej(url, slowo):
    urls = znajdz_odnosniki(url)
    global ile
    if ile < glebokosc:
        ile += 1
        for url in urls:
            idz_glebiej(url, slowo)
            try:
                html_file = wczytaj_strone(url)

                return html_file.count(slowo)
            except Error as e:
                return 0
    else:
        try:
            html_file = wczytaj_strone(url)

            return html_file.count(slowo)
        except Error as e:
            return 0


def start(slowo):
    global glebokosc
    glebokosc = 5
    L = []

    try:
        urls = znajdz_odnosniki('http://python.rk.edu.pl/')
    except urllib2.URLError as err:
        raise Error("No network connection")

    for url in urls:
        global ile
        ile = 0
        L.append(idz_glebiej(url, slowo))
    pass


start('Python')