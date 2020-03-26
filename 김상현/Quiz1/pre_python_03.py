"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
import random
player_num = int(input("주사위 게임에 오신 걸 환영합니다.\n 참여인원을 입력해주세요"))
player_dice_num = []
exist = -1
while exist != 1:
    for i in range(player_num):
        player_dice_num.append(0)
    for i in range(player_num):
        player_dice_num[i] = (random.randint(1, 6))
        print("{}번 플레이어의 주사위 값은 {}입니다.".format(i+1, player_dice_num[i]))
    exist = 0
    for i in range(len(player_dice_num)):
        if player_dice_num[i] == max(player_dice_num):
            exist += 1

    if exist >= 2:
        player_num = exist
        print("{}명의 동점자가 발생하였습니다. 동점자 간의 게임을 다시 실행합니다.".format(exist))
        player_dice_num = []

winner = player_dice_num.index(max(player_dice_num)) + 1

print("{}번 플레이어가 승리하였습니다.".format(winner))