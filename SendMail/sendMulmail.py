#!/usr/bin/env python
# coding=utf-8
# 测试发送带附件的邮件
__author__ = 'zhaoyingnan'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sSmtpHost = "smtp.163.com"
sLoginUser = "*****"
sLoginPass = "*****"
listReceiveUser = ['*****@qq.com', '*****@qq.com']
sTitle = "你好zhaoyn"
sContent = '<h3><a href="http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html">python发送各类邮件的主要方法</a></h3>'

# 附件的容器
multMsg = MIMEMultipart()

# 内容部分（html）
htmlMsg = MIMEText(_text=sContent, _subtype='html', _charset='utf-8')

# 附件部分
sFileName = '1.JPG'
f = open(sFileName, 'rb')
imgMsg = MIMEApplication(f.read())
imgMsg.add_header('Content-Disposition', 'attachment', filename=sFileName)
f.close()

# 将各个部分附加到容器中
multMsg.attach(htmlMsg)
multMsg.attach(imgMsg)

multMsg["Subject"] = sTitle
multMsg["From"] = sLoginUser
multMsg["To"] = ";".join(listReceiveUser)

smtp = smtplib.SMTP()
smtp.connect(host=sSmtpHost)
smtp.login(user=sLoginUser, password=sLoginPass)
smtp.set_debuglevel(True)
smtp.sendmail(from_addr=sLoginUser, to_addrs=listReceiveUser, msg=multMsg.as_string())
smtp.quit()
