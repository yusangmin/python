def hanoi_tower(height, from_pole, to_pole, temp_pole):
    if height >= 1:
        hanoi_tower(height-1,from_pole,temp_pole,to_pole)
        move_disk(from_pole,to_pole)
        hanoi_tower(height-1,temp_pole,to_pole,from_pole)

def move_disk(from_pole, to_pole):
    print(from_pole,"에서",to_pole, "로 디스크를 이동한다")

hanoi_tower(3,"A","B","C")
