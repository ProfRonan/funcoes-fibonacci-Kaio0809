def fibonacci(n): 
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    fbncc = [0, 1]

    while len(fbncc) < (n + 1): 
        prox_fib = fbncc[-1] + fbncc[-2]
        fbncc.append(prox_fib)
    return fbncc[n]
