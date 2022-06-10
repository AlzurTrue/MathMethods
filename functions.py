from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import optimize
from sympy import *
import numpy as np
import sys


class Optimization:
    """API для задач оптимизации целевых функций"""
    def __init__(self):
        self.q1 = None
        self.q2 = None
        self.C = None
        self.P = None
        self.I = None
        self.bounds = None
        self.max_p1 = None
        self.max_p2 = None
        self.extremum = None
        self.__expr_q1 = None
        self.__expr_q2 = None
        self.__expr_C = None
        self.__expr_P = None

    def start(self, task_number):
        """Начальный метод, запускающий программу"""
        try:

            if task_number == "exit":
                print("Выход из системы...")
                sys.exit()
            elif task_number == 2:
                self.q1 = '58 - 2 * p1'
                self.q2 = '28 - 1 * p2'
                self.C = '3 * (q1 ** 2) + 5 * q1 * q2 + 2 * (q2 ** 2) + 9'
                self.P = 'p1 * q1 + p2 * q2 - C'

            elif task_number == 3:
                self.q1 = 3
                self.q2 = 16
                self.I = 1847
                self.C = 'x * p + y * q'
                self.P = '5 * (x - 7) * (y ** (5/6))'
                self.bounds = [0, 0]

            elif task_number == 4:
                self.q1 = 4
                self.q2 = 2
                self.I = 100
                self.C = 'x * p + y * q'
                self.P = '40 * (x ** 0.33) * (y ** 0.25)'
                self.bounds = [0, 0]

            eval(f"self.task_{task_number}()")
        except (AttributeError, ValueError, TypeError):
            print("Введите правильный номер задачи (или exit)!")


    def task_2(self):
        """Задача по нахождению максимальной прибыли по оптимальному плану фирмы-монополиста"""
        print(self.__formulas_concatenation())

        result = self.__find_max()
        print(f"Оптимальный план (q1*, q2*): ({round(result.get('p1'), 3)}, {round(result.get('p2'), 3)})")
        print(f"Максимальная прибыль П(q1*, q2*): {round(result.get('ext'), 3)}")

        calc_formulas = self.__calc_formulas_with_max()
        print(f"Значения q1 при максимальном p1: {round(calc_formulas.get('q1'), 3)}")
        print(f"Значения q2 при максимальном p2: {round(calc_formulas.get('q2'), 3)}")
        print(f"Значения C при максимальных p1 и p2: {round(calc_formulas.get('C'), 3)}")
        print(f"Значения P при максимальных p1 и p2: {round(calc_formulas.get('P'), 3)}")

        self.__draw_chart("Оптимальный план (q1*, q2*)",
                          ["p1", "p2"],
                          "Прибыль фирмы-монополиста, тыс. руб.",
                          "Цена единицы товара x1",
                          "Цена единицы товара x2")
        self.__draw_contour()

    def task_3(self):
        """Задача по нахождению оптимального выбора потребителя"""
        self.__expr_C = parse_expr(self.C, evaluate=False).subs([("p", self.q1), ("q", self.q2)])
        self.__expr_P = parse_expr(self.P, evaluate=False)
        result = self.__find_max_with_constrains()

        print(f"Оптимальный набор товаров (x*, y*): ({round(result.get('p1'), 3)}, {round(result.get('p2'), 3)})")
        print(f"Максимальная полезность U(x*, y*): {round(result.get('ext'), 3)}")

        self.__draw_chart("U(x*, y*)",
                          ["x", "y"],
                          "Полезность потребителя",
                          "Количество товаров x",
                          "Количество товаров y")
        self.__draw_contour_2()

    def task_4(self):
        """Задача максимизации прибыли производителя"""
        self.__expr_C = parse_expr(self.C, evaluate=False).subs([("p", self.q1), ("q", self.q2)])
        self.__expr_P = parse_expr(self.P, evaluate=False)
        result = self.__find_max_with_constrains()

        print(f"Оптимальный набор товаров (x*, y*): ({round(result.get('p1'), 3)}, {round(result.get('p2'), 3)})")
        print(f"Максимальная прибыль Q(x*, y*): {round(result.get('ext'), 3)}")

        self.__draw_chart4("Q(x*, y*)",
                          ["x", "y"],
                          "Производственная функция",
                          "Количество ресурсов x",
                          "Количество ресурсов y")
        self.__draw_contour_3()

    def get_max_p1(self) -> float:
        """Получение оптимального значения цены p1"""
        return self.max_p1

    def get_max_p2(self) -> float:
        """Получение оптимального значения цены p2"""
        return self.max_p2

    def get_extremum(self) -> float:
        """Получение оптимальной прибыли компании"""
        return self.extremum

    def input_bounds(self) -> None:
        """Ввод ограничений для формул функций в виде списка"""
        self.bounds = list(map(int, str(input("Введите ограничения bounds в виде списка через пробел: ")).split()))

    def input_q1(self) -> None:
        """Ввод формулы функции спроса q1 или параметр (содержит p1 параметр)"""
        self.q1 = str(input("Введите q1: "))

    def input_q2(self) -> None:
        """Ввод формулы функции спроса q2 или параметр (содержит p2 параметр)"""
        self.q2 = str(input("Введите q2: "))

    def input_I(self) -> None:
        """Ввод дохода потребителя I"""
        self.q2 = str(input("Введите I: "))

    def input_C(self) -> None:
        """Ввод формулы функции издержек C (содержит q1 и q2 параметры)"""
        self.C = str(input("Введите C: "))

    def input_P(self) -> None:
        """Ввод формулы функции прибыли P (содержит p1, p2, q1, q2 и C параметры)"""
        self.P = str(input("Введите P: "))

    def check_formulas(self) -> bool:
        """Проверка корректного формата формул функций"""
        try:
            sympify(self.q1)
            sympify(self.q2)
            sympify(self.C)
            sympify(self.P)
            return True
        except SympifyError:
            return False

    def __formulas_concatenation(self) -> str:
        """Преобразование формул в простой вид"""
        if self.check_formulas():
            self.__expr_q1 = simplify(self.q1)
            self.__expr_q2 = simplify(self.q2)

            self.__expr_C = simplify(self.C)
            self.__expr_C = self.__expr_C.subs([("q1", self.q1), ("q2", self.q2)])

            self.__expr_P = simplify(self.P)
            self.__expr_P = self.__expr_P.subs([("q1", self.q1), ("q2", self.q2), ("C", self.__expr_C)])

            return "Формулы преобразованы в простой вид"
        else:
            return "Проверьте правильность введенных формул!"

    def __find_max(self) -> dict:
        """Нахождение максимальной прибыли и оптимального плана"""
        if self.__expr_P is not None:
            res = optimize.minimize(lambda x: -lambdify(["p1", "p2"], self.__expr_P)(*x), (0, 0))
            self.max_p1, self.max_p2, self.extremum = res.x[0], res.x[1], -res.fun
            return {"ext": self.extremum, "p1": self.max_p1, "p2": self.max_p2}
        return {}

    def __find_max_with_constrains(self) -> dict:
        """Нахождение максимальной полезности и оптимального набора товаров"""
        if self.check_formulas():
            res = optimize.minimize(
                lambda a: -lambdify(symbols('x y'), self.__expr_P)(*a),
                list(map(lambda t: t + 1, self.bounds)),
                constraints={
                    'type': 'ineq',
                    'fun': lambda a: -lambdify(symbols('x y'), self.__expr_C)(*a) + self.I},
                bounds=[(bound, np.inf) for bound in self.bounds]
            )

            self.max_p1, self.max_p2 = list(map(round, res.x.tolist()))
            if round(res.fun, 3) == 0: self.extremum = res.fun
            else: self.extremum = -res.fun

            return {"ext": self.extremum, "p1": self.max_p1, "p2": self.max_p2}
        return {}

    def __calc_formulas_with_max(self) -> dict:
        """Вычисление значений формул по оптимальному плану"""
        if self.max_p1 is not None and self.max_p2 is not None and self.extremum is not None:
            return {"q1": self.__expr_q1.subs([('p1', str(self.max_p1))]),
                    "q2": self.__expr_q2.subs([('p2', str(self.max_p2))]),
                    "C": self.__expr_C.subs([("p1", str(self.max_p1)), ("p2", str(self.max_p2))]),
                    "P": self.__expr_P.subs([("p1", str(self.max_p1)), ("p2", str(self.max_p2))])}
        return {}

    def __draw_chart(self, label: str, params: list, title: str, xlabel: str, ylabel: str) -> None:
        """Изображение 3D-графика прибыли фирмы-монополиста"""
        if self.__expr_P is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)

            plt.figure()
            ax = plt.axes(projection='3d')

            x = np.linspace((-p1 - 1) * 5, (p1 + 1) * 5, (p1 + 1) * 10)
            y = np.linspace(0, (p2 + 1) * 5, (p2 + 1) * 10)
            X, Y = np.meshgrid(x, y)
            Z = lambdify(params, self.__expr_P)(X, Y)
            Z = np.nan_to_num(Z, copy=True, nan=0.0, posinf=None, neginf=None)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="viridis")
            ax.scatter(self.max_p1, self.max_p2, self.extremum, s=10, color="red", label=label)

            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.legend()
            plt.show()

    def __draw_chart4(self, label: str, params: list, title: str, xlabel: str, ylabel: str) -> None:
        """Изображение 3D-графика прибыли фирмы-монополиста"""
        if self.__expr_P is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)

            plt.figure()
            ax = plt.axes(projection='3d')

            x = np.linspace(self.bounds[0], (p1 + 1) * 5, (p1 + 1) * 10)
            y = np.linspace(self.bounds[1], (p2 + 1) * 5, (p2 + 1) * 10)
            X, Y = np.meshgrid(x, y)
            Z = lambdify(params, self.__expr_P)(X, Y)
            Z = np.nan_to_num(Z, copy=True, nan=0.0, posinf=None, neginf=None)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="viridis")
            ax.scatter(self.max_p1, self.max_p2, self.extremum, s=25, color="black", label=label)

            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.legend()
            plt.show()

    def __draw_contour(self) -> None:
        """Изображение графика линий уровня прибыли фирмы-монополиста"""
        if self.__expr_P is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)
            x, y = np.mgrid[-5 * p1:p1 * 5, -5 * p2:p2 * 5]
            z = lambdify(["p1", "p2"], self.__expr_P)(x, y)

            fig, ax = plt.subplots()
            ax.contour(x, y, z, levels=20)
            fig.set_figwidth(6)
            fig.set_figheight(6)

            plt.scatter(self.max_p1, self.max_p2, color='red', s=30, label="Максимальная прибыль П(q1*, q2*)")
            plt.title("Прибыль фирмы монополиста, тыс. руб.")
            plt.xlabel("Цена единицы товара x1")
            plt.ylabel("Цена единицы товара x2")
            plt.legend()
            plt.show()

    def __draw_contour_2(self) -> None:
        """Изображение графика линий уровня максимальной полезности"""
        if self.__expr_P is not None and self.__expr_C is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)
            x, y = np.mgrid[-5 * p1:p1 * 5, 0:(p2 + 1) * 5]
            z = lambdify(["x", "y"], self.__expr_P)(x, y)

            fig, ax = plt.subplots()
            ax.contour(x, y, z, levels=20)
            cr = ax.contour(x, y, z, levels=[-self.extremum], colors="red")
            cr.collections[0].set_label("Кривая безразличия")
            # plt.plot(x, lambdify('x', solve(self.__expr_C, 'y'))(x)[0])
            fig.set_figwidth(6)
            fig.set_figheight(6)

            plt.scatter(self.max_p1, self.max_p2, color='black', s=30, label="U(x*, y*)")
            plt.title("Полезность потребителя")
            plt.xlabel("Количество товаров x")
            plt.ylabel("Количество товаров y")
            plt.legend()
            plt.show()
    def __draw_contour_3(self) -> None:
        """Изображение графика линий уровня максимальной полезности"""
        if self.__expr_P is not None and self.__expr_C is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)
            x, y = np.mgrid[self.bounds[0]:p1 * 5, self.bounds[1]:(p2 + 1) * 5]
            z = lambdify(["x", "y"], self.__expr_P)(x, y)

            fig, ax = plt.subplots()
            ax.contour(x, y, z, levels=20)
            cr = ax.contour(x, y, z, levels=[self.extremum], colors="red")
            cr.collections[0].set_label("Кривая безразличия")

            x2 = np.linspace(self.bounds[0], (self.I / self.q1))
            y_tr = (self.I - self.q1 * x2) / self.q2
            fig2 = ax.fill_between(x2, self.bounds[1], y_tr)
            fig2.set_facecolor('green')
            fig2.set_label("Бюджетное множество")

            fig.set_figwidth(6)
            fig.set_figheight(6)

            plt.scatter(self.max_p1, self.max_p2, color='black', s=30, label="Q(x*, y*)")
            plt.title("Производство")
            plt.xlabel("Количество ресурсов x")
            plt.ylabel("Количество ресурсов y")
            plt.legend()
            plt.show()

    def __draw_contour_3(self) -> None:
        """Изображение графика линий уровня максимальной полезности"""
        if self.__expr_P is not None and self.__expr_C is not None:
            p1, p2 = int(self.max_p1), int(self.max_p2)
            x, y = np.mgrid[self.bounds[0]:p1 * 5, self.bounds[1]:(p2 + 1) * 5]
            z = lambdify(["x", "y"], self.__expr_P)(x, y)

            fig, ax = plt.subplots()
            ax.contour(x, y, z, levels=20)
            cr = ax.contour(x, y, z, levels=[self.extremum], colors="red")
            cr.collections[0].set_label("Кривая безразличия")

            x2 = np.linspace(self.bounds[0], (self.I / self.q1))
            y_tr = (self.I - self.q1 * x2) / self.q2
            fig2 = ax.fill_between(x2, self.bounds[1], y_tr)
            fig2.set_facecolor('green')
            fig2.set_label("Бюджетное множество")

            fig.set_figwidth(6)
            fig.set_figheight(6)

            plt.scatter(self.max_p1, self.max_p2, color='black', s=30, label="Q(x*, y*)")
            plt.title("Производство")
            plt.xlabel("Количество ресурсов x")
            plt.ylabel("Количество ресурсов y")
            plt.legend()
            plt.show()


if __name__ == "__main__":
    o = Optimization()
    o.start()
