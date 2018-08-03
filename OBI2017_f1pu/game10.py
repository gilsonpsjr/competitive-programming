nrPosicoes = int(input())
posicaoDisco = int(input())
posicaoAviao = int(input())

if (posicaoAviao > posicaoDisco) :
	totalApertos = nrPosicoes - posicaoAviao + posicaoDisco
else :
	totalApertos = posicaoDisco - posicaoAviao

print(totalApertos)
