***Clebsch - Gordan Coefficients Calculator***

Clebsch - Gordan Coefficients play crucial role in many areas of physics. This is a simple code I wrote to compute Clebsch- Gordon Coefficients.



clebsch_gordan.py

Code Explanation

This Python code accurately calculates the Clebsch-Gordan coefficient using the CG function from the sympy.physics.quantum.cg module.

Import Functions
'CG' function is imported from the 'sympy.physics.quantum.cg' module, which provides quantum mechanics tools for the mathematics library 'sympy'. 'S' is imported from sympy to convert the user input into expressions.

Input Statements
Then, there are input statements for j1, m1, j2, m2, j, and m. The input function is used to read the user input as a 'string', and the 'S' function is used to convert each input value to a symbolic expression.

Calculating Clebsch Gordan Coefficients
Then the 'CG' function is used to calculate the Clebsch-Gordan coefficient for the input values. The 'doit' is then called on the 'cg' expression to evaluate it and simplify the result.
