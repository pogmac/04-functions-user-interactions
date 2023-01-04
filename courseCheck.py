def demo_function():
    print("I am inside of a function!")

demo_function()    

def add_two_numbers(a,b):
    print("sum = ", a+b)

add_two_numbers(23,12)    

a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)

print() 
def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: " + '\n''\n'
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

#print(shopping())

shoppping_result = shopping()
print(shoppping_result)

def no_result_function():
    print("I am just printing I love you")
    print("and returning nothing to you!")

no_result_function(); print()
print(type(no_result_function()))

def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

#Taka krotka może zostać rozpakowana automatycznie, w zwykły, znany Ci sposób.
first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)

def customized_hello(first_name, last_name):
    print("Hello Mr %s %s!" % (first_name, last_name))
    print("Hello Mr", first_name, last_name,"!")
    print(f"Hello Mr {first_name} {last_name}!")

customized_hello("John", "Cleese");print()

def customized_hello(first_name, last_name, gender_prefix ='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name}!")

customized_hello("John", "Cleese");print()

customized_hello("Clara", "Cleese","Ms");print()

# Funkcja z zakupami

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy"
]

def shopping(items):
    shopping_cart = "Koszyk zawiera: " +'\n''\n'
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart
    

basket = shopping(shopping_items)
print(basket)

def shopping(items,payment ='card',shop='local'):
    print(payment);print(shop)
    pass

shopping(shopping_items)

shopping(shopping_items, 'card', 'supermarket')
shopping(shopping_items, shop='supermarket')
shopping(shopping_items, payment='cash')
shopping(shopping_items, 'supermarket')

# Różne typy argumentów
def shopping(items, *, payment='card', shop ='local'):
    print(payment);print(shop)
    pass
#shopping(shopping_items, 'cash')
shopping(shopping_items, payment='cash', shop ='supermarket')

def name(positional_only_parameters, /, positional_or_keyword_parameters,
         *, keyword_only_parameters):
         pass


name(1,positional_or_keyword_parameters=2,keyword_only_parameters=3)
name(1,2,keyword_only_parameters=3)         

#Żeby dobrze sobie to przećwiczyć, zadeklaruj trzy funkcje z pustą implementacją, czyli z komendą pass. Pierwsza z nich, fun_default, powinna przyjmować argumenty pozycyjne albo nazwane. Druga, fun_positional, tylko pozycyjne. Trzecia, fun_keyword, tylko nazwane. Testem na to, czy druga i trzecia funkcja jest dobrze zadeklarowana będzie próba podstawienia argumentów odwrotnie, niż było w planie, czyli np. do fun_keyword, próba podania argumentów pozycyjnych.
def fun_default(items, /,payment ='card', shop='local'):
    print(),print(payment);print(shop)
    pass

fun_default(shopping_items,"cash","supermarket")

def fun_positional(items, payment ="card",shop = "local", /):
    print(),print(payment);print(shop)
    pass
fun_positional(shopping_items,"cash","supermarket")

def fun_keyword(items, *,payment ='card', shop='local'):
    print(),print(payment);print(shop)
    pass
fun_keyword(shopping_items,payment ="cash", shop ="supermarket")

print("Jedna i dwie gwiazdki:");print()

def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3, "A");print()

def count_them_all(*args, **kwargs):
    print(f"I have received {len(args)} positional arguments")
    print(f"I have received {len(kwargs)} named arguments")

count_them_all(1, 2, 3, "A", a=1, b=2);print()

print(" Lambda");print()

shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

sorted_items = sorted(shopping_items, key=get_index_1_tuple_element, reverse=True)
print(sorted_items)



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

customized_hello("John","Cleese")
