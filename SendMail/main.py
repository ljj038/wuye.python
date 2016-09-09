#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import mysendmail
import htmlLoader
import urlManager
import htmlParser


class Main:
    def __init__(self):
        self.smtp = mysendmail.MyMail()
        self.htmlLoader = htmlLoader.HtmlLoader()
        self.urlManager = urlManager.UrlManager()
        self.htmlParser = htmlParser.HtmlParser()

    def excute(self, listReceiveUser):
        f = open("url", "r")
        for sUrl in f:
            # 删除 url 后的换行符
            sUrl = sUrl.strip()

            # 判断 url 是否被处理
            if (self.urlManager.isExixts(sUrl)):
                print "url [%s] is alreay exists" % sUrl
                continue

            # 获取 url 的内容
            sContent = self.htmlLoader.urlLoad(sUrl)
            if (sContent is None):
                print "get url content is none [%s]" % sUrl
                continue

            # 获取 title
            sTitle = self.htmlParser.parse(sContent)
            if (sContent is None):
                print "get url title is none [%s]" % sUrl
                continue

            # 发送邮件
            sSendContnt = '<h3 style="color=red;"><a href="%s">%s</a></h3>' % (sUrl, sTitle)
            # html 邮件
            # dictResult = self.smtp.senHtmlMail(listReceiveUser=listReceiveUser, sSubject=sTitle, sContent=sSendContnt)

            # 附件邮件
            dictResult = self.smtp.setMultMail(listReceiveUser=listReceiveUser, sSubject=sTitle, sContent=sSendContnt)
            if (dictResult['code'] == 200):
                # 保存已经处理过的 url
                self.urlManager.insert(2, sUrl)
                print "url [%s] title [%s] is ok" % (sUrl, sTitle)
        f.close()


if (__name__ == "__main__"):
    # listReceiveUser = ['53381435@qq.com', '150005932@qq.com']
    listReceiveUser = ['1280293909@qq.com', '791520450@qq.com']
    smtp = Main()
    smtp.excute(listReceiveUser)
