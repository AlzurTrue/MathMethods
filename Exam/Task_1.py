from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(12, 'x')
c= [0,  13,  9,  8,
    15, 8, 7, 10,
    3, 15,  20, 0]
z=(c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] +
   c[4]*x[4] + c[5]* x[5]+c[6]*x[6] +c[7]*x[7] +
   c[8]* x[8] + c[9]* x[9] + c[10]* x[10] + c[11]* x[11])

mass1 = (x[0] + x[1] +x[2] + x[3] <= 240)
mass2 = (x[4] + x[5] + x[6] + x[7] <= 70)
mass3 = (+ x[8] + x[9] + x[10] + x[11] <= 140)

mass4 = (x[0] + x[4] + x[8] == 90)
mass5 = (x[1] +x[5] + x[9] == 190)
mass6 = (x[2] + x[6] + x[10] == 40)
mass7 = (x[3] + x[7] + x[11] == 130)


x_non_negative = (x >= 0)
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,mass6, mass7, x_non_negative])
problem.solve(solver='glpk')
print("Результат Xopt:")

print(str(x.value[0]) + "  " + str(x.value[1]) + "  " + str(x.value[2]) + "  " + str(x.value[3]))
print(str(x.value[4]) + "  " + str(x.value[5]) + "  " + str(x.value[6]) + "  " + str(x.value[7]))
print(str(x.value[8]) + "  " + str(x.value[9]) + "  " + str(x.value[10]) + "  " + str(x.value[11]))
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)