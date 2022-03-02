#Neste desafio, você criará um contador de calorias que solicita ao usuário:
#    A data atual (em qualquer formato)
#    Calorias ingeridas no café da manhã
#    Calorias ingeridas no almoço
#    Calorias ingeridas no jantar
#    Calorias ingeridas no lanche


#geanclm in 20/11/2021 at 11:55h
dt = input('informe a data de hoje, por favor. Execmplo: 28/11/2021: ')
cc = int(input ('informe as Calorias ingeridas no café da manhã: '))
ca = int(input ('informe as Calorias ingeridas no almoço: '))
cj = int(input ('informe as Calorias ingeridas no jantar: '))
cl = int(input ('informe as Calorias ingeridas no lanche: '))
calorias = cc+ca+cj+cl
print ('na data '+(dt)+' você ingeriu o total de '+str(calorias)+' calorias')