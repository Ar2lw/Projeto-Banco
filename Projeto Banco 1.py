print("Sistema Financeiro")
opcao = 0
nomedosaldo = []
valordosaldo = []
fontedadespesa = []
valordadespesa = []
while opcao != 4:
    print("Escolha uma das opções:")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Sair")
    try:
        opcao = int(input())
    except:
        print("Erro! O Sistema aceita apenas numeros")
    if opcao == 1:
        while True:
            try:
                nome = (input("Adicione a fonte do saldo: "))
                valor = (float(input("Adicione o valor do saldo: ")))
                if valor>=0:
                        nomedosaldo.append(nome)
                        valordosaldo.append(valor)
                        break
                else:
                    print("o valor deve ser positivo")
            except:
                 print("Não aceitamos letras")
    elif opcao == 2:
        while True:
            try:
                nome2 = (input("Adicione a fonte da despesa: "))
                valor2 = (float(input("Adicione o valor da despesa: ")))
                if valor2>=0:
                    fontedadespesa.append(nome2)
                    valordadespesa.append(valor2)
                    break
                else:
                    print("O valor deve ser positivo, pois no final já vai ser subtraido")
            except:    
                print("Não aceitamos letras")
    elif opcao == 3:
        print("Saldo atual da conta:")
        for i in range(len(nomedosaldo)):
            print(f"{nomedosaldo[i]} - R$ {valordosaldo[i]}")
        print("Despesas atuais da conta:")
        for i in range(len(fontedadespesa)):
            print(f"{fontedadespesa[i]} - R$ {valordadespesa[i]}")
        print("Saldo da conta: ")
        final = sum(valordosaldo) - sum(valordadespesa)
        print("Saldo", final)