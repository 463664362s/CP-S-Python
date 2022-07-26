#Validação valor e pratos
while (True):
    pratos = int(input("Entre com o numero de pratos principais: "))
    valor_total = float(input("Entre com o valor do pedido: "))
    if valor_total <= 0:
        print("Valor inválido. Digite novamente.")
    elif pratos <= 0:
        print("Número de pratos principais inválido. Digite novamente.")
    else:
        break

#Atribuição das variaveis de desconto
desconto_500 = 0
desconto_pratos = 0
desconto_borala10 = 0
desconto_borala05 = 0
desconto_vez = 0 

#Desconto da conta maior que $500
if  valor_total > 500:
    desconto_500 = 6/100
    
#Desconto dos pratos
if  pratos > 3:
    desconto_pratos = 4/100

#Validação e desconto do cupom de desconto 
while (True): 
    cupom = input("Você tem cupom valido? 'S' para sim e 'N' para não: ")
    if (cupom == "S") or (cupom == "s"): 
        cupom = input("Nome do cupom: ")
        if (cupom == "BORALA10"):
            desconto_borala10 = 10/100
            break
        elif (cupom == "BORALA05"):
            desconto_borala05 = 5/100
            break 
        else:
             print("Cupom inválido.")
    elif (cupom == "N") or (cupom == "n"):
        break
    else:
        print("Resposta inválida.")

#Validação e desconto da primeira visita
while (True): 
    vez = input("É a primeira vez que visita o restaurante? 'S' para sim e 'N' para não: ")
    if (vez == "S") or (vez == "s"):
        desconto_vez = 5/100
        break
    elif (vez == "N") or (vez == "n"):
        break
    else:
        print("Resposta invalida")

#Validação para rachar conta
desconto_total = valor_total - valor_total*(desconto_500 + desconto_borala05 + desconto_borala10 + desconto_pratos + desconto_vez)

while (True): 
    pessoa = input("Deseja rachar a conta? 'S' para sim e 'N' para não: ")
    if (pessoa == "S") or (pessoa == "s"):
        numeropessoa = int(input("Coloque o número de pessoas: "))
        break
    elif (pessoa == "N") or (pessoa == "n"):
        numeropessoa = 1
        break
    else:
        print("Resposta Inválida.")

#Saída de dados
print("------------------------------------------------------")
print("Valor total da nota fiscal:", valor_total)
print("Valor total da nota com desconto:", desconto_total)
print()
print("Número de pessoas:", numeropessoa)
print("Total por pessoa:", desconto_total/numeropessoa)
print("------------------------------------------------------")