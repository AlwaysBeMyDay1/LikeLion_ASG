import random

menu = ["초밥", "된장찌개", "김치찜"]

while True:
    order = input("동작에 따른 번호를 입력하세요.\n(1 : 메뉴 추가, 2 : 메뉴 삭제, 3 : 랜덤 출력, 4 : 종료) >> ")
    if order == "1":
        print(menu)
        add_menu = input("추가할 메뉴의 이름을 입력해주세요 >> ")
        menu.append(add_menu)
        print(menu)
    elif order == "2":
        print(menu)
        remove_menu = input("삭제할 메뉴의 이름을 입력해주세요 >> ")
        menu = list(set(menu)-set([remove_menu]))
        print(menu)
    elif order =="3" :
        print("오늘의 추천 메뉴는 " + random.choice(menu) + "입니다")
    elif order == "4":
        print("메뉴 추천 프로그램이 종료됩니다.")
        break
    else:
        print("올바른 번호를 입력해주세요.")




note = ["주원","나원","민솔"]