#Funções são blocos de código reutilizáveis.

def saudacao (nome): 
    return f"Olá, {nome}!"
                 
mensagem=saudacao("Adryan")
print(mensagem)
                   
def age (idade):
    return f"Sua idade é, {idade}!"
mensagem=age("16")
print(mensagem )

def boas_vindas(nome,cargo):
    print(f"Olá, {nome}! Você é novo{cargo}.")
boas_vindas("Adryan","Desenvolvedor")
boas_vindas("Lucas", "Gerente")
boas_vindas("Bruno",'Professor')

#Conversões 
nome = input("Seu nome:")
idade = int(input("Sua idade:")) #Converte para texto inteiro
print(f"{nome} tem {idade} anos")


