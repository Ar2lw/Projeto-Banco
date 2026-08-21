print("Sistema Financeiro Tribank")
selecionado = 0
movimenta = []

while selecionado != 5:
    print("Bem Vindos ao Tribank!")
    print("Selecione uma das opções para continuar: ")
    print("1 - Adicionar receita liquida ao seu banco")
    print("2 - Adicionar o valor da fatura")
    print("3 - Ver o seu saldo final contando com a fatura e a receita")
    print("4 - Buscar gasto exato")
    print("5 - Sair do sistema")
    try:
        selecionado = int(input("Qual a função que gostaria? "))
    except:
        print("Não há essa função disponivel")
    if selecionado == 1:
             while True:
                try:
                    nome = input("Qual o nome da renda? ")
                    liquido = float(input("Qual o valor que deseja adicionar? "))
                    tipo = input("Qual o tipo de renda? (Receita/Despesa)")
                    categoria = input("Qual a categoria da renda?")
                    movimentacao = {
                        "Nome": nome,
                        "Liquido": liquido,
                        "Tipo": tipo,
                        "Categoria": categoria
                    }
                    if liquido>=0:
                        movimenta.append(movimentacao)
                        break
                    else:
                        print("Digito invalido")
                except:
                    print("Digite apenas o recomendado")
    elif selecionado == 2:
             while True:
                try:
                    nome2 = input("Qual a fonte da despesa? ")
                    liquido2 = float(input("Qual o valor da despesa? "))
                    tipo2 = input("Qual o tipo de gasto é? (Receita/Despesa)")
                    categoria2 = input("Qual a categoria do gasto?")
                    movimentacao2 = {
                        "Nome": nome2,
                        "Liquido": liquido2,
                        "Tipo": tipo2,
                        "Categoria": categoria2
                    }
                    if liquido2>=0:
                        movimenta.append(movimentacao2)
                        break
                    else:
                        print("Digito invalido")
                except:
                    print("Digite apenas o recomendado")
    elif selecionado == 3:
         totaldes = 0 
         totalsal = 0 
         for movi in movimenta:
              print(movi["Liquido"])
              if movi ["Tipo"] == "Receita":
                totalsal += movi["Liquido"]
                print(movi["Liquido"]) 
              elif movi ["Tipo"] == "Despesa":
               totaldes += movi["Liquido"]
         saldo = totalsal - totaldes
         print("Total de receita deste mês:", totalsal)
         print("Total de despesas este mês: ", totaldes)
         print("Saldo final da conta", saldo)
    elif selecionado == 4:
        Item = input("Qual item você procura? ")
        for movimentao in movimenta:
                    if Item in movimentacao ["Nome"]:
                        print("O seu produto está listado!!")
                        break
        else:
                        print("Produto não encontrado")
