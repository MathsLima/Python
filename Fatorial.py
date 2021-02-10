#Calculo de numero fatorial.

num = int(input("Digite o numero: "))

for cont in range(1, num+1):
	fat = fat * cont

print("O fatorial de", num, "é", fat)