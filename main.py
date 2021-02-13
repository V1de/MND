import random

a0 = 1
a1 = 2
a2 = 3
a3 = 4

X = [[], [], []]
Y = [[], [], [], [], [], [], [], []]
Xn = [[], [], []]

tmp = 1000000
number = 0

for i in range(8):
    for k in range(3):
        X[k].append(random.randint(1, 20))

x0_1 = min(X[0]) + max(X[0])/2
x0_2 = min(X[1]) + max(X[1])/2
x0_3 = min(X[2]) + max(X[2])/2

dx_1 = x0_1 - min(X[0])
dx_2 = x0_2 - min(X[1])
dx_3 = x0_3 - min(X[2])

for k in range(8):
    Y[k] = a0 + a1 * X[0][k] + a2 * X[1][k] + a3 * X[2][k]
    Xn[0].append((X[0][k] - x0_1)/dx_1)
    Xn[1].append((X[1][k] - x0_2)/dx_2)
    Xn[2].append((X[2][k] - x0_3)/dx_3)

avg = sum(Y)/8

for i in range(8):
    if Y[i] - avg > 0 and Y[i] - avg < tmp:
        tmp = Y[i] - avg
        number = i

print("a0 = {} | a1 = {} | a2 = {} | a3 = {}".format(a0, a1, a2, a3))

print("№ | X1 | X2 | X3 | Y | Xn1 | Xn2 | Xn3")
for i in range(8):
    print("{} | {} | {} | {} | {} | {} | {} | {}".format(i, X[0][i], X[1][i], X[2][i], Y[i], Xn[0][i], Xn[1][i], Xn[2][i]))

print("X0| {} | {} | {} |".format(x0_1, x0_2, x0_3))
print("dx| {} | {} | {} |".format(dx_1, dx_2, dx_3))
print("\nAverage Y =", avg)
print("Y <-- X1 - {} | X2 - {} | X3 - {}".format(X[0][number], X[1][number], X[2][number]))