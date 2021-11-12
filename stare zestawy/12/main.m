close all; clear; clc;

tol = 1e-12;
f = @(x) sin(x .^ 2 + log(x)) + tan(x);
df = @(x) cos(x .^ 2 + log(x)) .* (2 * x + 1 ./ x) + 1 ./ cos(x) .^ 2;

h = 0.01;
h2 = h / 2;
xx = 0.01 : h : 10;
yy = f(xx);
pp = xx((yy(2:end) .* yy(1:(end-1))) < 0);
n = length(pp);

z = pi/2 : pi : 10;

for i = 1 : n
  if sum(abs(pp(i) - z) < h) > 0
    pp(i) = -1;
  end
end

pp = pp(pp > 0);
n = length(pp);

x_falsi = zeros(n, 1);
errs_falsi = zeros(n, 1);
x_newton = zeros(n, 1);
errs_newton = zeros(n, 1);
iters_falsi = zeros(n, 1);
iters_newton = zeros(n, 1);

fig = figure;
plot(xx, yy);
grid on;
ylim([-1 1]);


for i = 1 : n
  x = pp(i);
  a = x;
  b = x + h;
  fa = f(a);
  fb = f(b);
  
  % regula falsi
  for iter = 1 : 100
    c = (fa * b - fb * a) / (fa - fb);
    fc = f(c);
    
    if abs(fc) < tol
      break;
    end

    if fa * fc < 0
      b = c;
      fb = fc;
    else
      a = c;
      fa = fc;
    end
  end

  x_falsi(i) = c;
  errs_falsi(i) = abs(fc);
  iters_falsi(i) = iter;

  % metoda Newtona
  fx = f(x);
  for iter = 1 : 50
    x = x - fx / df(x);
    fx = f(x);
    if abs(fx) < tol
      break;
    end
  end

  x_newton(i) = x;
  errs_newton(i) = abs(fx);
  iters_newton(i) = iter;
end

display(x_falsi);
display(errs_falsi);
display(iters_falsi);

display(x_newton);
display(errs_newton);
display(iters_newton);

hold on;
plot(x_newton, zeros(n, 1), 'o');
saveas(fig, 'fig12.png');
close(fig);