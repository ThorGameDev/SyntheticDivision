import cmath


def sd(coefficients, left_side):
    dropdown = []
    side = 0
    for co in coefficients:
        lower = co + side
        dropdown.append(lower)
        side = lower * left_side
    return dropdown


def factor(num):
    factors = []
    for i in range(num + 1):
        if i == 0:
            continue
        if num % i == 0:
            factors.append(i)
    if len(factors) == 0:
        return [1]
    return factors


def possible_rational_roots(a, C):
    if a < 0:
        a = -a
    if C < 0:
        C = -C
    possible = []
    a_fac = factor(a)
    C_fac = factor(C)
    for i in a_fac:
        for j in C_fac:
            possible.append(j / i)
            possible.append(-j / i)
    return possible


def check_roots(coefficients):
    possible = possible_rational_roots(coefficients[0], coefficients[-1])
    results = []
    for i in possible:
        if sd(coefficients, i)[-1] == 0:
            results.append(i)
    return list(set(results))


def quadratic_formula(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    left = -b
    inner = b * b - 4 * a * c
    right = cmath.sqrt(inner)
    bottom = 2 * a
    if right.real.is_integer() and right.imag.is_integer():
        return f"(x+{-((left-right)/bottom)})(x+{-((left+right)/bottom)})"
    else:
        return f"(x+({left}-sqrt({inner}))/{bottom})(x+({left}+sqrt({inner}))/{bottom})"


def simplify_and_factor(coefficients):
    roots = check_roots(coefficients)
    factored = ""
    for root in roots:
        coefficients = sd(coefficients, root)
        if coefficients.__len__() > 0:
            coefficients.pop(-1)
        factored += f"(x+{-root})"
    if len(coefficients) == 3:
        factored += quadratic_formula(coefficients)
    elif len(coefficients) > 0:
        factored += f"{coefficients}"

    return factored


print(simplify_and_factor([5,19,-4]))
print(simplify_and_factor([5,-17,6]))
