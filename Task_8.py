from pulp import *

# Создание объекта модели
prob = LpProblem("Simple LP Problem", LpMaximize)

# Определяем переменные решения
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
# Определяем целевую функцию
prob += x1 + x2 + x3

# Определяем ограничения
prob += x1 + 2*x2 + 3*x3<= 1, "1st constraint"
prob += 5*x1 + 3*x2 + 4*x3<= 1, "2nd constraint"
prob += 5*x1 + 4*x2 + 0*x3<= 1, "3rd constraint"
prob += x1 >= 0, "4rd constraint"
prob += x2 >= 0, "5rd constraint"
prob += x3 >= 0, "6rd constraint"

# Решаем задачу линейного программирования
prob.solve()

# Печатаем результаты
print ("Статус: ", LpStatus[prob.status])
list=[]
for v in prob.variables():
    print (v.name, "=", v.varValue)
    list.append(v.varValue)

newx1=list[0]/value(prob.objective)
newx2=list[1]/value(prob.objective)
newx3=list[2]/value(prob.objective)

game_price = 1/value(prob.objective)
print(f'Ответ: X* = ({newx1, newx2, newx3})' + f' оптимальная стратегия I игрока, Y∗ = ({newx1, newx2, newx3}) – оптимальная стратегия II игрока,' + f'νA = {game_price} – цена игры.')
