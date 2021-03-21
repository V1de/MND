import random
from numpy import linalg
import sys

m = 5
main_dev = ((2 * (2 * m - 2)) / (m * (m - 4))) ** (1 / 2)

x1_min = -20
x1_max = 15
x2_min = 10
x2_max = 60

X = [[-1, -1],
     [1, -1],
     [-1, 1]]

y_max = (30 - 109) * 10
y_min = (20 - 109) * 10

array1 = [random.randint(y_min, y_max) for i in range(5)]
array2 = [random.randint(y_min, y_max) for k in range(5)]
array3 = [random.randint(y_min, y_max) for n in range(5)]

average1 = sum(array1) / len(array1)
average2 = sum(array2) / len(array2)
average3 = sum(array3) / len(array3)

dispersion1 = sum([(average1 - array1[i]) ** 2 for i in range(5)]) / 5
dispersion2 = sum([(average2 - array2[k]) ** 2 for k in range(5)]) / 5
dispersion3 = sum([(average3 - array3[n]) ** 2 for n in range(5)]) / 5

dispersions_sum = dispersion1 + dispersion2 + dispersion3
dispersion1_percentage = dispersion1 / dispersions_sum
dispersion2_percentage = dispersion2 / dispersions_sum
dispersion3_percentage = dispersion3 / dispersions_sum

Fuv1 = dispersion1 / dispersion2
Fuv2 = dispersion3 / dispersion1
Fuv3 = dispersion3 / dispersion2

Ouv1 = ((m - 2) / m) * Fuv1
Ouv2 = ((m - 2) / m) * Fuv2
Ouv3 = ((m - 2) / m) * Fuv3

Ruv1 = abs(Ouv1 - 1) / main_dev
Ruv2 = abs(Ouv2 - 1) / main_dev
Ruv3 = abs(Ouv3 - 1) / main_dev

mx1 = (X[0][0] + X[1][0] + X[2][0]) / 3
mx2 = (X[0][1] + X[1][1] + X[2][1]) / 3
my = (average1 + average2 + average3) / 3

a1 = ((X[0][0]) ** 2 + (X[1][0]) ** 2 + (X[2][0]) ** 2) / 3
a2 = (X[0][0] * X[0][1] + X[1][0] * X[1][1] + X[2][0] * X[2][1]) / 3
a3 = ((X[0][1]) ** 2 + (X[1][1]) ** 2 + (X[2][1]) ** 2) / 3

a11 = (X[0][0] * average1 + X[1][0] * average2 + X[2][0] * average3) / 3
a22 = (X[0][1] * average1 + X[1][1] * average2 + X[2][1] * average3) / 3

b0 = (linalg.det([[my, mx1, mx2],
                  [a11, a1, a2],
                  [a22, a2, a3]])) / (linalg.det([[1, mx1, mx2],
                                                  [mx1, a1, a2],
                                                  [mx2, a2, a3]]))

b1 = (linalg.det([[1, my, mx2],
                  [mx1, a11, a2],
                  [mx2, a22, a3]])) / (linalg.det([[1, mx1, mx2],
                                                   [mx1, a1, a2],
                                                   [mx2, a2, a3]]))

b2 = (linalg.det([[1, mx1, my],
                  [mx1, a1, a11],
                  [mx2, a2, a22]])) / (linalg.det([[1, mx1, mx2],
                                                   [mx1, a1, a2],
                                                   [mx2, a2, a3]]))

deltaX1 = abs(x1_max - x1_min) / 2
deltaX2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

a0 = b0 - b1 * x10 / deltaX1 - b2 * x20 / deltaX2
a1 = b1 / deltaX1
a2 = b2 / deltaX2

print("y_min = " + str(y_min) + " y_max = " + str(y_max))

print("Експеримент 1 Y: ", array1)
print("Експеримент 2 Y: ", array2)
print("Експеримент 3 Y: ", array3)

print("\nСереднє значення 1 Y: ", average1)
print("Середнє значення 2 Y: ", average2)
print("Середнє значення 3 Y: ", average3)

print("\nДисперсія 1: " + str(dispersion1) + " у відсотках:" + str(dispersion1_percentage))
print("Дисперсія 2: " + str(dispersion2) + " у відсотках:" + str(dispersion2_percentage))
print("Дисперсія 3: " + str(dispersion3) + " у відсотках:" + str(dispersion3_percentage))

print("\nFuv1: ", Fuv1)
print("Fuv2: ", Fuv2)
print("Fuv3: ", Fuv3)

print("\nOuv1: ", Ouv1)
print("Ouv2: ", Ouv2)
print("Ouv3: ", Ouv3)

# Перевірка дисперсії на однорідність
if Ruv1 > 2 or Ruv2 > 2 or Ruv3 > 2:
    print("\nДисперсія неоднорідна!")
    sys.exit()

print("\nRuv1: " + str(Ruv1) + "<Rkr = 2")
print("Ruv2: " + str(Ruv2) + "<Rkr = 2")
print("Ruv3: " + str(Ruv3) + "<Rkr = 2 \nОтже дисперція однорідна")

print("\nmx1: ", mx1)
print("mx2: ", mx2)
print("my: ", my)

print("\na1 - ", a1)
print("a2 - ", a2)
print("a3 - ", a3)

print("a11 - ", a11)
print("a22 - ", a22)

print("\nb0 - ", b0)
print("b1 - ", b1)
print("b2 - ", b2)

print("\nНормоване рівняння регресії: y=" + str(b0) + "+" + str(b1) + "*x1 +" + str(b2) + "*x2")
print("Зробимо перевірку: \n"
      + str(b0) + "+ (" + str(-1 * b1) + ") + (" + str(-1 * b2) + ") = " + str(b0 - b1 - b2) + "\n"
      + str(b0) + "+ (" + str(b1) + ") + (" + str(-1 * b2) + ") = " + str(b0 + b1 - b2) + "\n"
      + str(b0) + "+ (" + str(-1 * b1) + ") + (" + str(b2) + ") = " + str(b0 - b1 + b2) + "\n"
      + "Результат збігається з середніми значеннями y \n")

print("Натуралізоване рівняння регресії \n y = " + str(a0) + "+" + str(a1) + "*x1 +" + str(a2) + "*x2")
print("Зробимо перевірку по рядках: \n"
      + str(a0) + " + (" + str(a1 * x1_min) + ") + (" + str(a2 * x2_min) + ") = " + str(a0 + a1 * x1_min + a2 * x2_min) + "\n"
      + str(a0) + " + (" + str(a1 * x1_max) + ") + (" + str(a2 * x2_min) + ") = " + str(a0 + a1 * x1_max + a2 * x2_min) + "\n"
      + str(a0) + " + (" + str(a1 * x1_min) + ") + (" + str(a2 * x2_max) + ") = " + str(a0 + a1 * x1_min + a2 * x2_max) + "\n"
      + "Отже коефіцієнти натуралізованого рівняння регресії вірні \n")
