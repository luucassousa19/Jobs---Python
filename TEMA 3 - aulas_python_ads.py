# -*- coding: utf-8 -*-
"""AULAS PYTHON ADS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-0rhrVwQ7-8KvQ0HWaqjK9yd124wqU93
"""

print("ola, mundo")

"""# **ASPAS SIMPLES**"""

print(12345)
print('valor',12345)
print('valor = {}'.format(12345))
print(f'valor = {12345}')

"""# **ASPAS DUPLAS**"""

print(12345)
print("valor",12345)
print("valor = {}".format(12345))
print(f"valor = {12345}")

"""# **EXEMPLO DE ATRIBUIÇÃO MULTIPLA**"""

# Atribuição Multipla
a,b = 1,2
print('Antes da Troca')
print(f"O valor das variaveis: a={a}, b={b}")

# Primeira Troca
temp = a
a = b
b = temp
print('Primeira troca')
print(f"O valor das variaveis: a={a}, b={b}")

# Segunda Troca
a, b = b, a
print('Segunda troca')
print(f"O valor das variaveis: a={a}, b={b}")

"""# **OPERADORES COMPOSTOS**"""

X = 10
print(f"X={X}")

X += 2
print(f"X={X}")

X -= 2
print(f"X={X}")

X *= 2
print(f"X={X}")

X /= 2
print(f"X={X}")

X %= 2
print(f"X={X}")

"""# **SEQUENCIAIS E DICIONARIOS**"""

#### SEQUENCIAIS
# posições de cada número da lista ( 101 - posição zero / 202 - posição um / 303 - posição dois / 404 - posição três / 505 - posição quatro)
lista = [101,202,303,404,505]

print(f'lista[0] ={lista[0]}')
print(f'lista[0] ={lista[1]}')
print(f'lista[0] ={lista[2]}')
print(f'lista[0] ={lista[3]}')
print(f'lista[0] ={lista[4]}')
print(f'lista completa:{lista}')

### DICIONARIO
pessoas = {1111:['nome 01'],2222:['nome 02'],3333:['nome 03'],4444:['nome 04'] }

pessoas

print(f'primeira pessoa = {pessoas[1111]}')

print(f'quarta pessoa = {pessoas[4444]}')

"""# **EXERCICIOS**"""

# Exercicio 1) Qual resultado da operação a+b+c:

a = ['10']
b = ['20']
c = ['30']

# Guarda a junção das 3 listas em uma nova variavel:
r = a+b+c

# Imprimi resultado:
print(f'r = {r}')

# Exercicio 2) Qual resultado da operação a*2+b*3+c*4:

# Guarda/Concatena as 3 listas em uma nova variavel:
r2 = a * 2 + b * 3 + c * 4

# Imprimi resultado:
print(f'r2 = {r2}')

# Exercicio 3) Obter a raiz da equação do primeiro grau f(x) = ax+b
#f(x) = ax+b
# x = -b/a com a diferente de zero
a = 10
b = 5
x = -b/a
print('A raiz da equação do primeiro grau é: x = {}'.format(x))

x = 2
y = 4
x = x / y
y = y / x
print(y)

