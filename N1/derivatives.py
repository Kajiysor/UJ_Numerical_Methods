import numpy as np
import matplotlib.pyplot as plt

def derive_a(x, h, fn):
	return ( fn(x+h) - fn(x) ) / h

def derive_b(x, h, fn):
	return ( fn(x+h) - fn(x-h) ) / (2*h)

def derive_c(x, h, fn):
	return ( (-fn(x+2*h)+8*fn(x+h)-8*fn(x-h)+fn(x-2*h)) / (12*h))

def abs_err(fn1, fn2, x):
	return np.abs( fn1(x) - fn2(x) )

def plot_err(x, h, fn, Dfn, filename):
	err_a = abs_err(lambda k: derive_a(k, h, fn), Dfn, x)
	err_b = abs_err(lambda k: derive_b(k, h, fn), Dfn, x)
	err_c = abs_err(lambda k: derive_c(k, h, fn), Dfn, x)
	fig = plt.figure()
	ax = fig.gca()
	line_a, = ax.plot(h, err_a)
	line_b, = ax.plot(h, err_b)
	line_c, = ax.plot(h, err_c)
	line_a.set_label('Metoda a')
	line_b.set_label('Metoda b')
	line_c.set_label('Metaoda c')
	ax.set_xscale('log')
	ax.set_yscale('log')
	ax.legend()
	plt.xlabel('log h')
	plt.ylabel('log E(x)')
	plt.grid()
	fig.savefig(filename)

x = np.float32(1)
h = np.float32(np.logspace(start=-8, stop=-1, num=1000, endpoint=False))
plot_err(x=x, h=h, fn=np.sin, Dfn=np.cos, filename='./float_32.png')

x = np.float64(1)
h = np.float64(np.logspace(start=-16, stop=-1, num=1000, endpoint=False))
plot_err(x=x, h=h, fn=np.sin, Dfn=np.cos, filename='./float_64.png')