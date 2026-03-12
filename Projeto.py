import math

#Projeto de calculos!

#Neste primeiro momento foi criado um menu de opções para o usuário.
print("Calculos!")
print("1 - Cálculo de Média")
print("2 - Cálculo Fatorial")
print("3 - Conversão de Temperatura")
print("4 - Conversão de unidades de medida")
print("5 - Cálculo da área de uma figura geométrica")
print("6 - Cálculo de porcentagem")

#Primeira entrada de dados para o usuário escolher alguma dessas opções.
opcao = (input("Escolha uma opção:"))

#Estrutura de decisão da escolha, se(if) for opção 1 ele roda a opção 1
if opcao == "1":

#Entrada de valores para média.
    valorUm = float(input("Digite a Nota 1:"))
    valorDois = float(input("Digite a Nota 2:"))
    valorTres = float(input("Digite a Nota 3:"))
    valorQuatro = float(input("Digite a Nota 4:"))

#Processamento dos valores acima, nessa parte é realizada a soma e a média dos valores.
    soma = (valorUm + valorDois + valorTres + valorQuatro) / 4

#Saido do processamento na tela para o usuário.
    print("A média desse calculo é: ", soma)

# Se o usuario escolher a opção 2 irá ser executado o cálculo fatorial.
elif opcao == "2":

#Entrada de valores para o  calculo fatorial
    fator = int(input("Digite um valor para fazer o calculo Fatorial:"))

    #calculo fatorial utilizando a biblioteca "math".
    calculo = math.factorial(fator)

    print("O valor Fatorial desse número é: ", calculo)

#Se o usuario escolher a opção 3 irá ser executado a conversão de temperatura.
elif opcao == "3":

#
    print("Esolha qual conversão você deseja fazer: ")
    print(" 1 - Fahrenheit")
    print(" 2 - Celsius")

    conversao = (input("Escolha:"))

    if  conversao == "1":
       celsius = float(input("Escreve a temperatura Celsius para a conversão para Fahrenheit: "))
       fahrenheit = (celsius * 1.8) + 32
       print("A conversão é: ", fahrenheit)

    elif conversao == "2":
        far = float(input("Escreve a temperatura Fahrenheit para a conversão para Celsius:"))
        cel = (far - 32) * 5 / 9
        print("A conversão é: ", cel, "graus")

elif opcao == "4":

    print("Para qual unidade de medida deseja converter: ")
    print(" 1 - Quilometros para centímetros.")
    print(" 2 - Metros para centímetros.")
    print(" 3 - Horas para minutos.")

    converte = (input("Escolha: "))

    if converte == "1": 
        KM = float(input("Digite o KM desejado para conversão: "))
        CM = KM * 100000
        print("A conversão de KM para CM foi de: ", CM, "CM")

    elif converte == "2":
        M = float(input("Digite os Metros para conversão: "))
        C = M * 1000
        print("A conversão de Metros para Centimetros é: ", C, "CM")

    elif converte == "3":
        H = float(input("Digite as Horas para fazer a conversão: "))
        min = H * 60
        print("A conversão de Horas para Minutos é: ", min, "Minutos")

elif opcao == "5":
    print("Calcular áreas da figuras:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Círculo")

    areaT = input("Escolha uma opção: ")

    if areaT == "1":
        lateral = float(input("Diga o valor do Perimetro: "))
        area = lateral* lateral
        print("A área desse QUADRADO é: ", area, "cm")

    elif areaT == "2":
        baseDois = float(input("Digite o valor da base: "))
        alturaDois = float(input("Digite o valor da altura: "))
        areaDois = baseDois * alturaDois

        print("A área desse Retângulo é: ", areaDois)

    elif areaT == "3":
         baseTres = float(input("Digite o valor da base: "))
         alturaTres = float(input("Digite o valor da altura: "))
         areaTres = (baseTres * alturaTres) / 2

         print("A área desse Triângulo é: ", areaTres)

    elif areaT == "4":
        raio = float(input("Digite o Raio desse círculo: "))
        areaQuatro = math.pi * raio **2

        print("A área desse Círculo é: ", areaQuatro)

elif opcao == "6":
    print("Informe um valor para a Porcentagem: ")
    valorP = float(input("Digite o valor: "))
    porcentagem = float(input("Digite a Porcentagem que você quer tirar do número: "))

    porc = (valorP * porcentagem) / 100
    final = valorP - porc

    print("O valor da Porcentagem retirada de %", porcentagem, "é: ", porc, "sobrando o valor de: ", final)

else:
    print("Opcão Inválida!")
    