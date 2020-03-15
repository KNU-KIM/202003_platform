"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""


def factoral(number):
    if number == 0:
        return 1

    return factoral(number-1) * number


print(factoral(4))