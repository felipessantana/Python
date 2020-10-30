#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada. 

nome = input('Digite o seu nome: ')

#range(start,stop,step)

#for i in range(5,20,5):
#    print(i)

for i in range(1,len(nome)+1):
    print(nome[:i])

