"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """
idCode = input("주민등록번호를 입력해주세요: ")

if idCode[6].isnumeric():
    D_Number = int(idCode[6])
    if D_Number == 1 or D_Number == 3:
        print("남자입니다.")
    elif D_Number == 2 or D_Number == 4:
        print("여자입니다.")
else:
    D_Number = int(idCode[7])
    if D_Number == 1 or D_Number == 3:
        print("남자입니다.")
    elif D_Number == 2 or D_Number == 4:
        print("여자입니다.")

