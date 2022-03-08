term1_coef = -46
term1_var = "c"
term2_coef = -10
term2_var = "b"

coeff_add = int(term1_coef) + int(term2_coef)
result = str(coeff_add) + str(term2_var)
if term1_var != term2_var:
	print("Cannot further be simplified")
else:
	print(result)

