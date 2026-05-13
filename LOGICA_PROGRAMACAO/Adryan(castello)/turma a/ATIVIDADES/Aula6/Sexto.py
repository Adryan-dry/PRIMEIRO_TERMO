#                                        CORREÇÃO SOMATIVA 1
#Q1
# print("Registro de veículo")
# modelo = input("Qual é o modelo do veículo?...")
# placa = input ("Qual é a placa do veículo?...")
# print (f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem:)")

#Q2
# print("Cálculo de Autonomia")
# tanque = float(input("Qual é a capacidade de seu tanque em litros?"))
# consumo =float(input("Digite o consumo médio por caminhão em Km/L"))
# total = tanque/consumo
# print(f"Seu caminhão pode percorrer {total:.2f} em Km/L")
# print("Seu caminhão pode percorrer", round(total,2), "em Km/L")

#Q3
# print("Conversor de Moeda (Frete Internacional)")
# valor_reais = float(input("Qual é o valor em Reais que será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa em Dólar em Reais?..."))
# total = valor_reais / taxa_dolar 
# print(f"O valor total convertido é... {total:.2f}")

#Q4
# print("Média de Entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3 /3) 
# print(f"A média{media:.2f} de tempo das entregas")

#Q5
# print("Monitor de Carga")
# peso = float(input("Qual é o peso atual do seu caminhão?..."))

# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("Carga padrão")
# else:
#     print("ALERTA: Excesso de peso!!!!") 

#Q6
# print("Classificador de Destino")
# print("Regiões = N- Região Norte , S- Região Sul , Qualquer Outra - Internacional")
# regiao = input("Inserir o código da Região: ").lower()
# if regiao == "N".upper () or regiao == "n".lower ():
#     print("Região Norte")
# elif regiao == "S": 
#     print("Regiao Sul")
# else:
#     print("Regiao Internacional")

#Q7 
# print("Liberação de Saída")
# checklist = input("O checklist foi concluído?[Concluído ou Não Concluído]")
# motorista = input("O motorista foi identificado?[Sim ou Não]")
# if checklist == "Concluído" and motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else: 
#     print("Veículo NÃO autorizado a iniciar a rota. Verificar checklist e identificação do motorista.")


#Q8
# print("Cálculo de Atrasos")
# total_entregas = int(input("Total Entregas Agendadas:..."))
# total_atrasos = int(input("Total Entregas em Atrasos:..."))
# if total_atrasos > total_entregas * 0.1:
#     print("Necessário otimizar rotas")
# else :
#     print("Logística Eficiente")
    
#Q9
# print("Validação de Calibragem ")
# pressao = float (input("Digite a pressão do pneu em PSI..."))
# if 100 <= pressao <= 110:
#     print ("Dentro do padrão")
# elif pressao <100:
    
#Q10
# print("Contagem de Embarque")
# import time
# for contagem in range (40,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("Portão trancado")

#Q11
# print("Somatório de Frete (Acumulador)")
# total = 0
# while True:
#     valor = float(input("Valor do Frete:"))
#     if valor == 0:
#         total += valor
#         print(f"Total acumulado{total} do Frete")

# print("Somatório do Frete (Acumulador) - Versão 2")
# faturamento_total = 0 
# valor_frete = -1
# while valor_frete != 0:
#     valor_frete = float (input("Valor de Frete ou 0 para encerrar"))
#     faturamento_total += valor_frete 
#     print(f"Faturamento acumulado: R$ {faturamento_total}")
# print("Cálculo executado com sucesso")

# print("Somatório de Frete (Acumulador) - Versão 3")
# b=0 
# while True:
#     t= int(input("Valor Frete..."))
#     c= input("Quer continuar s/n")
#     b += t 
#     if c == "s":
#         continue
#     else:
#         break
# print(f"Faturamento total {b} acumulado")

#Q12
# print("Monitoramento de Frota")
# maior_km = 0 
# for frota in range (1, 6):
#     km = float (input(f"Digite a quilometragem do veículo{frota}:"))
#     if km > maior_km:
#         maior_km = km
# print(f"A maior quilometragem registrada é: {maior_km} km.")

#Q13
# print("Sistema de Rastreio")
# codigo_correto = "track99"
# tentativas = 0 
# max_tentativas = 3
# while  tentativas < max_tentativas:
#     codigo_input =  input("Códgio de acesso do Rastreador:")
#     if codigo_input == codigo_correto:
#         print("Acesso Permitido:). Iniciando Rastreamento")
#         break
#     else: 
#         tentativas += 1 
#         print("Acesso Negado:(")
#         if tentativas < max_tentativas:
#             print(f"Tentativas restantes:{max_tentativas}")
# else:
#     print("Rastreamento Bloqueado")