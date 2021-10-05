from math import *

m = 1.0
c = 300000000.0
v = 1.0

def E_rel():
    return(float(m*(c**2)*(1/(sqrt(1-(v**2/c**2)))-1)))

def E_nrel():
    return(float((1/2)*m*(v**2)))

print (E_rel())
print (E_nrel())