from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(15, 'x')
c= [9,  4,  6,  5, 6,
    17, 11, 15, 3, 7,
    20, 9,  15, 7, 25]
z=(c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] + c[4]*x[4] +
   c[5]* x[5]+c[6]*x[6] +c[7]*x[7] +c[8]* x[8] + c[9]* x[9] +
   c[10]* x[10] + c[11]* x[11] + c[12]* x[12] + c[13]* x[13] + c[14]* x[14])

mass1 = (x[0] + x[1] +x[2] + x[3] + x[4] <= 270)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 390)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 290)

mass4 = (x[0] + x[5] + x[10] == 150)
mass5 = (x[1] +x[6] + x[11] == 100)
mass6 = (x[2] + x[7] + x[12] == 250)
mass7 = (x[3] + x[8] + x[13] == 340)
mass8 = (x[4] + x[9] + x[14] == 110)

x_non_negative = (x >= 0)
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,mass6, mass7, mass8,x_non_negative])
problem.solve(solver='glpk')
print("Результат Xopt:")

print(str(x.value[0]) + "  " + str(x.value[1]) + "  " + str(x.value[2]) + "  " + str(x.value[3]) + "  " + str(x.value[4]))
print(str(x.value[5]) + "  " + str(x.value[6]) + "  " + str(x.value[7]) + "  " + str(x.value[8]) + "  " + str(x.value[9]))
print(str(x.value[10]) + "  " + str(x.value[11]) + "  " + str(x.value[12]) + "  " + str(x.value[13]) + "  " + str(x.value[14]))
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)