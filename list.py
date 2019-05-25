lista = list(range(0,3))

# adiciona algo numa lista
lista.append('python')
lista.append(10)

# remove algo numa lista
lista.remove('gabriel')

# find index of a property in a list
lista.index('gabriel')

# conta numero de ocorrencias de uma certo valor numa lista
lista.count('gabriel')

# ordenar uma lista
lista.sort()

# print a lista
print(lista)

list = [
    {
        'id': 1,
        "name": "Luke Skywalker",
        "height": "172",
        "birth_year": "19BBY",
        "gender": "male",
    },
    {
        'id': 2,
        "name": "C-3PO",
        "birth_year": "112BBY",
        "gender": "n/a",
    },
    {
        'id': 3,
        "name": "Darth Vader",
        "birth_year": "41.9BBY",
        "gender": "male",
    }
]
a = 2
len(list)

for i in range(0, len(list)):
    print(list[i])