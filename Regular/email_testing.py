# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os
# import math
#
#
# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.login('stu.ecell@gmail.com', 'ouiqixvqwvmdgbjz')
#
# msg = MIMEMultipart()
# subject="FEEDBACK FORM"
# msg['Subject'] = subject
#
# t='Hello Participant,'+'\n'+'Thank you for registering for the event. Please find the enclosed webinar link in this email. Hoping to you there soon. '+'\n'+'Thanking you.'+'\n'+'Link: https://us02web.zoom.us/j/3678804732'+'\n'+'Meeting ID: 367 880 4732'+'\n'+'Yours sincerely'+'\n'+'Team E-Cell'
# text='Hello ,'+'\n'+'\n'+' We from team E-Cell, are hear to know your views on the webinar conducted on 25-06-2022 (i.e)IMPACT LECTURE SERIES 2022-2023 we promise you that either good or bad we will  view from your point and also a part in enhancing our performance we request you to fill the feedback from '+'\n'+'\n'+'Link: https://forms.gle/48NS1jRUd9HoXeDBA'+'\n'+'\n'+'Thanking you'+'\n'+'\n'+'Team E-Cell'
# print(text)
# msg.attach(MIMEText(text))
#
# mail = []
#
#
# k=0
# m=['saikiranreddyappidi123@gmail.com']
# for i in mail:
#     k=int(k+1)
#     smtp.sendmail(from_addr="stu.ecell@gmai.com", to_addrs=i, msg=msg.as_string())
#     print(k," Mail sent:",i)
#
# smtp.quit()
#
#
# """import random
# import math
#
# def hi():
#     return 10,20
# l=int(18)
# nl=int(15)
# pl=(9)
# l=int(l*l + math.sin(math.sqrt(l))+math.ceil(math.sqrt(l))+math.pi)
# nl=int(l*l + math.cos(math.sqrt(nl))+math.ceil(math.sqrt(nl))+math.pi)
# pl=int(l*l + math.tan(math.sqrt(pl))+math.floor(math.sqrt(pl))+math.pi)
# otp=l+nl+pl+min(l,nl,pl)
# print(l,nl,pl)
# otp+=random.randint(l,pl)
# otp=str(otp)
#
# print(otp)
# print(random.randint(1,20))
#
# a=hi()
# print(a,type(a))
#
# mail = ['sivaramsiva6197@gmail.com',
# 'papasaniprasanna9490@gmail.com',
# 'venkateshdande8004@gmail.com',
# 'Preethikundan@gmail.com',
# 'charvi.varma19@gmail.com',
# 'arcda88@gmail.com',
# 'tumatisumasri@gmail.com',
# 'sureshbabudevi.p@gmail.com',
# 'doctorsundaresan@gmail.com',
# 'indusreeramachandruni@gmail.com',
# 'dayyamprasad6@gmail.com',
# 'srinijakasthala@gmail.com',
# 'anuchowdary2003@gmail.com',
# 'chinnirenna9@gmail.com',
# 'chandrasekhararao.vullikanti@gmail.com',
# 'satyamohankrishna2003@gmail.com',
# 'sirigirivenkatasaibharath@gmail.com',
# 'brexample99@gmail.com',
# 'seelamvarshareddyvarshareddy@gmail.com']
#
#
# mail='Hello ,'+'\n'+'We from team E-Cell, are hear to know your views on the webinar conducted on 25-06-2022 (i.e)IMPACT LECTURE SERIES 2022-2023 we promise you that either good or bad we will  view from your point and also a part in enhancing our performance we request you to fill the feedback from'+'\n'+'Link: https://forms.gle/48NS1jRUd9HoXeDBA'+'\n'+'Thanking you'+'\n'+'Team E-Cell'
#
# print(mail)"""
# import numpy
# print(numpy.__version__)
# try:
#     i = 1
#     print(i)
# except(i==0):
#     print("hello")

