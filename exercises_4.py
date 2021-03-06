# Zadanie 1
# Napisz funkcję create_list, która przyjmie dwa argumenty dowolnego typu, a następnie zwróci listę, której kolejne elementy będą parametrami powtórzonymi czterokrotnie.

# Przykład:
# my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
# my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]
from typing import Dict


def create_list(x, y):
    return [x,y]*4
print(create_list(1,2))

# Zadanie 2
# Napisz funkcję list_keys(d), gdzie d to dowolny słownik. Niech funkcja przeiteruje pętlą for po kluczach słownika i zwróci listę tych kluczy. Sprawdź w dokumentacji, czy można zrobić to prościej.
def list_keys(d):
    array =[]
    for i in d:
        array.append(i)
    return array
    # return Dict.keys(d)
print(list_keys({1:'1',2:'2','ja':'ja', 'ty':3}))

# Zadanie 3.
# Napisz funkcję find_short_words, która przyjmie listę wyrazów. Funkcja powinna zwrócić listę słów krótszych od 5 znaków.
# Przykład
#
# l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
# print(l)
#
# ['moja', 'ty', 'jak']
def find_short_words(l):
    array =[]
    for i in l:
        if len(i) < 5:
            array.append(i)
    return array

print(find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))



# Zadanie 4.
# Napisz funkcję suma(numbers) gdzie numbers to lista liczb dowolnego typu. Funkcja powinna zwrócić sumę wszystkichh elementów listy numbers.
# Dla uproszczenia możesz przyjąć, że wszystkie parametry wprowadzone przez programistę będą poprawnymi liczbami.
def suma(numbers):
    return sum(numbers)
print(suma([1,2,3,4,5]))


# Zadanie 5.
# Napisz funkcję mean(numbers), gdzie numbers to lista liczb dowolnego typu. Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers. Czy znasz jakiś sposób, by ułatwić sobie pracę?
def mean(numbers):
    return sum(numbers)/len(numbers)
print(mean([1,2,3,4,5]))


# Zadanie 6.
#
# Napisz funkcję message, która jako parametr przyjmie słownik o następujących kluczach:
#
#     name,
#     role,
#     movie.
#
# Następnie niech funkcja przygotuje sformatowany napis: "In movie, name is a role.", gdzie w odpoweidnie miejsca podstawi wartości z ww. kluczy.
# Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość None.
# Przykład:
#
# input_dict = {
#     "name": "Han Solo",
#     "role": "smuggler",
#     "movie": "Star Wars"
# }
#
# print(message(input_dict))
#
# Wynik:
#
# In Star Wars, Han Solo is a smuggler.
#
# input_dict = {
#     "name": "Bilbo Baggins",
#     "role": "burglar"
# }
#
# print(message(input_dict))
#
# Wynik:
#
# None
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars",
}
def message(i_d):
    name = i_d.get('name')
    role = i_d.get('role')
    movie = i_d.get('movie')
    ret_sting = f"In {movie}, {name} is a {role}."
    return ret_sting

def message2(slownik):
    try:
        name = slownik['name']
        movie = slownik['movie']
        role = slownik['role']
    except Exception as  e:
        return None
    ret_sting = f"In {movie}, {name} is a {role}."
    return ret_sting

print(message(input_dict),)
print(message2(input_dict))