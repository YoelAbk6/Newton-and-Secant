Newton Raphson and Secant methods

==Description==

The program takes a function f(x) and finds her roots using Newton Raphson
and the Secant methods.

The methods will stop on three conditions:
1) The current proximity is "very close" to the previous one
2) The f(Xn) is "very close" to zero
3) The maximal number of iterations has been reached 
---EPS is defined as 10^-10.

For each method, the program prints the current proximity and the corresponding graph.


==Functions==
Three main functions:

1. newton - Implements the NR method
2. secant - Implements the secant method
3. convergence - Computes the convergence rate and constant

==Program files==
ex2.py

==Output==
Current proximity and the initial root
Corresponding graph for each iteration

