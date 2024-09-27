

'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

numero = int(input("Informe um numero: "))
sequencia = [0, 1]
while sequencia[-1] < numero:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        if  sequencia[-1] == numero:
            print("O numero pertence a sequencia")


    