input("Preparado? Então aperte enter")
input(".......")
input("Perai só mais um pouco")

idade = int(input("Qual a sua idade? "))
doenca = input ("Você tem doença infecciosa? ")

if idade >= 65:
    print ("Você tem atendimento prioritário, aguarde por favor ")
    if doenca.lower() == "Sim":
        print("Você tem uma doença infecciosa... sinto muito")
    else: print("Aguarde o atendimento..")


elif idade <= 64:
    print("Você não tem atendimento prioritário, porém aguarde mesmo assim ")
    if doenca.lower() == "Não":
        print("Que ótimo, você não tem uma doença infecciosa, fico feliz! ")


else: print("Desculpe, eu não entendi")
