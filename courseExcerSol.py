# 4.1. Wprowadzenie do funkcji

# Definicja i wywołanie
# 4.1.1 Napisz funkcję demo_function() która będzie drukowała na ekran tekst "I am inside of a function" (komenda def ... :)

def demo_function(): # nazwa funkcji - powinna opisywać, czym funkcja się zajmuje. 
    print("I am inside of a function!") # blok kodu funkcji

#demo_function()  # wywołanie funkcji

# 4.1.2 Stwórz funkcję, w której dodasz dwie liczby i wyświetl to na ekranie. Jak ją nazwiesz? Funkcję stworzysz z użyciem def. W ciele umieść operację i funkcję print.

# Widoczność zmiennej
# 4.1.3 Stwórz zmienną 'a' poza funkcją a następnie zadeklaruj ją dodatkowo w ciele funkcji (within function's body). Wywołaj funkcję i wydrukuj potem zmienną 'a'.Które 'a' zostało wydrukowane?

a = 1

def scope_demo():
    a = 2
    print(a)

#scope_demo()
#print(a)

# jeśli zadeklarujemy zmienną w bloku, jest ona widoczna tylko dla tego bloku. Pierwsze 'a' jest widoczne w bloku z zerowym wcięciem a drugie tylko w bloku funkcji scope_demo()

# Zwracana wartość

# 4.1.4 Stwórz listę shopping_items a następnie w funkcji przpisz na zmienną shopping_cart tekst "Koszyk zawiera: " oraz listę produktów w osobnych liniach. Zwróć (return) zmienną shopping_cart.

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

#print(shopping()) 

#shopping_result = shopping() # alternatywa przypisanie rezultatu funkji na zmienną i wyświetlenie jej. Zaleta: możemy rezultatu użyć wielokrotnie dla raz wywołanej funkcji.
#print(shopping_result)

# 4.1.5 Brak rezultatu? Stwórz funkcję bez resultatu (return None) sprawdź jakiego typu jest none

def no_result_function():
    print("test")

#result = no_result_function()
#print(type(result))    

# 4.1.6 Więcej wyników. Stwórz funkcję która zwróci nam krotkę z czterema elementami a następnie przypisz do zmiennych jej wartości.

def multi_results():
    return "morning", "afternoon","evening", "night"

#print(multi_results())

#time1, time2, time3,time4 = multi_results()
#print(time2)
#print(f'Trzeci element listy to "{time3}"')

# 4.2. Argumenty funkcji

# 4.2.1 Zefiniuj dwa argumenty 'a' i 'b' i dodaj je w ciele (body) funkcji.

a = 2
b = 2
def dod(a,b):
    print(a+b)
#dod(a,b)    

#Argumenty tekstowe
# 4.2.2 Jaka jest różnica między parametrami  a argumentami funkcji?

"""
What is the difference between arguments and parameters?¶
Parameters are defined by the names that appear in a function definition, whereas arguments are the values actually passed to a function when calling it. Parameters define what types of arguments a function can accept. For example, given the function definition:

def func(foo, bar=None, **kwargs):
    pass
foo, bar and kwargs are parameters of func. However, when calling func, for example:

func(42, bar=314, extra=somevar)
the values 42, 314, and somevar are arguments.
"""

# 4.2.3  Stwórz funkcję customized_hello() z dwoma parametrami first_name i last_name, która wydrukuje powitanie na ekranie.

def customized_hello(first_name, last_name):
    #print("Hello Mr %s %s" % (first_name, last_name)) # stara metoda phyton 2. lub starszy
    print(f"Hello Mr {first_name} {last_name}") # nowa metoda od wersji 3.

#customized_hello("John", "Cleese")    

# Argumenty domyślne
# 4.2.4 Stwórz funkcję customized_hello() z trzema parametrami: first_name, last_name i gender_prefix(domyślnie = 'Mr'), która wydrukuje powitanie na ekranie. 

def customized_hello(first_name, last_name, gender_prefix = 'Mr'):
    print("Hello %s %s %s!" % (gender_prefix,first_name,last_name))

#customized_hello("John","Cleese")
#customized_hello("John","Cleese", "Ms")

# Funkcja z zakupami

# 4.2.5 Chcemy napisać funkcję, która tworzy koszyk zakupów na podstawie podanych jej argumentów. Zacznijmy od zdefiniowania listy produktów jako zmiennej shopping_items. Następnie podamy tę zmienną jako argument funkcji shopping(). Utworzymy też zmienną basket, do której przypiszemy wywołanie funkcji.

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki"
]

def shopping(items):
    shopping_cart = "Lista zakupów to:" + '\n'
    for item in items:
        shopping_cart +=  item + '\n'
    return shopping_cart 

#basket = shopping(shopping_items)    
#print(basket)

# Pozycja albo klucz

# 4.2.6 Rozszerzymy teraz naszą funkcję. Weźmy dodatkowe czynniki pod uwagę. Po pierwsze chcemy zdecydować – płacimy gotówką czy kartą. Po drugie interesuje nas rodzaj sklepu, do którego idziemy. Przyjmiemy, że najczęściej płacimy kartą (ustawiamy więc domyślny payment='card') oraz idziemy do pobliskiego sklepu osiedlowego (shop='local'). 
# Wywołaj funkcję z domyślnymi argumentami
# Wywołaj funkcję z nadpisanymi argumentami
# Spróbuj kilka kombinacji argumentów domyślnych i nadpisanych

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki"
]

def shopping(items, payment = "card", shop = "local"):
    print("Idę do %s " %(shop))
    print("Płacę %s" %(payment)); print()
    shopping_cart = "Lista zakupów to:" + '\n'
    for item in items:
        shopping_cart +=  item + '\n'
    return shopping_cart 
    

#basket = shopping(shopping_items)  # domyślne argumenty 
#print(basket)
#basket = shopping(shopping_items, "cash", "supermarket") # nadpisane argumenty. Możemy również je zdefiniować tak jak do tej pory, poprzez pozycję (positional arguments)
#basket = shopping(shopping_items, shop ="supermarket", payment="cash") # nadpisane argumenty. Możemy również je zdefiniować jako keyword/named arguments (argumenty po kluczu/nazwane). Co ciekawe funkcja zadziała poprawnie również jak zamieniym miejscami argumenty po kluczu.
#basket = shopping( shop ="supermarket", payment="cash", shopping_items) # Ale argumentu   
#basket = shopping(shopping_items, shop ="supermarket") # można wywołać funkcję wybierając tylko jeden argyment po kluczu (keyword argument)
#basket = shopping(shopping_items, "supermarket", payment ="cash") #natomiast to już nie zadziała 
#basket = shopping(shopping_items, "supermarket") # tu też argument "supermarket" zostanie przypisany na pierszą zmienna domyślną "payment"
#basket = shopping(shopping_items, "cash") # to z kolei zadziała 
#print(basket)

# Pozycyjne albo nazwane
# Różne typy argumentów
# 4.2.7 Za pomocą "*" wymuś żeby argumenty payement i shop były tylko wywoływane przy pomocy ich nazwy/klucza (argumenty nazwane/ po kluczu named keyword arguments)

def shopping(items, *, payment= 'cash',shop ='local'):
    pass
shopping(shopping_items, payment="card", shop ="supermarket")

# 4.2.8 Tak więc slash (/) rozdziela nam argumenty tylko pozycyjne od standardowych, a gwiazdka (*) rozdziela standardowe od nazwanych. zdefiniuj funkcję, która będzie przyjmowała trzy argumenty 1. positional_only_parameter! 2. postional_or_keyword, 3. keyword_only_parameter

def name(positional_only_parameter, / , positional_or_keyword_parameter, *, keyword_only_parameter):
    pass

name("sdafsdf", "sdfa", keyword_only_parameter="sdfs")# Runs ok
#name("sdafsdf", "sdfa", "sdfs") # Rerutrns error
name("sdafsdf", positional_or_keyword_parameter="sdf", keyword_only_parameter="sdfs") # Runs ok

#name(positional_only_parameter="sdafsdf", positional_or_keyword_parameter="sdf", keyword_only_parameter="sdfs") # returns error

# 4.2.9 Ćwiczenie. Żeby dobrze sobie to przećwiczyć, zadeklaruj trzy funkcje z pustą implementacją, czyli z komendą pass.

#Pierwsza z nich, fun_default, powinna przyjmować argumenty pozycyjne albo nazwane. Druga, fun_positional, tylko pozycyjne. Trzecia, fun_keyword, tylko nazwane. Testem na to, czy druga i trzecia funkcja jest dobrze zadeklarowana będzie próba podstawienia argumentów odwrotnie, niż było w planie, czyli np. do fun_keyword, próba podania argumentów pozycyjnych.

#Jedna i dwie gwiazdki

# 4.2.10 za pomocą funkcji "*" zbierz wszystkie argumenty pozycyjne do jednej listy args

def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

#count_them_all(1, 2, 3, "A")

# 4.2.11 za pomocą funkcji "*" i "**" zbierz wszystkie argumenty pozycyjne do jednej listy args a nazwane do słownika kwargs (nazwa:wartość)

def count_them_all(*args, **kwargs):
    print(args)
    print(kwargs)
    pass

#count_them_all(1, 2, 3, "A", a=1, b=2)

#Lambda
#Kiedy masz do wykonania jakąś małą funkcjonalność, która jest przetworzeniem, nie zawsze potrzebujesz funkcji. W Pythonie istnieje wybór – stworzysz pełnoprawną funkcję albo napiszesz proste wyrażenie o nazwie lambda. Jest ono szczególnie potrzebne, gdy chcesz przekazać funkcję jako argument.

# 4.2.12 
"""
shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

#Gdybyśmy chcieli poukładać elementy po cenie za kilogram albo po ilości, to możemy skorzystać z regularnej funkcji.
sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
print(sorted_items)


sorted_items = sorted(shopping_items, key=get_index_1_tuple_element, reverse = True)
print(sorted_items)

#Możemy jednak posłużyć się wyrażeniem lambda i zapisać to w taki sposób:

sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])
print(sorted_items)
"""
#Wyrażenie lambda przyjmuje więc zapis ze słowem kluczowym lambda, a następnie mamy zmienną, która będzie przetwarzana i rezultat przetwarzania po dwukropku.

#Dokumentacja
# 4.2.13 Wywołaj Help na funkcji print()

#help(print())

#W Pythonie możesz zdefiniować dokumentację dla swojej funkcji w bardzo łatwy sposób. Po prostu zadeklaruj tekst na jej początku. Teraz każdy, kto będzie chciał się dowiedzieć, jak działa Twoja funkcja i jak interpretować jej argumenty, będzie mógł się tego dowiedzieć dzięki funkcji help().

# 4.2.14 na poniższej funkcji przetestuj help()

def customized_hello(first_name, last_name, gender_prefix='Mr'):
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """
    print("Hello %s %s %s" % (gender_prefix, first_name, last_name))

#help(customized_hello)

#4.2.15 Zadanie: palindromy
# Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

#4.3. Interakcja z użytkownikiem — IO

"""
#4.3.1 
Stwórz na swoim komputerze plik, który zawiera jedną linijkę:
print("Greetings from file!")
Nazwij go skrypt.py i uruchom go tą komendą:
python skrypt.py
"""
"""
if __name__ == "__main__":
    print("main")
    pass
"""
    # here you have a place to write code that will be
    # executed after python <path_to_this_script.py>
    # Ten blok będzie wykonany wyłącznie wtedy, gdy skrypt jest bezpośrednio uruchomiony.
    # Pozostały kod, który znajduje się poza tą klauzulą, zadziała także wtedy, gdy nasz skrypt jest importowany


#4.3.2 Zacznijmy jednak od wydrukowania listy naszych zakupów razem ze sposobem płatności i miejscem kupna. Rozszerzmy naszą funkcję z tego modułu i dopiszemy do niej prostą funkcjonalność:

def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
#print(text) 

#Z technicznego punktu widzenia w środku naszej funkcji tworzymy tekst, który jest zwracany jako rezultat.

#4.3.3 Przetestuj przyjmowanie parametrów:

"""
print("Pokażę wszystko, co wpiszesz!")
text = input()
print("Oto Twój tekst: ***%s***" % text)
"""
# Bardziej przejrzysta wersja tego kodu:
"""
print("Pokażę wszystko, co wpiszesz!")
text = input("Wpisz swój tekst:")
print("Oto Twój tekst: ***%s***" % text)
"""

#4.3.4 

#W naszym krótkim programie będziemy posługiwać się listą. OK, ale jak przekazać ją do skryptu? Niech lista, która jest podawana, będzie tekstem dzielonym przecinkami. Do tego celu użyjemy funkcji split.

"""
items_text = "cola,whiskey,lód"
items = items_text.split(',')
print(items)
print(type(items))
print(len(items))
"""
#Napiszmy skrypt w Pythonie, który będzie pobierał pojedynczy tekst (rozdzielony przecinkami), a następnie stworzy opis naszych zakupów na tej podstawie.

def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result
"""
if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone)przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)
"""

#4.3.5 Napisz skrypt, który zapyta o imię i nazwisko z wykorzystaniem input, a następnie przywita się (funkcją print z odpowiednim tekstem) z wykonawcą tego skryptu, nawet jeśli ma najdłuższe na świecie nazwisko.

#v1
"""
if __name__ == "__main__":
    text = input("Wpisz swóje imię i nazwisko:")
    print("Witaj: ***%s!***" % text)
"""

#Przykład użycia argumentów

#4.3.6 W programie możemy oczywiście prosić użytkownika o dane wielokrotnie i na podstawie odpowiedzi uruchamiać odpowiednie reakcje. Spójrz choćby na poniższy przykład. Przebieg programu jest tutaj zależny od płci użytkownika:

"""
print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
adult = None
sex = input("Podaj proszę swoją płeć [M/K]: ")
if sex == 'M':
    age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
    over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
    adult = (over18_yesno == 'T')
else:
    print("Nie ma takiej płci!")
    exit(1)
print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))
"""

# Przy okazji, zwróć uwagę na wykorzystanie funkcji exit(), która kończy działanie programu. Jeśli podamy błędną płeć, wywołamy exit z parametrem 1, który oznacza, że nastąpił pewien błąd. Zwykle, gdy program kończy się poprawnie, to rezultat skryptu ma wartość 0.

# Argumenty programu

#Zdarzają się sytuacje, gdy od początku wiemy jakie argumenty od użytkownika będą nam potrzebne. Nie musimy wtedy czekać aż kod “dojdzie” do polecenia input. Możemy podać je od razu, przy uruchomieniu. Są to tzw. argumenty skryptu.

#Moduł sys ma przydatną zmienną argv, która przetrzymuje wszystkie argumenty programu. Dopiszmy więc do naszego skryptu wykorzystanie argv i zobaczmy, co kotek ma w środku.

# 4.3.7 Wywołaj poniższy kod przez python "nazwa_skryptu".py 
"""
import sys

def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Cleese")
"""


# 4.3.8 Przyjmijmy teraz, że nasz skrypt musi przyjąć imię i nazwisko. W innym wypadku nie ma sensu. Zabezpieczymy się, testując liczbę argumentów. Jeśli jest ich za mało, to po prostu wyjdziemy ze skryptu, komendą exit. W tym konkretnym wypadku wywołamy to z parametrem 1, który oznacza, że nastąpił błąd.

"""
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
"""

# 4.4. Logowanie i błędy

import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)