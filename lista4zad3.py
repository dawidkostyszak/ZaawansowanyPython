from itertools import imap


def generator_zdania(tekst):
    zdanie = ''
    for litera in tekst:
        if litera == '\n':
            yield zdanie
            zdanie = ''
        else:
            zdanie += litera

    yield zdanie


def korekta(zdanie):
    poczatek = True
    poprawione_zdanie = ''

    if zdanie:
        for litera in zdanie:
            if litera.islower() and poczatek:
                poprawione_zdanie += litera.upper()
                poczatek = False
            elif litera.isupper() and poczatek:
                poprawione_zdanie += litera
                poczatek = False
            elif litera.isupper() and not poczatek:
                poprawione_zdanie += litera.lower()
            elif litera == '.':
                return poprawione_zdanie + litera
            else:
                poprawione_zdanie += litera

        return poprawione_zdanie + '.'
    else:
        return zdanie

plik = open('plik.txt', 'r')
tekst = plik.read()

for i in imap(korekta, generator_zdania(tekst)):
    print i