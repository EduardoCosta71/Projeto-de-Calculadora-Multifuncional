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


#Calculo fatorial, o usuário irá informar um valor para o calculo fatorial e o programa irá mostrar o resultado. ------------------------
elif opcao == "2":

#Entrada de valores para o  calculo fatorial
    fatorial = int(input("Digite um valor para fazer o calculo Fatorial:"))

    #calculo fatorial utilizando a biblioteca "math".
    calculo = math.factorial(fatorial)

    print("O valor Fatorial desse número é: ", calculo)

#Calculo de conversão de temperatura, o usuário irá escolher qual conversão deseja fazer,
#  depois irá informar o valor para a conversão e o programa irá mostrar o resultado. ------------------------
elif opcao == "3":

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


#Calculo de conversão de unidades de medida, o usuário irá escolher qual unidade de medida deseja converter,
#depois irá informar o valor para a conversão e o programa irá mostrar o resultado. ------------------------
elif opcao == "4":

    print("Para qual unidade de medida deseja converter: ")
    print(" 1 - Quilometros para centímetros.")
    print(" 2 - Metros para centímetros.")
    print(" 3 - Horas para minutos.")

    ConversoesCalculo = (input("Escolha: "))
#Entrada de dados para o usuário escolher qual unidade de medida deseja converter,
#  cada opção tem um calculo diferente, o programa irá solicitar o valor para a conversão de cada unidade de medida.
    if ConversoesCalculo == "1": 
        CalculoKM = float(input("Digite o KM desejado para conversão para centímetros: "))
        ConversaoCM = CalculoKM * 1000
        print("A conversão de KM para CM foi de: ", ConversaoCM, "CM")

    elif ConversoesCalculo == "2":
        CalculoMetros = float(input("Digite os Metros para conversão para centímetros: "))
        CM = CalculoMetros * 100
        print("A conversão de Metros para Centimetros é: ", CM, "CM")

    elif ConversoesCalculo == "3":
        CalculoHora = float(input("Digite as Horas para fazer a conversão: "))
        ConversaoMin = CalculoHora * 60
        print("A conversão de Horas para Minutos é: ", ConversaoMin, "Minutos")


#Cálculo de área de figuras geométricas, o usuário irá escolher qual figura deseja calcular a área,
#depois irá informar os valores necessários para o cálculo da área e o programa irá mostrar o resultado. ------------------------
elif opcao == "5":
    print("Calcular áreas da figuras:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Círculo")

#Entrada de dados para o usuário escolher qual figura deseja calcular a área.
#Cada figura tem um calculo diferente, o programa irá solicitar os valores necessários para o cálculo da área de cada figura.
    areaFiguras = input("Escolha uma opção: ")

    if areaFiguras == "1":
        lateral = float(input("Diga o valor do Perimetro do QUADRADO: "))
        areaUm = lateral* lateral
        print("A área desse QUADRADO é: ", areaUm, "cm")

    elif areaFiguras == "2":
        baseDois = float(input("Digite o valor da base do RETÂNGULO: "))
        alturaDois = float(input("Digite o valor da altura do RETÂNGULO: "))
        areaDois = baseDois * alturaDois

        print("A área desse Retângulo é: ", areaDois)

    elif areaFiguras == "3":
         baseTres = float(input("Digite o valor da base do TRIÂNGULO: "))
         alturaTres = float(input("Digite o valor da altura do TRIÂNGULO: "))
         areaTres = (baseTres * alturaTres) / 2

         print("A área desse Triângulo é: ", areaTres)

    elif areaFiguras == "4":
        raio = float(input("Digite o Raio desse círculo: "))
        areaQuatro = math.pi * raio **2

        print("A área desse Círculo é: ", areaQuatro)


#Calculo de Porcentagem, o usuário irá informar um valor e a porcentagem que
#deseja retirar desse valor, o programa irá mostrar o valor da porcentagem retirada e o valor final. ------------------------
elif opcao == "6":
    print("Informe um valor para a Porcentagem: ")
    valorCalculo = float(input("Digite o valor: "))
    porcentagem = float(input("Digite a Porcentagem que você quer tirar do número: "))

    porc = (valorCalculo * porcentagem) / 100
    calculo = valorCalculo - porc

    print("O valor da Porcentagem retirada de %", porcentagem, "é: ", porc, "sobrando o valor de: ", calculo)

#Por fim, caso o usuário digite uma opção inválida, o programa irá mostrar a mensagem "Opção Inválida!".
else:
    print("Opcão Inválida!")
    
