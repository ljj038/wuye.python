#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class MyMail:
    def __init__(self):
        self.sSmtpHost = "smtp.163.com"
        self.sLoginUser = "zhao1280293909@163.com"
        self.sLoginPass = "YINGNAN211.DI"
        self.bDebugLevel = False

    def setSmtpHost(self, sSmtpHost):
        self.sSmtpHost = sSmtpHost

    def setLoginUser(self, sLoginUser):
        self.sLoginUser = sLoginUser

    def setLoginPass(self, sLoginPass):
        self.sLoginPass = sLoginPass

    def setDebugLevel(self, bIsDebug):
        self.bDebugLevel = bool(bIsDebug)

    def setMultMail(self, listReceiveUser, sSubject, sContent):
        if (len(listReceiveUser) == 0):
            return {"code": 0, "msg": "no content"}

        if (self.sSmtpHost is None):
            return {"code": 0, "msg": "smtp host is None"}

        if (self.sLoginUser is None or self.sLoginPass is None):
            return {"code": 0, "msg": "user or password is None"}

        if (sSubject is None or sContent is None):
            return {"code": 0,
                    "msg": "subject or content is None",
                    "data": {"subject": len(sSubject), "content": len(sContent)}
                    }

        sFromUser = "wuye<%s>" % self.sLoginUser  # 发件人
        sFileName1 = '1.JPG'
        sFileName2 = 'vim.png'

        # MIMEMultipart 我理解为附件的容器
        multMsg = MIMEMultipart()

        # 邮件内容部分(html)
        htmlMsg = MIMEText(_text=sContent, _subtype='html', _charset='utf-8')

        # 附件部分
        f = open(sFileName1, 'rb')
        imgMsg = MIMEApplication(f.read())
        imgMsg.add_header('Content-Disposition', 'attachment', filename=sFileName1)
        f.close()

        # 附件部分
        f = open(sFileName2, 'rb')
        imgMsg2 = MIMEApplication(f.read())
        imgMsg2.add_header('Content-Disposition', 'attachment', filename=sFileName2)
        f.close()

        # 将各个部分附加到容器中
        multMsg.attach(htmlMsg)
        multMsg.attach(imgMsg)
        multMsg.attach(imgMsg2)

        # 设置邮件的：标题/发件人/收件人
        multMsg["Subject"] = sSubject
        multMsg["From"] = sFromUser
        multMsg["To"] = ";".join(listReceiveUser)

        # 发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host=self.sSmtpHost)
            smtp.login(user=self.sLoginUser, password=self.sLoginPass)
            smtp.set_debuglevel(self.bDebugLevel)
            smtp.sendmail(from_addr=sFromUser, to_addrs=listReceiveUser, msg=multMsg.as_string())
            smtp.quit()
            return {"code": 200, "msg": "success"}
        except Exception as e:
            print(e)
        finally:
            smtp.close()

    def senHtmlMail(self, listReceiveUser, sSubject, sContent):
        if (len(listReceiveUser) == 0):
            return {"code": 0, "msg": "no content"}

        if (self.sSmtpHost is None):
            return {"code": 0, "msg": "smtp host is None"}

        if (self.sLoginUser is None or self.sLoginPass is None):
            return {"code": 0, "msg": "user or password is None"}

        if (sSubject is None or sContent is None):
            return {"code": 0,
                    "msg": "subject or content is None",
                    "data": {"subject": len(sSubject), "content": len(sContent)}
                    }

        sFromUser = "wuye<%s>" % self.sLoginUser  # 发件人

        # html
        objMimeText = MIMEText(_text=sContent, _subtype='html', _charset='utf-8')
        objMimeText['Subject'] = sSubject
        objMimeText['From'] = sFromUser
        objMimeText['To'] = ";".join(listReceiveUser)
        # print(objMimeText)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(host=self.sSmtpHost)
            smtp.login(user=self.sLoginUser, password=self.sLoginPass)
            smtp.set_debuglevel(self.bDebugLevel)
            smtp.sendmail(from_addr=sFromUser, to_addrs=listReceiveUser, msg=objMimeText.as_string())
            smtp.quit()
            return {"code": 200, "msg": "success"}
        except Exception as e:
            print(e)
        finally:
            smtp.close()

