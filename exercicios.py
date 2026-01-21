# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
resultado = numero1 + numero2
print(resultado)

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero1 = int(input('Digite um número: '))
resto = numero1 % 5 
print(f'O resto da divisão por 5 é {resto}')

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
resultado = numero1 * numero2
print(resultado)

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
resultado = numero1 // numero2
print(resultado)

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário
numero1 = int(input("Digite um número: "))
quadrado = numero1 ** 2
print(quadrado)

# %%

# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
resultado = numero1 + numero2
print(resultado)
# %%
# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
resultado = (numero1 + numero2) / 2
print(resultado)
# %%
# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário)
base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))
potencia = base ** expoente
print(potencia)
# %%
# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")
# %%
# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada
raio = float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# 12 - Imprimir Nome Completo em Minúsculas
nome_completo = input("Digite seu nome completo: ")
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)

# 13 - Remover Espaços em Branco de uma Frase
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

# 14 - Separar Dia, Mês e Ano de uma Data
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 15 - Concatenar Duas Strings
parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

# 16 - Operador and (E lógico)
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17 - # Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18 - Operador not (NÃO lógico)
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19 - Operador == (Igualdade)
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20 - Operador != (Diferença)
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)