"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""
Word = input("변환을 원하는 영단어를 입력하세요: ")
check=0
list_word = list(Word)

for i in range(len(list_word)):
    if str.isalpha(list_word[i]):
        if str.isupper(list_word[i]):
            list_word[i] = list_word[i].lower()
        elif str.islower(list_word[i]):
            list_word[i] = list_word[i].upper()
        else:
            print("입력 형식이 잘못되었습니다.")
            check += 1
            break
    elif list_word[i] == " " or list_word[i].isnumeric():
        pass
    else:
        print("입력 형식이 잘못되었습니다.")
        check += 1
        break


if check == 0:
    print(''.join(list_word))
else:
    pass