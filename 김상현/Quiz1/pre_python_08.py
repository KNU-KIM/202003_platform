"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오"""
inputNumber = int(input("판별을 원하는 '정수'를 입력해주세요: "))
if inputNumber % 2 == 0:
    print("{}(은)는 짝수입니다.".format(inputNumber))
else :
    print("{}(은)는 홀수입니다.".format(inputNumber))