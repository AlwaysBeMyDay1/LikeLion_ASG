import random

for x in range(30):
    print(random.choice(["된장찌개", "피자", "제육볶음"]))
    break

info = {"사는곳":"서울", "취미":"피아노", "좋아하는 음식":"된장찌개"}

print(info.get("사는곳"))