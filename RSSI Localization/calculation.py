from numpy import *
from math import *
n = 9
size = 1001
d0 = 0.2
d = []
r = []
y = []
f = 0.0
nx = 0.0
a = [0.0]*4
up = 300.0
down = 0.1
eps = 0.0000001

def getData():
    global n, size, d, r, y, d0
    f = open('rssi', 'r')
    g = open('data', 'w')
    x = [0.0]*size
    d = [0.0]*(n + 1)
    r = [0.0]*(n + 1)
    y = [0.0]*(n + 1)
    d[0] = 0.0
    for i in range (0, n):
        d[i + 1] = d[i] + d0
        mean = 0.0
        for k in range (0, size):
            x[k] = float(f.readline())
            mean += x[k]
        mean /= size
        r[i + 1] = mean
        var = 0.0
        for k in range(0, size):
            var += (x[k] - mean)**2
        var /= size - 1
        y[i + 1] = var
        g.writelines(str(mean) + ' ' + str(var) + '\n')
    f.close()
    g.close()

def LNSM_DV():
    global n, d, y, r, f, nx, a, d0
    m1 = [0.0]*2
    m2 = [0.0]*2
    mc = [0.0]*2
    for i in range (1, n + 1):
        t = log(d[i]/d0, 10)
        m1[0] += t*t
        m1[1] += t
        mc[0] += r[i]*t
        mc[1] += r[i]
    m1[0] *= 10
    m2[0] = 10*m1[1]
    m2[1] = n
    sol = linalg.solve([m1, m2], mc)
    f = sol[1]
    nx = sol[0]

    m = [[0.0 for x in range(4)] for x in range(4)]
    C = [0.0]*4
    D = [0.0]*7
    Dy = [0.0]*4
    for i in range(1, n + 1):
        for k in range(0, 7):
            D[k] += d[i] ** k
        for k in range(0, 4):
            Dy[k] += y[i]*(d[i] ** k)
    for i in range(0, 4):
        C[i] = Dy[3 - i]
        for k in range(0, 4):
            m[i][k] = D[6 - i - k]
    sol2 = linalg.solve(m, C)
    for i in range (0, 4):
        a[i] = sol2[i]

def fx(d):
    global f, nx, a
    return f + 10*nx*log(d/0.2, 10) - sqrt(a[0]*(d**3) + a[1]*(d**2) + a[2]*d + a[3])

def solve(rssi):
    global up, down, eps
    m = 0.5*(down + up)
    while(abs(fx(m) - rssi) > eps):
        if(fx(m) - rssi < 0):
            up = m
        else:
            down = m
        m = 0.5*(down + up)
    return m

def cal():
    getData()
    LNSM_DV()
    print("rssi = %s + 10*(%s)*log(d/d0, 10) - sqrt(%s*d^3 + %s*d^2 + %s*d + %s)" %(f, nx, a[0], a[1], a[2], a[3]))
    print(solve(-70))

cal()