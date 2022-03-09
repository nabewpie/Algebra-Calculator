print("AlgCalc v1.1")
print("PLEASE SPECIFY THE SIGNS!!!")

term1_coef = input("Term 1 coefficient: ")
term1_var = input("Term 1 Variable: ")
term2_coef = input("Term 2 Coefficient: ")
term2_var = input("Term 2 Variable: ")

term1 = str(term1_coef)+str(term1_var)
term2 = str(term2_coef)+str(term2_var)
print("Answer for the equation "+ term1 + term2 + " is:")

coeff_add = int(term1_coef) + int(term2_coef)
result = str(coeff_add) + str(term2_var)
if term1_var != term2_var:
	print("Cannot further be simplified")
else:
	print(result)

