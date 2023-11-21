from sympy.physics.quantum.cg import CG
from sympy import S

# Prompt the user for input
j1 = S(input("Enter j1: "))
m1 = S(input("Enter m1: "))
j2 = S(input("Enter j2: "))
m2 = S(input("Enter m2: "))
j = S(input("Enter j: "))
m = S(input("Enter m: "))

# Calculate the Clebsch-Gordan coefficient
cg = CG(j1, m1, j2, m2, j, m)
result = cg.doit()
# Print the result
print("CG coefficient=", (result))
