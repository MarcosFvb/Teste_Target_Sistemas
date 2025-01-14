#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

def soma(indice, soma, k):
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma


print(soma(13, 0, 0)) # 91