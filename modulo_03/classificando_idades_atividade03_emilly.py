'''
Explicação sobre atividade-03

'''
# Solicitando a idade
idade = int(input("Digite a idade da pessoa: "))

# Classificando de acordo com as regras de idade
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")