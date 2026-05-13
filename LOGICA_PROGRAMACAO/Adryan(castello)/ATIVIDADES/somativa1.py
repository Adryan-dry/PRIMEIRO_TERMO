# #Questão 1
# Modelo = input ("Qual modelo do seu veículo?")
# Placa = input ("Qual é o número da placa?")
# print(f"Veículo {Modelo} de placa {Placa} registrado no sistema. Boa Viagem!") 

# #Questão 2 
# Capacidade = float (input("Quantos litros possui o tanque de combustível?"))
# Consumo = float(input("Qual o consumo médio de combustível por Kmh?"))
# Kmtotal = Capacidade*Consumo
# print(f"Seu caminhão pode percorrer {Kmtotal} Kms, com o tanque cheio")

# #Questão 3
# ValorEUA = float(input("Qual o frete em USD?"))
# ValoremBRL = ValorEUA* 5.00
# print(f"O valor em BRL é: {ValoremBRL}")

# #Questão 4
# rota1 = int(input("tempo da rota 1 (horas): "))
# rota2 = int(input("tempo da rota 2 (horas: "))
# rota3 = int(input("tempo da rota 3 (horas): "))
# Mediatotal = (rota1 + rota2 + rota3)/3
# print(f"O tempo aproximado de entrega é: {Mediatotal}")
# print("A média da sua rota é:",round(Mediatotal,2))

#Questão 5 
# print("Verificar o peso")
# tonelada = int(input("Digite o peso"))
# if tonelada <= 10 :
#     print("Carga leve")
# elif 10 < tonelada < 25:
#     print("Carga padrão")
# else:
#     print("ALERTA: Excesso de peso")

#Questão 6
# regiao = input("Digite o código da carga; N será região Norte ou S para regiao Sul")
# if regiao == "S":
#    print("Você selecionou: Região Sul")
# elif regiao == "N":
#    print("Você selecionou : Região Norte")
# else:
#    print("A sua carga é de região Internacional ")

# #Questão 7
# checklist = input  ("Seu checklist foi concluído? Sim/Não")
# motorista = input("Foi possível identificar o motorista? Sim/Não")
# if checklist == "Sim" and motorista == "Sim":
#     print("Saída liberada :)")
# else:
#     print("Saída negada!")

#Questão 8
# EntregasAgendadas = int(input("Qual a quantidade de entregas agendadas?"))
# EntregasAtrasadas = int(input("Qual a quantidade de entregas atrasadas?"))
# Indice = (EntregasAgendadas/EntregasAtrasadas)*100

# if Indice >= 10:
#     print("Necessário Otimizar rotas!")
# else:
#     print("Logística eficiente!")

#Questão 9 
# Pressao = int(input("Calibração do pneu de carga?"))

# if Pressao >110:
#     print("Pressão acima do padrão")
# elif 100 < Pressao < 110:
#     print("Pressão padrão")

# else: 
#     print("Pressão abaixo do padrão")

# #Questão 10
# print("O portão está fechando")
# for n in range(1, 6): 

