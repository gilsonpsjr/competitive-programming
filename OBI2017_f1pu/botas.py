nrBotas = int(input())

totalPares = 0
botas = {}
for i in range(nrBotas) :
	tamBota = int(input())
	peBota = input()
	botas.keys()
	if ((tamBota in botas) and (botas[tamBota] != peBota)) :
		del botas[tamBota]
		totalPares += 1
	else :
		botas[tamBota] = peBota

print(totalPares)
