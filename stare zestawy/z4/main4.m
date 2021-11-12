close all; clear; clc;

f = @(x) 1.0 ./ (1.0 + 25.0 * x .* x);

N = 1000 - 1;

a = 1.0;
b = 4.0;
c = ones(N, 1);
u = zeros(N, 1);
h = 2.0 / (N + 1);
x = ((-1) : h : 1)';

n = N - 1;

fx = f(x);
g = 6.0 / (h * h) * (fx(1:n) - 2 * fx(2:N) + fx(3:(N+1)));
u = g;

c(1) = c(1) / 3;
u(1) = u(1) / 3;

for i = 2 : (n - 1)
  d = b - a * c(i - 1);
  c(i) = c(i) / d;
  u(i) = (u(i) - a * u(i - 1)) / d;
end

u(n) = (u(n) - a * u(n - 1)) / (3 - a * c(n - 1));

for i = (n - 1) : -1 : 1
  u(i) = u(i) - c(i) * u(i + 1);
end


c = ones(N, 1);
q = zeros(n, 1);
q(1) = 1; q(n) = 1;
c(1) = c(1) / 3;
q(1) = q(1) / 3;

for i = 2 : (n - 1)
  d = b - a * c(i - 1);
  c(i) = c(i) / d;
  q(i) = (q(i) - a * q(i - 1)) / d;
end

q(n) = (q(n) - a * q(n - 1)) / (3 - a * c(n - 1));

for i = (n - 1) : -1 : 1
  q(i) = q(i) - c(i) * q(i + 1);
end

u = u - ((u(1) + u(n)) / (1 + q(1) + q(n))) * q;

fig = figure;
plot(x(2:N), u);
xlabel('x');
ylabel('u');
title('Wykres zaleznosci');
saveas(fig, 'fig4.png');
close(fig);

Au = 4 * u + [u(2:n); 0] + [0; u(1:(n-1))];
Au(1) = Au(1) + u(n);
Au(n) = Au(n) + u(1);
R = Au - g;

% norma euklidesowa
err_2 = norm(R, 2)

% norma maksumum
err_inf = norm(R, inf)