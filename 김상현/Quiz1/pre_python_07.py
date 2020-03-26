"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오"""
i = 1
sum = 0
OverflowLevel = 1000
while sum < OverflowLevel :
    sum += i
    i += 1

print(sum)

print("{}을 넘게하는 수는 {}입니다.".format(OverflowLevel,i))