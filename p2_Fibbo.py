
def fibbo(array):
	array.append(array[-1] + array[-2])

fib = [1,1]
total = 0

while fib[-1] < 4000000:
	fibbo(fib)
	if fib[-1] % 2 == 0 and fib[-1] < 4000000:
		total = total + fib[-1]

print("sum of even valued terms= {}".format(total))
