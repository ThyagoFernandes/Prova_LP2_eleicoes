#Aluno: Thyago Henrique Fernandes Bezerra de Mendonça
from operator import itemgetter
import csv

total_cadeiras = 29
QE = 12684
aux = list()
#variaveis utilizadas
coligacoes_votos = dict()
coligacoes_qp = dict()
coligacoes_vagas_residuais = dict()
lista_de_eleitos = list()
lista_de_candidatos = list()
lista_de_eleitos_da_col = list()
# ler o arquivo separa em uma lista no formato [numero, nome, [partido, coligacao], quantidadee de votos]
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
    	line =line.strip('\n')
    	line = line.split(';')
    	if(len(line[2].split('-'))<2):
    		line[2] = [line[2],line[2]]
    	else:	
    		line[2] = line[2].split('-')
    	line[3] = int(line[3])
    	lista_de_candidatos.append(line)
#contagem de votos por coligacoes
for n in lista_de_candidatos:
	if(n[2][0] != n[2][1]):
		if(coligacoes_votos.get(n[2][1]) is not None):
			coligacoes_votos[n[2][1]] += int(n[3])
		else:
			coligacoes_votos[n[2][1]] = int(n[3])

	else:
		if(coligacoes_votos.get(n[2][0]) is not None):
			coligacoes_votos[n[2][0]] += int(n[3])
		else:
			coligacoes_votos[n[2][0]] = int(n[3])
#calculo do qp e dos eleitos sem vagas residuais
for chave in coligacoes_votos.keys():
    coligacoes_qp[chave] = coligacoes_votos[chave] // QE
    if(coligacoes_qp[chave] > 0):
    	lista_de_candidatos_da_col = sorted([elem for elem in lista_de_candidatos if(elem[2][1] == chave)],key = itemgetter(3), reverse = True)
    	lista_de_eleitos.extend(lista_de_candidatos_da_col[0:coligacoes_qp[chave]])


vagas_restantes = total_cadeiras - len(lista_de_eleitos)

print(sum(coligacoes_qp.values()),len(lista_de_eleitos))
listares = list()
#a parti do calculo de vagas residuais e decidido quem eh os outros candidatos eleitos
while vagas_restantes >0:
	coligacao_vencedora = ''
	media= 0
	media_nova = 0
	for chave in coligacoes_votos.keys():
		media_nova = coligacoes_votos[chave]/(coligacoes_qp[chave] +1)
		print(coligacao_vencedora, media, coligacoes_votos[chave] ,chave, media_nova)
		if( media_nova> media):
			media = media_nova
			coligacao_vencedora = chave
	
	coligacoes_qp[coligacao_vencedora] += 1
	lista_de_candidatos_da_col = sorted([elem for elem in lista_de_candidatos if(elem[2][1] == coligacao_vencedora)],key = itemgetter(3), reverse = True)
	print(' ')
	print(coligacoes_qp)
	print(' ', lista_de_candidatos_da_col[coligacoes_qp[coligacao_vencedora]])
	lista_de_eleitos.append(lista_de_candidatos_da_col[coligacoes_qp[coligacao_vencedora]-1])
	
	vagas_restantes -= 1
file = open("eleicao.tsv","w")
lista_de_eleitos = sorted(lista_de_eleitos,key = itemgetter(3), reverse= True)
#coloca no arquivo de saida tsv
for n in lista_de_eleitos:
	n[3] = str(n[3])
	if(n[2][0] != n[2][1]):
		file.write(n[0]+"\t" +n[1]+"\t"+n[2][0]+n[2][1]+"\t"+n[3])
	else:
		file.write(n[0]+"\t" +n[1]+"\t"+n[2][0]+"\t"+n[3])
	file.write('\n')
file.close()



