import imp
import smtplib
from email.message import EmailMessage
import imghdr
import re


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

#MIME type 이메일 만들기
# 이메일 담을 통 만들기
message = EmailMessage()
# 통에 이메일 담기
message.set_content("코드라이언 수업중입니다.")
#이메일 header(제목, 송수신자) 설정
message["Subject"] = "제목!!!"
message["From"] = "eodus0901@gmail.com"
message["To"] = "eodus09011@naver.com"

# #이미지 파일 열기
# img = open("gandalf_with_macbook.jpg","rb")
# # 이미지 파일 읽어오기
# print(img.read())
# # 파일 열었으면 닫아줘야 함
# img.close()
with open("gandalf_with_macbook.jpg","rb") as img :
    img_file = img.read()

img_type = imghdr.what("gandalf_with_macbook",img_file)
message.add_attachment(img_file,maintype='image',subtype='')

# smtp 메일 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

# smtp 서버에 로그인
print(smtp.login("eodus0901@gmail.com","start2020!"))

#정규 표현식 사용
reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
re.match(reg,"")
# 메일 보내기
smtp.send_message(message)
smtp.quit()