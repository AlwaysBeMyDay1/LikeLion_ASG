from googletrans import Translator

translator = Translator()

while True:
    sentence = input("번역할 문장을 입력하세요. >> ")
    dest = input("1 - 한국어, 2 - 영어, 3 - 중국어, 4 - 독일어, 5 - 프랑스어, 6 - 스페인어\n번역을 원하는 언어의 번호를 입력하세요. >> ")
    if dest == "1" : dest = "kr"
    elif dest == "2" : dest = 'en'
    elif dest == "3" : dest = "zh-CN"
    elif dest == "4" : dest = "de"
    elif dest == "5" : dest = "fr"
    elif dest == "6" : dest = "es"
    detected = translator.detect(sentence)
    result = translator.translate(sentence,dest)
    
    print("================= 번역 결과 =================")
    print(f"{detected.lang} : {sentence}")
    print(f"{result.dest} : {result.text}")
    print("=============================================")
    print("\n")