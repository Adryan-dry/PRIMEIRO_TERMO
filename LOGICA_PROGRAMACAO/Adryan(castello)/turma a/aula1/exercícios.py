#Exercício 1 
#Criar um algoritmo que pergunte essas informações: seu nome, sua idade, curso e seu hobbie e apresente no final resultado
nome=input("Qual seu nome?")
idade =input("Qual sua idade?")
curso=input("Faz curso, se sim qual?")
hobbie=input("Qual hobbie voce faz?")
print("seu nome é:",nome)
print("sua idade é",idade )
print("seu curso é",curso)
print("seu hobbie é",hobbie)

#Exercício 2 
# Crie um algoritmo que pergunte o valor A e o valor B e apresente o resultado em um valor C
ValorA=int(input("digite o primeiro valor"))
ValorB=int(input("digite o segundo valor:"))
ValorC=ValorA+ValorB
print("o valor da soma é:",ValorC)
  
  #Exercício 3
  #Criar um algoritmo que calcule sua viagem por 3 pedágios, em cada pedágio será cobrado um valor e no fim apresente o total das passagens 

print("cálculo de pedágio") 
px1=int(input("qual é o valor do primeiro pedágio?"))
px2=int(input("qual é o valor do 2°p"))
px3=int(input("qual é o valor do pedágio px3"))
        
print("o valor da soma é:")

#Exercício 4
#Criar um algoritmo para calcular o IMC (Indice de Massa Corporal).
#Para esse cálculo precisamos do peso e altura. O cálculo deverá ser peso/altura *altura ou peso /altura^2 ou por altura **altura
print("cálculo IMC")
peso = float(input("qual seu peso?"))
altura = float(input("qual sua altura?"))
IMC=float(peso*altura)
print("o seu IMC é:",IMC) 
