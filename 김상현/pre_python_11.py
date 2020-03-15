"""11. 최대공약수를 구하는 함수를 구현하시오"""


def maxCD(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a


print(maxCD(110, 33))