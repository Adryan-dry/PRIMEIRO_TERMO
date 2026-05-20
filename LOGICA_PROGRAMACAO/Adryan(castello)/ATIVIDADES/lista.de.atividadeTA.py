#LISTA DE ATIVIDADES 2 - TA
#ERRADO
# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

# CORRIGIDO:
# 1.O Problema da idade:
# idade = int(input("Digite sua idade"))
# if idade >= 18:
#     print("Você é maior de idade ")

# else: 
#     print("Você é menor de idade")


# # MELHORADO:
# idade = int(input("Qual sua idade?"))
# if idade < 18 :
#     print("Peça ajuda para alguém de maior idade:)")


# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")    


# CORRIGIDO:
# nome = "Mariana"
# print("Seja bem-vinda" , nome)

# #MELHORADO:
# nome = input("Digite seu nome:")
# print(f"Seja bem-vinda, {nome}!")


# 3. Falta de Espaço
#ERRADO:
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#CORRIGIDO:

# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#      print("O número é menor ou igual a cinco.")

#MELHORADO
# numero = int(input("Digite o valor:"))
# if numero > 10:
#     print("O número é maior que dez")
# else: 
#      print("O número é menor ou igual a dez")
# 4. Esquecimento Fatal
# ERRADO:
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")
 
#  #CORRIGIDO
# usuario = "aluno123"
# if usuario == "aluno123":
#   print("Login realizado com sucesso.")

#MELHORADO
# usuario = input("Digite o login:") 
# if usuario =="aluno123":
#    print("Parabéns, seu login foi realizado") 
# else:
#      print("Não foi possível realizar o login!")

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#CORRIGIDO
# clima = "ensolarado"
# if clima == "chuvoso":
#   print("Leve um guarda-chuva!")

# MELHORADO
# input("Qual o clima de hoje?")



# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")


# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
#ERRADO

# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# CORRIGIDO
# nota = 9.5
# if nota >= 7:
#    print("Aprovado")
# elif nota >= 9:
#    print(Excelente)