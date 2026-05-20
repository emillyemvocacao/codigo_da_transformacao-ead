'''
Explicação sobre atividade-02


'''
# Solicitando dois números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Comparando os valores
if n1 > n2:
    print(f"O maior número é o primeiro: {n1}")
elif n2 > n1:
    print(f"O maior número é o segundo: {n2}")
else:
    print("Ambos os números são iguais.")