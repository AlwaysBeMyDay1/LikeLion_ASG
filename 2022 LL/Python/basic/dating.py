q_and_a = []

while True:
    question = input("상대에게 알려주고 싶은 질문을 입력해주세요. (q 입력하면 답변 화면으로 이동.) >> ")
    if question == "q":
        break
    elif question == "":
        print("질문을 입력해주세요.")
    else:
        q_and_a.append({"질문": question, "답변": ""})

for index, item in enumerate(q_and_a):
    print(index+1,"번 질문 :", item["질문"])
    answer = input("답변을 입력하세요. >> ")
    item["답변"] = answer

print(q_and_a)
