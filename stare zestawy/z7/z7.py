N = 3
iterations = 0

def conjugateGradient(A, b, x):
    d = []
    g = []
    p = []

    alpha = 0
    beta = 0
    dividend = 0
    divisor = 0
    temp0 = 0
    temp1 = 0
    abstand = 0
    stol = 0.0

    i = 0
    j = 0
    k = 0
    
    for i in range(N):
        x.append(0)
        p.append(0)
    
    for i in range(N): 
        temp0 = b[i]
        d.append(temp0)
        g.append(-temp0)
    
    
    for k in range(N, 0, -1):
        dividend = 0
        divisor  = 0

        for i in range(N): 
            dividend += d[i] * g[i]

            temp0 = 0
            for j in range(i):
                temp0 += A[j][i] * d[j]
            
            for j in range(i, N, 1):
                temp0 += A[i][j] * d[j]
            
            
            p[i] = temp0
            divisor += d[i] * temp0
        
        alpha = -dividend / divisor
        stol   = 0
        abstand = 0
        
        for i in range(N):  
            temp0 =  x[i]
            stol += pow(temp0, 2.0)
            temp1 =  alpha * d[i]
            abstand += pow(temp1, 2.0)
            x[i] =  temp0 + temp1
        
        
        for i in range(N):  
            g[i] += alpha * p[i]
        
        dividend = 0
        
        for i in range(N): 
            dividend += g[i] * p[i]
        
        
        beta = dividend / divisor
        
        for i in range(N): 
            d[i] = -g[i] + beta * d[i]
            
        global iterations
        iterations += 1

A = [4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]
b = [2.0, 6.0, 2.0]

x = []
    
conjugateGradient(A, b, x);
    
print "Wyniki: \n"
for i in range(N): 
    print "\t{}".format(x[i])