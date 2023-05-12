#!/usr/bin/python3

def karatsuba(x, y):
    # convert to string for easier manipulation of digits
    x_str = str(x)
    y_str = str(y)

    # base case
    if len(x_str) == 1 or len(y_str) == 1:
        return x * y

    # find the maximum length between x and y
    n = max(len(x_str), len(y_str))

    # split x and y into two parts
    mid = n // 2
    a = int(x_str[:-mid]) if len(x_str[:-mid]) > 0 else 0
    b = int(x_str[-mid:])
    c = int(y_str[:-mid]) if len(y_str[:-mid]) > 0 else 0
    d = int(y_str[-mid:])

    # recursive calls to karatsuba algorithm
    ac = karatsuba(a, c)
    print(ac)
    bd = karatsuba(b, d)
    print(bd)
    ad_bc = karatsuba(a+b, c+d) - ac - bd
    print(ad_bc)
    # combine results
    return (ac * 10**(2*mid)) + (ad_bc * 10**mid) + bd

    # 예제 코드 실행
a = 12
b = 34
c = karatsuba(a, b)
print(c)