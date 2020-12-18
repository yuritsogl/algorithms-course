def karatsuba(num1: int, num2: int):
    n = check_if_even(max(num1,num2))
    a, b = split(num1, n)
    c, d = split(num2, n)
    z1 = multi(a, c)
    z2 = multi(b, d)
    gauss_trick = multi(a + b, c + d)
    z3 = gauss_trick - z1 - z2
    return int((10**n)*z1 + 10**(n//2)*z3 + z2)


def check_if_even(num) -> int:
    if len(str(num)) % 2 == 0:
        return len(str(num))
    else:
        return len(str(num)) - 1


def split(number: int, digits: int) -> int:
    if (number >= 10):
        mid = digits//2
        return(number // (10**mid), number % (10**mid))
    else:
        return (number // 10, number % 10)


def multi(x: int, y: int) -> int:
    if (x < 10 or y < 10):  # base case
        return x * y
    else:
        return karatsuba(x, y)


if __name__ == "__main__":
    # test cases
    assert karatsuba(1234, 5678) == 1234*5678
    assert karatsuba(10, 2) == 10*2
    assert karatsuba(1, 1) == 1*1
    assert karatsuba(111, 222) == 111*222
    assert karatsuba(109204597, 112812353) == 109204597*112812353
    assert karatsuba(1111111110, 2222222223) == 1111111110*2222222223
    assert karatsuba(1234, 45) == 1234*45
    assert karatsuba(387, 1153) == 387*1153
    assert karatsuba(2345679, 234) == 2345679*234
    assert karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == 3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627
    # The answer to the exercise
    print("The answer is:", karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
