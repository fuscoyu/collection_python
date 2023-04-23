# coding:utf-8

import json
import re
import urllib.request
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='649729384@qq.com'    # 发件人邮箱账号
my_pass = 'nmpgoglnzolhbcae'              # 发件人邮箱密码
my_user='820953610@qq.com'      # 收件人邮箱账号，我这边发送给自己

def mail(msg=''):
    text = '快快快 ！！！' + msg
    ret=True
    try:
        msg=MIMEText(text,'plain','utf-8')
        msg['From']=formataddr(["fosco",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["luqi",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="查询到物理老师的招聘信息"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret=False
    return ret

def gethtml(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

def parse_home_page(html):
    parttern = re.compile('<li.*?bmjx.*?<span>\n(.*?)<.*?lh_olistCatename.*?href=\"(.*?)\"\stitle=\"(.*?)\"', re.S)
    items = re.findall(parttern, html)
    data = []
    for info in items:
        data.append({
                'date': info[0].strip(),
                'detail_url': info[1],
                'title': info[2]
                }) 
    return sorted(data, key=lambda x:x["date"],reverse=True).pop()

# check physical fields in the details page
def check_physical_fields_in_the_details_page(html):
    parttern = re.compile('物理', re.S)
    items = re.findall(parttern, html)
    if items:
        return True
    return False



url = 'http://www.offcn.com/jiaoshi/zhaopin/2240/xian/'
# http://www.offcn.com/jiaoshi/zhaopin/2240/xian/

# 中文字符
home_html = gethtml(url)
home_data = parse_home_page(home_html)
detail_html = gethtml(home_data['detail_url'])
detail_data = check_physical_fields_in_the_details_page(detail_html)
if detail_data:
    print(home_data['detail_url']) 
    ret = mail(msg=home_data['detail_url'])

    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
