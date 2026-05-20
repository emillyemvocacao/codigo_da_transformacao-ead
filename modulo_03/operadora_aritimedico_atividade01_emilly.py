'''
Explicação sobre atividade-01
'''
# Solicitando os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando os cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Tratamento para evitar divisão por zero
if num2 != 0:
    divisao = num1 / num2
    resto = num1 % num2
else:
    divisao = "Não é possível dividir por zero"
    resto = "Não é possível calcular o resto de divisão por zero"

# Exibindo os resultados
print(f"\n--- Resultados ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão: {resto}")