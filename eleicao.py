

total_cadeiras = 29
QE = 12684
aux = list()
coligacoes = list()
l = list()
def 
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
    	line =line.strip('\n')
    	l.append(line.split(';'))

for n in l:
	aux = n[2].split('-')
	if(len(aux) >1):
		coligacoes.append(aux[1])
	else:
		coligacoes.append(aux[0])

	n[3] = int(n[3])
	#print(n)
coligacoes = list(set(coligacoes))) # tira os nomes repetidos coligacoes reptidadas
for co in coligacoes: # filtrar e soma votos das coligacoes

