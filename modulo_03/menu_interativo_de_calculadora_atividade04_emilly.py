'''
Explicação sobre atividade-desafio
'''
while True:
    # Exibindo o menu de opções
    print("\n====== CALCULADORA INTERATIVA ======")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Sair")
    
    opcao = input("Escolha uma opção (1/2/3): ")
    
    # Verificando a escolha do usuário
    if opcao == '3':
        print("Saindo do programa... Até logo!")
        break # Interrompe o loop while imediatamente
        
    elif opcao == '1' or opcao == '2':
        # Se a opção for válida, pede os números para o cálculo
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        
        if opcao == '1':
            resultado = valor1 + valor2
            print(f"Resultado da Soma: {resultado}")
        elif opcao == '2':
            resultado = valor1 - valor2
            print(f"Resultado da Subtração: {resultado}")
            
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")