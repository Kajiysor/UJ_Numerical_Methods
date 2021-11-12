import math

pi = 3.14159265358979323846
N = 20

aritmCounter = 0
mathFuncCounter = 0
operatorCounter = 0.5

def x_equation(n): 
	global aritmCounter

	aritmCounter += 3
	return (pi / N) * (n + 0.5)


def t_equation(k, x):
    global aritmCounter
    global mathFuncCounter

    aritmCounter += 2
    mathFuncCounter += 2*30

    return math.cos(k * math.acos(x))

def t_equation_recur(k, x):
	global aritmCounter

	aritmCounter += 5

	if k == 0:
		return 1.0
	elif k == 1:
		return x
	else:
		return 2.0 * x * t_equation_recur(k-1, x) - t_equation_recur(k-2, x)

def sum_equation(N = 20): 
	global aritmCounter
	global mathFuncCounter
	global operatorCounter
	
	I_k = []
	sum = 0.0 

	for k in range(N):
		for i in range(N):
			aritmCounter += 3
			mathFuncCounter += 90
			operatorCounter += 1
			temp = math.cos(x_equation(i))
			sum = sum + t_equation_recur(k, math.cos(x_equation(i))) / (1.0 + 25.0 * temp * temp)
		
		I_k.append(sum)
		sum = 0.0

	for i in range(N):
		print "I[{}] = {:.11}".format(i, I_k[i])
   
sum_equation()

print "\nLiczba obliczen: ", aritmCounter
print "Liczba funkcji: ", mathFuncCounter
print "Liczna obliczen w sumie: ", aritmCounter + mathFuncCounter + operatorCounter