#Zadanie
#Napisz skrypt, który zapyta o imię i nazwisko z wykorzystaniem input, a następnie przywita się (funkcją print z odpowiednim tekstem) z wykonawcą tego skryptu, nawet jeśli ma najdłuższe na świecie nazwisko.

#Oto co po wywołaniu skryptu powinno pojawić się na ekranie 
#>> Podaj imię i nazwisko:

#A po jego wpisaniu przez użytkownika odpowiedź programu powinna brzmieć:
#>> Witaj John Cleese


#v1
"""
if __name__ == "__main__":
    text = input("Wpisz swóje imię i nazwisko:")
    print("Witaj: ***%s!***" % text)
"""
#v2

"""
def customized_hello(text):

#        Prints hello, based on arguments passed
#        Arguments:
#        first_name,
#        last_name

    print("Hello %s!" % (text))
    
if __name__ == "__main__":
    text = input("Wpisz swóje imię i nazwisko:")
    customized_hello(text)
"""
# v3 Gdybyśmy funkcję tę zamknęli w pliku, to stworzylibyśmy skrypt.
"""
def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    customized_hello("John", "Cleese")
"""

#v3 Moduł sys ma przydatną zmienną argv, która przetrzymuje wszystkie argumenty programu. Dopiszmy więc do naszego skryptu wykorzystanie argv i zobaczmy, co kotek ma w środku.

"""
import sys

def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    print(sys.argv[1:])
    print(sys.argv)
    customized_hello("John","Cleese")
"""


#v4 Przyjmijmy teraz, że nasz skrypt musi przyjąć imię i nazwisko. W innym wypadku nie ma sensu. Zabezpieczymy się, testując liczbę argumentów. Jeśli jest ich za mało, to po prostu wyjdziemy ze skryptu, komendą exit. W tym konkretnym wypadku wywołamy to z parametrem 1, który oznacza, że nastąpił błąd.

import sys

def customized_hello(first_name, last_name, prefix):
    print("Hello %s %s %s!" % (prefix, first_name, last_name ))

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    customized_hello(first_name, last_name, prefix)
