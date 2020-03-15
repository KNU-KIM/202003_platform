"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""
for i in range(1, 100 + 1):
    NtoS = list(str(i))
    Dist = 0
    if i % 5 == 0:
        Dist += 1
    if '3' in NtoS:
        Dist += 2
    elif '6' in NtoS:
        Dist += 2
    elif '9' in NtoS:
        Dist += 2

    if Dist == 0: print(i)
    elif Dist == 1: print("아자")
    elif Dist == 2: print("짝")
    else : print("짜악자")