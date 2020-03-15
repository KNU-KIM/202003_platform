""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""
num_1 = int(input("첫번째 수를 입력해주세요"))
num_2 = int(input("두번째 수를 입력해주세요"))
operator = input("연산자(+, -, *, /)를 입력해주세요")

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
else:
    print("수행할 수 없습니다.")
