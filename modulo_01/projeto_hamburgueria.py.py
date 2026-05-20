'''
CRUD

HAMBÚRGUERIA




'''


print ('\n === Sitema de Hamburgueria === \n')


print ("1. Cadastro")
print ("2. Cardapio")
print ("3. Solicitar o Pedido")
print ("4. pagamento")
print ("5. Acompanhar o pedido")
print ("6. Cancelar o Pedido")
print ("0. Sair")

while True:

    escolha_menu = input("\n Escolha uma opção")
    if escolha_menu == '1':

        print("Cadastro do Cliente")
        nome_cliente = input("Digite o nome do cliente")
        telefone_ciente = input("digite o telefone do cliente")

    elif escolha == "2":
        print("\n--- Cardápio ---")
        print("\nCardápio")

        print("\nHambúrgueres:")

        print("1 - X-Burger (Pão, hambúrguer bovino, queijo mussarela, alface e tomate)")
        print("2 - X-Salada (Pão, hambúrguer bovino, queijo, alface, tomate e maionese)")
        print("3 - X-Bacon (Pão, hambúrguer bovino, queijo, bacon crocante)")


    elif escolha_menu== '3':
        print("\n---Preços---")
        print("\npreços")

        print("\nHambúrgueres:")
        print("X-burguer- RS15$")
        print("Coca Cola em lata-RS7$")
    



    elif escolha_menu == '4':

        print("\n ----Opções de pagamento:---- \n")
        
        print("1. Cartão Crédito\Débito")
        print("2. Pix")
        print("3. Dinheiro")
         
    pergunta = input ("Digite qual sera a forma de pagamento: ")
    
    if pergunta == "1":
        print ("Pagamento sera efetuado no momento da entrega!")
    
    elif pergunta == "2":
        print ("Chave Pix: 428.983.245-24")
        print ("Aguardando Pagamento...")
    
    elif pergunta == "3":
        dinheiro_do_cliente = input 


    elif escolha == "5" :

        print("\n ---Entrega:")
        input("Confirmar sua entrega com sim ou não :")
        print('Seu pedido esta sendo preparado')
        print('seu pedido saiu para entregar')
        input('seu pedido foi entregue com sucesso')

    elif escolha_menu == "6":
        print("\n ---Desejar cancelar o pedido?")
        print("Sim")
        print("Não")

        resposta = input("escolha")

        if resposta == "Sim" :
            print ("Pedido cancelado")

        elif resposta == "Não":
            print("")

        else:
            print("\n opção inválida")
        

    elif escolha_menu == '0':

        print("saindo do sistema")
        break




    else:
        print("opção inválida")