#!/usr/bin/python3

def toom_cook_recursive(x, y, k):
    # convert to string for easier manipulation of digits
    x_str = str(x)
    y_str = str(y)

    # base case
    if len(x_str) == 1 or len(y_str) == 1:
        return int(x) * int(y)

    # find the maximum length between x and y
    n = max(len(x_str), len(y_str))

    # pad zeros to make the length of x and y the same
    if n % k != 0:
        n += k - (n % k)
    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    # split x and y into parts
    part_size = n // k
    x_parts = [x_str[i*part_size:(i+1)*part_size] for i in range(k)]
    y_parts = [y_str[i*part_size:(i+1)*part_size] for i in range(k)]

    # calculate the intermediate values
    a = [int(x_parts[i]) for i in range(k)]
    b = [int(y_parts[i]) for i in range(k)]
    m = k + 1
    r = [0] * (2*k - 1)
    for i in range(k):
        for j in range(k):
            r[i+j] += a[i] * b[j]
    v = [0] * m
    for i in range(m):
        v[i] = sum(r[j] * pow(i, j) for j in range(2*k - 1))

    # solve the system of linear equations to get the coefficients of the product polynomial
    A = [[pow(i, j) for j in range(m)] for i in range(m)]
    coeffs = [0] * m
    for i in range(m):
        # Gaussian elimination
        for j in range(i+1, m):
            factor = A[j][i] // A[i][i]
            for k in range(i, m):
                A[j][k] -= factor * A[i][k]
            v[j] -= factor * v[i]
        # back substitution
        coeffs[m-1-i] = v[m-1-i] // A[m-1-i][m-1-i]
        for j in range(i+1, m):
            v[j] -= coeffs[m-1-i] * A[j][m-1-i]

    # evaluate the product polynomial at x = 10^(part_size)
    result = 0
    base = 10**part_size
    for i in range(m):
        result += coeffs[i] * pow(base, i)

    return result

# 예제 코드 실행
a = 123456
b = 789123
c = toom_cook_recursive(a, b, 3)
print(c)