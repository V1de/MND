from random import randint


def main(m_tmp):
    m = m_tmp
    N = 8
    d = 8
    print("y' = b0 + b1*x1 + b2*x2 + b3*x3 + b12*x1*x2 + b13x1*x3 + b23*x2*x3 + b123*x1*x2*x3")

    x1 = [-30, 0]
    x2 = [-35, 10]
    x3 = [0, 20]

    print("x1_min =", x1[0], ", x1_max = ", x1[1])
    print("x2_min =", x2[0], ", x2_max = ", x2[1])
    print("x3_min =", x3[0], ", x3_max = ", x3[1])

    xcp_min = (x1[0] + x2[0] + x3[0])/3
    xcp_max = (x1[1] + x2[1] + x3[1])/3

    print("\nXcp min = ", xcp_min)
    print("Xcp max = ", xcp_max)

    y_min = 200 + xcp_min
    y_max = 200 + xcp_max

    print("\nY min = ", y_min)
    print("Y max = ", y_max)

    y_matrix = [[randint(int(y_min), int(y_max)) for i in range(m)] for k in range(N)]
    print("\nY matrix:\n", y_matrix)

    average_y = [round(sum(i) / len(i), 3) for i in y_matrix]
    print("\nAverage y:\n", average_y)

    normalized_x = [[-1, -1, -1],
                    [-1, -1, 1],
                    [-1, 1, -1],
                    [-1, 1, 1],
                    [1, -1, -1],
                    [1, -1, 1],
                    [1, 1, -1],
                    [1, 1, 1]]

    b0 = sum(average_y) / N
    b1 = sum([average_y[i] * normalized_x[i][0] for i in range(N)]) / N
    b2 = sum([average_y[i] * normalized_x[i][1] for i in range(N)]) / N
    b3 = sum([average_y[i] * normalized_x[i][2] for i in range(N)]) / N
    b12 = sum([average_y[i] * normalized_x[i][0] * normalized_x[i][1] for i in range(N)]) / N
    b13 = sum([average_y[i] * normalized_x[i][0] * normalized_x[i][2] for i in range(N)]) / N
    b23 = sum([average_y[i] * normalized_x[i][1] * normalized_x[i][2] for i in range(N)]) / N
    b123 = sum([average_y[i] * normalized_x[i][0] * normalized_x[i][1] * normalized_x[i][2] for i in range(N)]) / N

    plan_matrix = [[x1[0], x2[0], x3[0], x1[0] * x2[0], x1[0] * x3[0], x2[0] * x3[0], x1[0] * x2[0] * x3[0]],
                    [x1[0], x2[0], x3[1], x1[0] * x2[0], x1[0] * x3[1], x2[0] * x3[1], x1[0] * x2[0] * x3[1]],
                    [x1[0], x2[1], x3[0], x1[0] * x2[1], x1[0] * x3[0], x2[1] * x3[0], x1[0] * x2[1] * x3[0]],
                    [x1[0], x2[1], x3[1], x1[0] * x2[1], x1[0] * x3[1], x2[1] * x3[1], x1[0] * x2[1] * x3[1]],
                    [x1[1], x2[0], x3[0], x1[1] * x2[0], x1[1] * x3[0], x2[0] * x3[0], x1[1] * x2[0] * x3[0]],
                    [x1[1], x2[0], x3[1], x1[1] * x2[0], x1[1] * x3[1], x2[0] * x3[1], x1[1] * x2[0] * x3[1]],
                    [x1[1], x2[1], x3[0], x1[1] * x2[1], x1[1] * x3[0], x2[1] * x3[0], x1[1] * x2[1] * x3[0]],
                    [x1[1], x2[1], x3[1], x1[1] * x2[1], x1[1] * x3[1], x2[1] * x3[1], x1[1] * x2[1] * x3[1]]]

    print("\nMатриця планування: \n", plan_matrix)

    normalized_plan_matrix = [[-1, -1, -1, 1, 1, 1, -1],
                              [-1, -1, 1, 1, -1, -1, 1],
                              [-1, 1, -1, -1, 1, -1, 1],
                              [-1, 1, 1, -1, -1, 1, -1],
                              [1, -1, -1, -1, -1, 1, 1],
                              [1, -1, 1, -1, 1, -1, -1],
                              [1, 1, -1, 1, -1, -1, -1],
                              [1, 1, 1, 1, 1, 1, 1]]

    result_y = []
    for i in range(N):
        result_y.append(b0 + b1 * plan_matrix[i][0] + b2 * plan_matrix[i][1] + b3 * plan_matrix[i][2] +
                        b12 * plan_matrix[i][3] + b13 * plan_matrix[i][4] + b23 * plan_matrix[i][5] +
                        b123 * plan_matrix[i][6])

    print("\nПЕРЕВІРКА ОДНОРІДНОСТІ ДИСПЕРСІЇ ЗА КРИТЕРІЄМ КОХРЕНА")
    matrix_dispersion_y = [sum([(y_matrix[j][i] - average_y[i]) ** 2 for i in range(m)]) / m for j in range(N)]
    print("dispersion: \n", matrix_dispersion_y)

    gp = max(matrix_dispersion_y) / sum(matrix_dispersion_y)
    print("Gp = ", gp)

    # f1=m-1=2, f2=N=8, q=0.05 => Gт=0.5157 за таблицею
    if gp > 0.5157:
        print("Дисперсія неоднорідна!")
        m += 1
        main(m)
    else:
        print("Gp < 0.5157 => Дисперсія однорідна")

    print("\nПЕРЕВІРКА ЗНАЧУЩОСТІ КОЕФІЦІЄНТІВ ЗА КРИТЕРІЄМ СТЬЮДЕНТА")
    s2b = sum(matrix_dispersion_y) / N
    s2bs = s2b / (m * N)
    sbs = s2bs ** (1/2)
    print("sbs = ", sbs)

    b_array = [b0, b1, b2, b3, b12, b13, b23, b123]
    t_array = [abs(b_array[i]) / sbs for i in range(N)]

    print("beta: ", b_array)
    print("t: ", t_array, "\n")
    b_result = b_array

    f1 = m - 1
    f2 = N
    f3 = f1 * f2

    for i in range(N):
        if t_array[i] < 2.120:
            b_result[i] = 0
            d -= 1
            print('Виключаємо з рівняння статистично незначущий коефіціент b', i)

    y_reg = [b_result[0] + b_result[1] * plan_matrix[i][0] + b_result[2] * plan_matrix[i][1] + b_result[3] * plan_matrix[i][2] + b_result[4] * plan_matrix[i][3] + b_result[5] * plan_matrix[i][4] + b_result[6] * plan_matrix[i][5] + b_result[7] * plan_matrix[i][6] for i in range(N)]
    print("Значення рівнянь регресій:\n", y_reg)

    print("\nПЕРЕВІРКА АДЕКВАТНОСТІ ЗА КРИТЕРІЄМ ФІШЕРА")
    f4 = N - d
    sad = (m / (N - d)) * int(sum([(y_reg[i] - average_y[i]) ** 2 for i in range(N)]))
    Fp = sad / s2b
    print("Кількість значимих коефіціентів:", d)
    print("\nFp = ", Fp)

    if Fp > 4.5:
        print("Рівняння регресії неадекватно оригіналу при рівні значимості 0.05")
    else:
        print("Рівняння регресії адекватно оригіналу при рівні значимості 0.05")

    print("Рівняння: \n "
          f"y = {b0} + {b1} * x1 + {b2} * x2 + {b3} * x3 + {b12} * x1x2 + {b13} * x1x3 + {b23} * x2x3 + {b123} * x1x2x3")


if __name__ == '__main__':
    main(3)
