# Criar um algoritmo para que:

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída será sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NOVO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Levantamento de requisitos 
#Primeira coisa: Dê boas vindas ao cliente: #Olá, seja bem-vindo ao SmartShopping Parking, este é nosso sistema de gerenciamento de cancelas do shopping!
#Quando o veículo parar o sensor de presença detecta o veículo juntamente com uma câmera específica de presença.
#Se encontrar tag levantar a cancela automaticamente
#Pergunte, se o cliente tem a tag. Se não tiver pergunte as informaçoes do veículo.
# #print("O senhor(a) não possui a tag, para usufruir do nosso estacionamento utilize o ticket. E digite as informações do veículo")
# #print("Clique no botão situado no totem e retire seu ticket")
# #print("Acesso liberado, guarde este ticket com você, e, ao sair do shopping, encontre um totem de pagamento do ticket, pague o ticket e apresente na cancela de saída do estacionamento para sair do estacionamento!:)")

#Se não encontrar nenhuma tag, exibir uma mensagem dizendo: Se não possui tag 
#Emitir uma fala: Pressione o botão para retirar seu ticket ou entre com sua tag.
#Segundo:
#- Clique no botão e retire seu ticket                                ^    ^    ^
#                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ À TERMINAR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ANTIGO QUE FOI ENTREGUE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Passo 1:                                                               
# -Quando o veículo chegar o sensor de presença no solo ou em forma de câmera, deve ser ativado e emitir um som: Bem-Vindo ao SmartParking.
# -Um outro sensor automaticamente lê as taggy do vidro.
#Passo 2:
# -Caso o motorista não tenha a taggy, ele precisa pressionar o botão do Totem.
# -Ao pressionar, diga: Retire seu ticket, automaticamente a cancela levanta para o veículo passar.
#Perguntar as informações sobre o veículo ou forma de acesso
# Pressionar o botão para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário
#
#Passo 2:
# Verificar tempo de permanência 
# Valor a ser cobrado
#  
#Passo 3:
# Saída como será?
#Se for taggy gerar na fatura da taggy 
#Pagar ticket
#Devolver ticket na saída 
#Passo 4
#Gerar relatorio de entradas e saidas
#Tratamento de Erros
#Revisão do código

# placa = input ("Digite a placa do carro:")
# tag = input("Você possui TAG?")

# if tag == "SIM":
#     print("Acesso liberado, Ótimo passeio!")
# elif tag == "Não":
#     print("Aperte o botão situado no totem")

# else:
#     print("Acione o interfone para obter ajuda!!")