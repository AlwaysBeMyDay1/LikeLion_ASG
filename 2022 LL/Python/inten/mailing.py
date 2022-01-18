import imp
import smtplib
from email.message import EmailMessage

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



# smtp 메일 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

# smtp 서버에 로그인
print(smtp.login("eodus0901@gmail.com","start2020!"))

# 메일 보내기
smtp.send_message(message)
smtp.quit()
print("완료")