#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def faturamento_mensal(faturamento=faturamento):
    total = sum(faturamento.values())
    percentual = {estado: (faturamento[estado] / total) * 100 for estado in faturamento}
    return percentual

print(faturamento_mensal()) # {'SP': 37.61, 'RJ': 20.36, 'MG': 16.23, 'ES': 15.09, 'Outros': 10.71}