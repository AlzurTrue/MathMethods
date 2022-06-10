from sympy import plot_implicit, symbols, And, Eq
from sympy.plotting import plot3d
from pulp import *

# Создание объекта модели
prob = LpProblem("Simple LP Problem", LpMaximize)

# Определяем переменные решения
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
# Определяем целевую функцию
prob += 36*x1 + 42*x2 + 32*x3

# Определяем ограничения
prob += x1 + 3*x2 + 4*x3<= 3000, "1st constraint"
prob += 6*x1 + 5*x2 + 2*x3<= 3320, "2nd constraint"
prob += x1 >= 0, "3rd constraint"
prob += x2 >= 0, "4rd constraint"
prob += x3 >= 0, "5rd constraint"

# Решаем задачу линейного программирования
prob.solve()

# Печатаем результаты
print ("Статус: ", LpStatus[prob.status])
list=[]
for v in prob.variables():
    print (v.name, "=", v.varValue)
    list.append(v.varValue)

print ("Оптимальное значение целевой функции равно = ", value(prob.objective))
print(f'Ответ: M*{list[0], list[1], list[2]}' + "; Fmax = F(M*) = " + str(value(prob.objective)))
