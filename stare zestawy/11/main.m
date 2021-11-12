close all; clear; clc;

tol = 1e-6 / 2;
f = @(x) exp(sin(x) .^ 2);
a = 0;
b = pi/2;

% metoda trapezow
h = (b - a) * 0.5;
Q = (f(a) + f(b)) * h;
err = tol;
iter = 1;

while err >= tol
  Qpre = Q;
  Q = 0.5 * Q + h * sum(f((a + h) : (2*h) : (b - h)));
  h = 0.5 * h;
  err = abs(Q - Qpre);
  iter = iter + 1;
end

Q1 = 2 * Q
err1 = 2 * err
iter1 = iter


% metoda Simpsona
h = (b - a) / 6;
Qt = (f(a) + f(b)) * h;
S = 4 * f((a + b) * 0.5);
Q = Qt + S * h; %(f(a) + 4 * f((a + b) * 0.5) + f(b)) * h;
err = tol;
iter = 1;
h = (b - a) / 4;

while err >= tol
  Qpre = Q;
  Qt = 0.5 * Qt + S * (h / 6);
  S = 4 * sum(f((a + h) : (2*h) : (b - h)));
  Q = Qt + (h / 3) * S;
  h = h / 2;
  err = abs(Q - Qpre);
  iter = iter + 1;
end

Q2 = 2 * Q
err2 = 2 * err
iter2 = iter


% metoda 3/8
h = (b - a) / 3;
Qt = (f(a) + f(b)) * (3/8 * h);
S = f(a + h) + f(a + 2 * h);
Q = Qt + (9/8 * h) * S;

err = tol;
iter = 1;

while err >= tol
  h = h / 3;
  Qpre = Q;
  Qt = Qt / 3 + (3/4 * h) * S;
  S = sum(f((a + h) : (3*h) : b)) + sum(f((a + 2 * h) : (3*h) : b));
  Q = Qt + (9/8 * h) * S;
  err = abs(Q - Qpre);
  iter = iter + 1;
end

Q3 = 2 * Q
err3 = 2 * err
iter3 = iter