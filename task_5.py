from sympy import plot_implicit, symbols, And, Eq
from pulp import *

# Создание объекта модели
prob = LpProblem("Simple LP Problem", LpMaximize)

# Определяем переменные решения
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
# Определяем целевую функцию
prob += x1 + 4*x2

# Определяем ограничения
prob += x1 + 2*x2 <= 10, "1st constraint"
prob += 3*x1 + 2*x2 <= 18, "2nd constraint"
prob += x1 - x2 >= -8, "3rd constraint"
prob += 0.75*x1 - x2 <= 9, "4rd constraint"

# Решаем задачу линейного программирования
prob.solve()

# Печатаем результаты
print ("Статус: ", LpStatus[prob.status])
list=[]
for v in prob.variables():
    print (v.name, "=", v.varValue)
    list.append(v.varValue)

print ("Оптимальное значение целевой функции равно = ", value(prob.objective))
print(f'Ответ: M*{list[0], list[1]}' + "; Fmin = F(M*) = " + str(value(prob.objective)))

x1, x2 = symbols('x1 x2')
p1 = plot_implicit(And(x1 + 2*x2<= 10,
                       3*x1 + 2*x2<= 18,
                       x1-x2>=-8,
                       3/4*x1-x2<=9),
                   x_var=(x1, -20, 20), y_var=(x2, -10, 10), line_color='yellow',
                   markers=[{'args': list, 'color': "blue", 'marker': "o", 'ms': 5}],
                   annotations=[{'xy': list, 'text': f'  M*{list[0], list[1]}', 'ha': 'left', 'va': 'top', 'color': 'blue'}],
                   show=False

              )

#Строим линии
p2 = plot_implicit(Eq(x1 + 2*x2, 10), (x1, -20, 20), (x2, -10, 10), show=False)
p3 = plot_implicit(Eq(3*x1 + 2*x2, 18), (x1, -20, 20), (x2, -10, 10), show=False)
p4 = plot_implicit(Eq(x1-x2, -8), (x1, -20, 20), (x2, -10, 10), show=False)
p5 = plot_implicit(Eq(3/4*x1-x2, 9), (x1, -20, 20), (x2, -10, 10), show=False)

#Добавляем графики все в одного
p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])
p1.append(p5[0])
p1.show()