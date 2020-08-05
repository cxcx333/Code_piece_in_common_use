import smtplib
from email.mime.text import MIMEText


def send_mail_from_163(msg, topic):
    """
    用fckccp@163.com给bfwpast@gmail.com发送一封邮件
    :param msg: 发送的邮件主体
    :param topic: 发送的邮件主题
    :return: 是否发送成功
    """
    try:
        # 连接163邮箱服务器
        mailserver = "smtp.163.com"
        # 163邮箱的端口号
        mailPort = 25
        # 163邮箱的用户名
        mailUsername = "fckccp@163.com"
        # 使用163邮箱的授权 密码
        mailPasswd = 'YTKPXXRKISOTASSV'
        # 接收方的邮件地址
        to_mail = "bfwpast@gmail.com"
        # 连接邮箱服务器,
        smtpServer = smtplib.SMTP(mailserver, mailPort)
        # 登陆邮箱服务器, 注意: 密码是邮箱的授权密码,    登陆前必须先授权
        smtpServer.login(mailUsername, mailPasswd)
        # 写邮件-发件人,收件人,内容
        # 创建MIMEtext(),并设置内容
        msg = MIMEText(msg)
        # 设置主题内容
        msg["Subject"] = topic
        msg["From"] = mailUsername
        msg["To"] = to_mail
        # 发送邮件
        smtpServer.sendmail(mailUsername, to_mail, msg.as_string())
        # 关闭连接
        smtpServer.close()
        return True
    except:
        return False
