number = 600851475143#int(input("Input the number you want to factorize:"))

pFactors = []

def factorize(num):
	for i in range(2,num+1):
		if num%i == 0:
			pFactors.append(i)
			factorize(int(num/i))
			return

factorize(number)

# print("the prime factors of {}".format(number), "are {}".format(pFactors))

print("largest prime factors of {}".format(number), "is {}".format(pFactors[-1]))