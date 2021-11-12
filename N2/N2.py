import numpy as np
import matplotlib.pyplot as plt

def find_l(a, d, N):
    l = []
    l.clear()
    for i in range(N-1):
        lt = a[i]/d[i]
        l.append(lt)
    l = np.array(l)
    return l

def find_d(a, b, c, N):
    d = []
    d.clear()
    d.append(b[0])
    for i in range(1, N):
        dt = b[i] - (a[i-1] * c[i-1]) / d[i-1]
        d.append(dt)
    d = np.array(d)
    return d

def find_z(l, f, N):
    z = []
    z.clear()
    z.append(f[0])
    for i in range(1, N):
        zt = f[i] - l[i-1] * z[i-1]
        z.append(zt)
    z = np.array(z)
    return z

def find_y(z, c, d, N):
    y = np.empty(N)
    y[N-1] = z[N-1] / d[N-1]
    for i in range(N-2, -1, -1):
        y[i] = (z[i] - c[i] * y[i+1]) / d[i]
    return y


def main():
    N = 100
    h = 1.0/N

    ### Vector f
    f = np.zeros(N)
    f[N-1] = 1
    print(f)
    ###

    ### Matrix A
    a = np.full(N-1, 1/(h*h))
    a[N-2] = 0
    print(f"{a = }")

    b = np.full(N, -(2/(h*h)))
    b[0] = 1
    b[N-1] = 1
    print(f"{b = }")

    c = np.full(N-1, 1/(h*h))
    c[0] = 0
    print(f"{c = }")
    ###

    ### Matrix L
    l = find_l(a, b, N)
    print(f"{l = }")
    ###
    
    ### Matrix U
    d = find_d(a, b, c, N)
    print(f"{d = }")
    ###

    ### Vector z
    z = find_z(l, f, N)
    print(f"{z = }")
    ###

    ### Vector y
    y = find_y(z, c, d, N)
    print(f"Szukany wektor: { y = }")
    ###

    plt.title("Wykres wartości wektora y")
    size = np.arange(0, N, 1)
    plt.plot(size, y, label = "$y_n$", color = "blue", linewidth = 2.25)
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.legend(loc = "best")
    plt.savefig("wykres_N2.pdf")

if __name__ == '__main__':
    main()