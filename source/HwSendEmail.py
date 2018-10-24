#!/usr/bin/env python
# coding:gbk

# Created by zhaohongwei on 2016-06-20
# Blog: http://blog.csdn.net/z_johnny

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
import os
import yaml

class HwSendEmail(object):
    def __init__(self, email_title, email_content):
        """
        init config
        """
        with open('./config/configEmail.yaml' ,'rb') as config:
            self.allConfig = yaml.load(config)
        self.attachment_path = './result'
        self.email_title = email_title
        self.email_content = email_content


        self.smtp = smtplib.SMTP()
        self.login_username = self.allConfig['SMTP']['login_username']
        self.login_password = self.allConfig['SMTP']['login_password']
        self.sender = self.allConfig['SMTP']['login_username']
        self.receiver = self.allConfig['SMTP']['receiver']
        self.host = self.allConfig['SMTP']['host']
        # self.port = self.allConfig['SMTP']['port']  发现加入端口后有时候发邮件出现延迟，故暂时取消

    def connect(self):
        """
        connect server
        """
        #self.smtp.connect(self.host, self.port)
        self.smtp.connect(self.host)

    def login(self):
        """
        login email
        """
        try:
            self.smtp.login(self.login_username, self.login_password)
        except:
            raise AttributeError('Can not login smtp!!!')

    def send(self):
        """
        send email
        """
        msg = MIMEMultipart()                   # create MIMEMultipart
        msg['From'] = self.sender              # sender
        receiver = self.receiver.split(",")     # split receiver to send more user
        msg['To'] = COMMASPACE.join(receiver)
        msg['Subject'] = self.email_title           # email Subject
        content = MIMEText(self.email_content, _charset='gbk')   # add email content  ,coding is gbk, becasue chinese exist
        msg.attach(content)

        for attachment_name in os.listdir(self.attachment_path):
            attachment_file = os.path.join(self.attachment_path,attachment_name)

            with open(attachment_file, 'rb') as attachment:
                if 'application' == 'text':
                    attachment = MIMEText(attachment.read(), _subtype='octet-stream', _charset='GB2312')
                elif 'application' == 'image':
                    attachment = MIMEImage(attachment.read(),  _subtype='octet-stream')
                elif 'application' == 'audio':
                    attachment = MIMEAudio(attachment.read(), _subtype='octet-stream')
                else:
                    attachment = MIMEApplication(attachment.read(), _subtype='octet-stream')

            attachment.add_header('Content-Disposition', 'attachment', filename = ('gbk', '', attachment_name))
            # make sure "attachment_name is chinese" right
            msg.attach(attachment)

        self.smtp.sendmail(self.sender, receiver, msg.as_string())    # format  msg.as_string()

    def quit(self):
        self.smtp.quit()

    def sendemail(self):
        self.connect()
        self.login()
        self.send()
        self.quit()

if __name__ == "__main__":
    # from sendemail import SendEmail
    import  time
    ISOTIMEFORMAT='_%Y-%m-%d_%A'
    current_time =str(time.strftime(ISOTIMEFORMAT))

    email_config_path = './configEmail.yaml'     # config path
    email_attachment_path = './result'                    # attachment path
    email_tiltle = 'johnny test'+'%s'%current_time       # as johnny test_2016-06-20_Monday ,it can choose only file when add time
    email_content = 'python发送邮件测试，包含附件'

    myemail = HwSendEmail(email_config_path,email_attachment_path,email_tiltle, email_content)
    myemail.connect()
    myemail.login()
    myemail.send()
    myemail.quit()
