# vetor e forIn
# vetor = [0,1,2,3]

# for numero in vetor:
#     print(numero)

# vetor.append(8)
# print(vetor)

# quantidade = 0

# for letra in 'batata':
#     if letra == 'a':
#         quantidade+=2

# print(quantidade)

numero = int(input('Digite um número para montar uma tabuada: '))

for i in range(1, 11):
    print(i, 'x', numero, '=', i*numero)

