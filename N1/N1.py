import numpy as np
import matplotlib.pyplot as plt

def derivative_1(x, h, f):
	return (f(x+h) - f(x)) / h

def derivative_2(x, h, f):
	return (f(x+h) - f(x-h)) / (2*h)

def derivative_3(x, h, f):
	return ((-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)) / (12*h))

def absolute_error(f1, f2, x):
	return np.abs(f1(x) + f2(x))

def plot_error(x, h, f, D_f):
	error_1 = absolute_error(lambda k: derivative_1(k, h, f), D_f, x)
	error_2 = absolute_error(lambda k: derivative_2(k, h, f), D_f, x)
	error_3 = absolute_error(lambda k: derivative_3(k, h, f), D_f, x)
	plt.title("Błąd metod dyskretyzacji")
	plt.xscale('log')
	plt.yscale('log')
	plt.plot(h, error_1, label = "Metoda 1")
	plt.plot(h, error_2, label = "Metoda 2")
	plt.plot(h, error_3, label = "Metoda 3")
	plt.grid()
	plt.xlabel('log h')
	plt.ylabel(f"log E(x) dla {x = }")
	plt.legend()
	plt.savefig("wykres_N1.pdf")

def main():
	x = np.float64(1)
	h = np.float64(np.logspace(-16, 0, num=1000, endpoint=False))
	plot_error(x, h, f = np.cos,  D_f = np.sin)

if __name__ == "__main__":
	main()