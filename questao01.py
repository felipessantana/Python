#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. 

texto1 = 'Brasil Hexa 2006'
texto2 = 'Brasil Hexa 2006!'

print(len(texto1), 'caracteres')
print(len(texto2), 'caracteres')

if len(texto1) != len(texto2):
    print('Os tamanho são diferentes')

if texto1 != texto1:
    print('os conteudos são diferentes!')
else:
    print('os conteudos são iguais!')