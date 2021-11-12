warning('off','all');
close all; clear; clc;

tol = 1e-6;
tol2 = 2 * tol;
h = 0.1;

V = [inf; inf];
n = 1;

for x = (-3) : h : 3
  for y = (-3) : h : 3
    v = [x; y];
    for iter = 1 : 50
      d = (v(1) + 1) ^ 2 + (v(2) - 1) ^ 2;
      g = [v(1) ^ 2 - sin(v(2) ^ 2); log(d) - 0.98];
      M = [2 * v(1), -2 * v(2) * cos(v(2) ^ 2);
           (2 * (v(1) + 1)) / d, (2 * (v(2) - 1)) / d];
      z = M \ g;
      v = v - z;
      if norm(z, 2) < tol
        if min( abs( sum( diag(v) * ones(2, n) - V ) ) ) > tol2
          n = n + 1;
          V = [V v];
        end
        break;
      end
    end 
  end
end

V = V(:,2:n);
n = n - 1;

errs_2 = zeros(n, 1);
errs_inf = zeros(n, 1);
for i = 1 : n
  v = V(:,i);
  err = abs([v(1) ^ 2 - sin(v(2) ^ 2); log((v(1) + 1) ^ 2 + (v(2) - 1) ^ 2) - 0.98]);
  errs_2(i) = norm(err, 2);
  errs_inf(i) = norm(err, inf);
end

V = V';

display(V);
display(errs_2);
display(errs_inf);