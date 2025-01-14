#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


# Não sei se a solução abaixo é considerada uma função pronta, mas caso seja, farei outra solução sem utilizá-la.

def inverte_string(string):
    return string[::-1]

print(inverte_string("teste")) # etset

def inverte_string(string):
    return "".join([string[i] for i in range(len(string)-1, -1, -1)])

print(inverte_string("teste")) # etset