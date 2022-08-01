cont = 1
soma = 0
while cont <= 5:
    idade = int(input(f'Digite a {cont} idade:'))
    soma = soma + idade
    cont += 1
media = soma / (cont -1)

if (media < 18):
    print('População jovem')
elif media <= 60:
    print('População adulta')
elif media > 61:
    print('População idosa')        