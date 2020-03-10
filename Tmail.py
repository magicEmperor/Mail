import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 配置smpt服务器
smtp_server = config.server_cfg.get('smpt_163')
# 发件人邮箱 收件人邮箱  发件人口令
sender = 'zyk18781278496@163.com'
receiver = '940040346@qq.com'
password = 'k132914'
# 创建邮件本身
msg = MIMEMultipart()
# 发件箱 收件箱 主题
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = '测试'
# 文本
part = MIMEText('乔装打扮，不择手段')
msg.attach(part)
# 音频
part = MIMEApplication(open('yin.mp3','rb').read())
part.add_header('Content-Disposition','attachment',filename='yin.mp3')
msg.attach(part)
# 图片
part = MIMEApplication(open('tu.jpg','rb').read())
part.add_header('Content-Disposition','attachment',filename = 'tu.jpg')
msg.attach(part)
# 表
part = MIMEApplication(open('biao.xlsx','rb').read())
part.add_header('Content-Disposition','attachment',filename = 'biao.xlsx')
msg.attach(part)
#pdf类型附件 
part = MIMEApplication(open('foo.pdf','rb').read()) 
part.add_header('Content-Disposition', 'attachment', filename="foo.pdf") 
msg.attach(part)


try:
    # 设置服务器及端口号
    server = smtplib.SMTP(smtp_server,25)
    # 登录发件箱
    server.login(sender,password)
    server.set_debuglevel(1)
    # 发送邮件
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()
    print('成功')
except Exception:
    print('失败')