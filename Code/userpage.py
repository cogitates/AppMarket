from tkinter import simpledialog
from tkinter import *  
import numpy as np
from tkinter import *  
from tkinter.messagebox import *  

import pymysql
 

class FirstFrame(Frame): #首页
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()
        self.rating = IntVar()


    def createPage(self):
        self.page = Frame(self.root) #创建Frame  
        
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute('select * from user_view')
        t = np.array(cur.fetchall())

        Label(self,text='应用ID').grid(row=1,column=0)
        Label(self,text='名字').grid(row=1,column=1)
        Label(self,text='功能').grid(row=1,column=2)
        Label(self,text='开发者').grid(row=1,column=3)
        Label(self,text='下载\更新').grid(row =1, column=4)
        Label(self,text='评价').grid(row =1, column=5)
        # Label(self,text='评论').grid(row =1, column=6)
        # print(t)
        x = 0
        # print(t[0],t[1])
        for i in t:
            print(i,i[0],type(i[0]))
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)
            Label(self,text='{0}'.format(i[3])).grid(row=x+2,column=3)

            Button(self,text='下载\更新',command = self.Download).grid(row = x+2,column=4)
            Button(self,text='评价',command = lambda:self.Rating(i[0])).grid(row = x+2,column=5)
            # Button(self,text='评论').grid(row = x+2,column=6)
            x=x+1

    def Download(self):
        showinfo(title='下载提醒：', message='下载\更新即将开始，请耐心等待，感谢您的使用！')

    def Rating(self,appid):
        # self.appid =simpledialog.askinteger(title='应用ID',prompt='请确定您评论应用的ＩＤ')
        self.rating =simpledialog.askinteger(title='评分',prompt='请评分（１－５分）')
        self.comment =simpledialog.askstring(title='评语',prompt='请评论')
        appid = int(appid)
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()

        cur.execute('select * from commenttable order by commentid desc limit 1')
        t = np.array(cur.fetchall())
        print(t,t[0],t[0][0])
        signal=askyesno(title="提示",message="您是否确定提交评论")
        if signal:
            cur.execute('insert into commenttable values(%s,%s ,%s ,%s)', (int(t[0][0])+1, appid,self.rating,self.comment))
            showinfo("提示","评论已经提交！")
        # print(self.rating)
        conn.commit()
        cur.close()
        

class QueryFrame(Frame): # 查询类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.kw = StringVar()  
        self.createPage()  
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)  
        Label(self, text = '应用名称: ').grid(row=1, stick=W, pady=10)  
        Entry(self, textvariable=self.kw).grid(row=1, column=1, stick=E) 
        Button(self, text='查询', command=self.check).grid(row=1, column=3, stick=E, pady=10) 
        Label(self).grid(row=2, stick=W, pady=10)  

    def check(self):
        kw = self.kw.get()
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()

        cur.execute('select appname from insideapp')
        if (kw, ) in cur.fetchall():
            cur.execute("select * from insideapp where appname=%s", kw)
            text = Text(self, width=16, height=6)
            text.grid(row=5, column=1) 
            result = cur.fetchall()
            text.insert(1.0, '应用编号：{}'.format(result[0][0]))
            text.insert(2.0, '\n应用名称：{}'.format(result[0][1]))
            text.insert(3.0, '\n应用描述：{}'.format(result[0][2]))
            text.insert(4.0, '\n开发者：{}'.format(result[0][3]))
            Button(self, text='下载', command=self.Download).grid(row=5, column=3, stick=E, pady=10)

        else:
            showinfo(title='无记录', message='找不到该应用信息！') 

        conn.commit()
        cur.close() 
        
    def Download(self):
        showinfo(title='下载\更新提醒：', message='下载\更新即将开始，请耐心等待，感谢您的使用！')

class AboutFrame(Frame): # 关于类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
  
    def createPage(self):  
        Label(self, text='\n\n\n数据库课程设计\n\n安卓应用市场\n\n使用 Python 开发\n', fg = 'red', 
            compound = 'center', font = ("Arial, 17")).pack()  
        # showinfo(title = '提示', message="请完善您的用户名信息")
        Button(self,text="注销",command=self.ExitUser).pack()
    
    def ExitUser(self):
        
        self.quit()
        # LoginPage(root)


class UserPage(object):  # 用户页类
    def __init__( self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (600, 600)) #设置窗口大小  
        self.createPage()  
        print(self.root,type(self.root))
    def createPage(self):  
        self.queryPage = QueryFrame(self.root)  
        self.aboutPage = AboutFrame(self.root)
        self.firstPage = FirstFrame(self.root)  
        self.firstPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='首页', command = self.firstpage)
        menubar.add_command(label='查询', command = self.queryData)  
        menubar.add_command(label='关于', command = self.aboutDisp)  
        
        self.root['menu'] = menubar  # 设置菜单栏  
  
  
    def queryData(self):  
        self.queryPage.pack()  
        self.aboutPage.pack_forget()  
        self.firstPage.pack_forget()
    
    def aboutDisp(self):  
        self.queryPage.pack_forget()  
        self.aboutPage.pack()  
        self.firstPage.pack_forget()
    
    def firstpage(self):
        self.queryPage.pack_forget()
        self.aboutPage.pack_forget()
        self.firstPage.pack()
  