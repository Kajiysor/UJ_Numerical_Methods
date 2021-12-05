import numpy as np
import matplotlib.pyplot as plt


def main():
    N = 1000
    h = 0.01

    # Wyznaczone z drugiego rownania
    a = h*h - 2

    # Wykorzystujemy faktoryzacje LU => {Ay = x; A = LU; LUy = x; Lz = x; Uy = z}

    # Wektor u wyznaczony z warunku A = LU
    u = np.zeros(N+1, dtype=np.float64)
    u[0] = 1
    u[1] = a
    for i in range(2, N):
        u[i] = (a*u[i-1] - 1)/u[i-1]
    u[N] = -2 - (1/u[N-1])

    # Wektor l wyznaczony z warunku A = LU
    l = np.zeros(N, dtype=np.float64)
    l[0] = 1
    for i in range(1, N-1):
        l[i] = a - u[i+1]
    l[N-1] = -2 - u[N]

    # Wektor z wyznaczony z warunku Lz = x
    z = np.zeros(N+1, dtype=np.float64)
    z[0] = 1
    for i in range(1, N):
        z[i] = -1 * l[i-1] * z[i-1]
    z[N] = -1 - (l[N-1] * z[N-1])

    # Wektor y wyznaczony z warunku Uy = z
    y = np.zeros(N+1, dtype=np.float64)
    y[0] = z[0]/u[0]
    y[N] = z[N]/u[N]
    for i in range(N-1, 0, -1):
        y[i] = (z[i] - y[i+1])/u[i]

    plt.title("Wykres wartości wektora y")
    size = np.arange(0, (N+1)*h, h)
    plt.plot(size, y, label="$y_n$", color="violet", linewidth=2.25)
    plt.xlabel("Indeks n")
    plt.ylabel("Wartość $y_n$")
    plt.legend(loc="best")
    plt.savefig("wykres_N3.pdf")


if __name__ == "__main__":
    main()
