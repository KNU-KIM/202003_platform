"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""
levelList = ["F", "D", "C", "B", "A"]
score = int(input("당신의 점수를 입력하세요(0~100): "))
if score == 0:
    score = 1
grade = levelList[(score-1)//20]

print("당신의 학점은 {}입니다.".format(grade))