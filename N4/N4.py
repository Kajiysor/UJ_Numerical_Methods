import numpy as np
import matplotlib.pyplot as plt

N = 1000
h = 0.01

# wzor na wyliczenie y_n+1 znajac y_n i y_n-1


def find_y(y_n0, y_n1):
    return (2 - h*h)*y_n1 - y_n0
#


def main():
    y = np.zeros(N+1)

    # y1 i y2 wyliczone w sposób jawny z wzorów
    y[0] = 1
    y[1] = 4 / (6 - h*h)
    #

    for n in range(2, N+1):
        y[n] = find_y(y[n-2], y[n-1])

    plt.title("Wykres wartości wektora y")
    size = np.arange(0, (N+1)*h, h)
    plt.plot(size, y, label="$y_n$", color="purple", linewidth=2.25)
    plt.xlabel("Indeks n")
    plt.ylabel("Wartość $y_n$")
    plt.legend(loc="best")
    plt.savefig("wykres_N4.pdf")


if __name__ == "__main__":
    main()
