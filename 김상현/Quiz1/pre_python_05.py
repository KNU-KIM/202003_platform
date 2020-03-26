"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
nDan = int(input("몇단을 출력하시겠습니까?: "))
for i in range(1, 10):
    print("{} * {} = {}".format(nDan, i, nDan*i))