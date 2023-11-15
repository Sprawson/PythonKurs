import time
import math

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = [x for x in range(100000)]

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print(f"Max: {max(results_list)}" )
    print(f"Min: {min(results_list)}")
    stop = time.time()
    print(f"Time for this operation was: {stop-start}")

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, "internal code", 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print(f"Max: {max(results_list)}" )
    print(f"Min: {min(results_list)}")
    stop = time.time()
    print(f"Time for this operation was: {stop-start}")


