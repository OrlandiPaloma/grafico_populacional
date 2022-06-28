#Crescimento população brasileira 1980-2016

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

#Legendas
eixox = 'Ano'
eixoy = 'Tamanho população x 100.000'
titulo = 'Crescimento população brasileira 1980-2016'

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color = "green") #grafico barra
plt.plot(x, y, color = "red") #grafico linha
plt.scatter(x, y, color = "purple") #grafico dispersão
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.show()