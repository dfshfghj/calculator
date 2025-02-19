import sympy


class PadeApproximant(sympy.Function):
    @classmethod
    def eval(cls, f, x, x0, m, n):
        func = f.subs(x,x+x0)
        laurent_series = sympy.series(func, x, 0, n+m+1).removeO()
        highest_negative_power = 0
        for term in laurent_series.as_ordered_terms():
            highest_negative_power = min(term.as_coeff_exponent(x)[1], highest_negative_power)
        coefficients = [0] * (n + m + 1 + highest_negative_power)
        for i in range(n + m + 1 + highest_negative_power):
            coefficients[i] = laurent_series.coeff(x, i + highest_negative_power)
        b = sympy.Matrix(coefficients)
        I = sympy.eye(m+1)
        O = sympy.zeros(n+highest_negative_power, m+1)
        A = sympy.zeros(m+1, n+highest_negative_power)
        B = sympy.zeros(n+highest_negative_power, n+highest_negative_power)
        for i in range(1, m+1):
            for j in range(min(i, n+highest_negative_power)):
                A[i, j] = -coefficients[i - j - 1]

        for i in range(n+highest_negative_power):
            for j in range(n+highest_negative_power):
                B[i, j] = -coefficients[m + i - j]
        
        S = sympy.Matrix([[I, A], [O, B]])
        if sympy.det(S) ==0:
            pass
        else:
            sol = S.LUsolve(b)
            a = sol[:m+1]
            b = sol[m+1:]

            return sum(a[i] * x**i for i in range(m+1)) / (x**(-highest_negative_power) + sum(b[i] * x**(i+1-highest_negative_power) for i in range(n+highest_negative_power)))
    
if __name__ == '__main__':
    x = sympy.symbols('x')
    f = sympy.sin(x)
    n = 3
    m = 3
    x0 = 0
    print(PadeApproximant(f, 3, 3, x, x0))
    print(PadeApproximant(sympy.exp(x)/x, 4, 4, x, x0))
    print(PadeApproximant(sympy.exp(x-1)/(x-1), 4, 4, x, 1))

    
    