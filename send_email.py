import smtplib

print ("wtf")

username = input("Enter your email username: ")
password = input("Enter your password: ")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(username, password)
server.sendmail(
  "dev.millerg09@gmail.com", 
  "millerg09@gmail.com", 
  "this message is from python")
server.quit()