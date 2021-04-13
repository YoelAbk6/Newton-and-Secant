"""The program takes a function f(x) and finds her roots using Newton Raphson method
and the secant method.
For each method the program prints the current proximity and the corresponding graph """

import numpy as np
import matplotlib.pyplot as plt

EPS = 10 ** -10


# receives a float x and returns the computed value f(x)
def f(x):
    return x ** 5 - 3 * x + 7


# receives a float x and returns the computed value df(x)
def der(x):
    return 5 * x ** 4 - 3


# Newton method
def newton(x0, steps):
    i = 0
    x0 = float(x0)
    x1 = 0.0
    x_list = []
    found = False
    while i < steps:
        x1 = x0 - (f(x0) / der(x0))
        x_list.append(x1)
        graphs(x1, "Newton")
        print("x after " + str(steps + 1) + " steps is " + str(x1))
        if abs(f(x1)) < EPS:
            print("|f(x)| < EPS")
            found = True
            break
        if abs(x1 - x0) < EPS:
            print("|x1 - x0| < EPS")
            found = True
            break
        x0 = x1
        steps += 1

    if found:
        print_output("Newton", steps, x1, x_list)
    else:
        print("Newton method stopped after " + str(steps) + " iterations")


# Secant method
def secant(x0, x1, steps):
    i = 0
    x0 = float(x0)
    x1 = float(x1)
    x2 = 0.0
    x_list = []
    found = False
    while i < steps:
        if (x1 != x0) and (f(x1) != f(x0)):
            x2 = x1 - (f(x1) / ((f(x1) - f(x0)) / (x1 - x0)))
            x_list.append(x2)
            graphs(x2, "Secant")
            print("x after " + str(steps + 1) + " steps is " + str(x2))
            if abs(f(x2)) < EPS:
                print("|f(x)| < EPS")
                found = True
                break
            if abs(x2 - x1) < EPS:
                print("|x2 - x1| < EPS")
                found = True
                break
            x0 = x1
            x1 = x2
            steps += 1
        else:
            print("Error! dividing by zero\n")
            return
    if found:
        print_output("Secant", steps, x2, x_list)
    else:
        print("Secant method stopped after " + str(steps) + " iterations")


# receives the method name, number of iterations, the root and the list of approximations -
# prints the corresponding output
def print_output(method_name, steps, x, x_list):
    print(f"{method_name} method found solution after {str(steps + 1)} iterations")
    print(f"The solution is: {x} ")
    if len(x_list) < 4:
        print("There is not enough iterations in order to compute the convergence")
    else:
        print("p is: " + str(convergence(x_list)[0]) + "\nc is: " + str(convergence(x_list)[1]))


# plot graphs
def graphs(x_dot, method_name):
    x = np.linspace(-2, 2, 100)
    y = []
    y_dot = []
    for i in range(len(x)):
        y.append(x[i] ** 5 - 3 * x[i] + 7)
        y_dot.append(der(x_dot) * (x[i] - x_dot) + f(x_dot))
    plt.plot(x, y, 'r')
    plt.plot(x, y_dot, 'g')
    plt.grid()
    plt.ylabel('y')
    plt.xlabel('x')
    plt.axvline()
    plt.axhline()
    plt.title(method_name)
    plt.show()


"""Receives the list of approximations and computes:
    C - The convergence constant
    P - The convergence rate
    Using En - The error in the n'th iteration"""


def convergence(x_list):
    e = []
    for x in x_list[-4:-1]:
        e.append(abs(x - x_list[-1]))
    p = np.log(e[2] / e[1]) / np.log(e[1] / e[0])
    c = (e[2] / pow(e[0], 2))
    return p, c


def main():
    steps = int(input("Enter the maximal iterations allowed"))
    newton(input("Enter your guess"), steps)
    x0, x1 = input("Enter your guesses").split()
    secant(x0, x1, steps)


if __name__ == "__main__":
    main()
