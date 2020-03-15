"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""
maxStar = int(input("숫자를 입력하세요 : "))
for i in range(1, maxStar+1):
    # starString = " " * (maxStar-i)
    print("{}{}".format(" " * (maxStar-i), "★"*i))

for i in range(1, maxStar):
    print("{}{}".format(" " * i, "★" * (maxStar -i)))