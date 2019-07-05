from tkinter import *  
import numpy as np
from tkinter import *  
from tkinter.messagebox import *  
from tkinter import simpledialog
import pymysql
 
class FirstFrame(Frame): #首页
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


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
        cur.execute('select * from insideapp')
        t = np.array(cur.fetchall())

        Label(self,text='应用ID').grid(row=1,column=0)
        Label(self,text='名字').grid(row=1,column=1)
        Label(self,text='功能').grid(row=1,column=2)
        Label(self,text='开发者').grid(row=1,column=3)
        Label(self,text='下架').grid(row =1, column=4)
        
        # print(t)
        x = 0
        # print(t[0],t[1])
        for i in t:
            print(i)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)
            Label(self,text='{0}'.format(i[3])).grid(row=x+2,column=3)

            Button(self,text='下架',command=lambda i=i:self.GetOff(i[0])).grid(row = x+2,column=4)
            
            x=x+1
        conn.commit()
        cur.close() 
    def GetOff(self,appid):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()
        appid = int(appid)
        cur.execute('select * from insideapp where insideappid=%s',(appid))
        t = np.array(cur.fetchall())
        print(t,appid,type(appid))
        # showwarning(title="警告",message="您是否决定下架此应用？")
        signal = askyesno("提示","您是否要下架此应用？")
        # cur.execute('delete from user where userid=4')
        if signal:
            cur.execute('SET FOREIGN_KEY_CHECKS=0')
            cur.execute('delete from insideapp where insideappid=%s',(appid))
            showinfo(title="提示",message="此应用已经下架")
            cur.execute('SET FOREIGN_KEY_CHECKS=1')
            cur.execute('insert into outsideapp values(%s,%s,%s,%s)',(int(t[0][0]),t[0][1],t[0][2],int(t[0][3])))
        conn.commit()
        cur.close() 

class UsermanageFrame(Frame): #用户管理
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


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
        cur.execute('select * from user')
        t = np.array(cur.fetchall())

        Label(self,text='用户ID').grid(row=1,column=0)
        Label(self,text='用户名').grid(row=1,column=1)
        Label(self,text='用户密码').grid(row=1,column=2)

        
        Label(self,text='移除').grid(row =1, column=5)

        x = 0
        for i in t:
            print(i)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)

            Button(self,text='移除',command=lambda i=i:self.RemoveUser(i[0])).grid(row = x+2,column=5)
            x=x+1

        conn.commit()
        cur.close() 
    def RemoveUser(self,userid):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()
        appid = int(userid)
        cur.execute('select * from user where userid=%s',(userid))
        t = np.array(cur.fetchall())
        print(t,appid,type(appid))
        # showwarning(title="警告",message="您是否决定下架此应用？")
        signal = askyesno("提示","您是否要移除该用户？")
        # cur.execute('delete from user where userid=4')
        if signal:
            cur.execute('delete from user where userid=%s',(userid))
            showinfo(title="提示",message="此用户已经被删除")
        conn.commit()
        cur.close() 

class DevelopermanageFrame(Frame): #开发者管理
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


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
        cur.execute('select * from developer')
        t = np.array(cur.fetchall())

        Label(self,text='开发者ID').grid(row=1,column=0)
        Label(self,text='开发者名字').grid(row=1,column=1)
        Label(self,text='开发者密码').grid(row=1,column=2)

        Label(self,text='移除').grid(row =1, column=5)

        x = 0

        for i in t:
            print(i)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)

            Button(self,text='移除',command=lambda i=i:self.RemoveDeveloper(i[0])).grid(row = x+2,column=5)
            x=x+1

    def RemoveDeveloper(self,developerid):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()
        appid = int(developerid)
        signal = askyesno("提示","您是否要移除该开发者？这将导致该用户的所有应用和应用评论从数据库中删除！！")
        if signal:
            cur.execute('SET FOREIGN_KEY_CHECKS=0')
            cur.execute('delete from developer where developerid=%s',(developerid))
            cur.execute('SET FOREIGN_KEY_CHECKS=1')
            showinfo(title="提示",message="此开发者已经被删除")
        conn.commit()
        cur.close() 
class AppCheckFrame(Frame): #app审核
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


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
        cur.execute('select * from outsideapp')
        t = np.array(cur.fetchall())

        Label(self,text='应用ID').grid(row=1,column=0)
        Label(self,text='名字').grid(row=1,column=1)
        Label(self,text='功能').grid(row=1,column=2)
        Label(self,text='开发者').grid(row=1,column=3)
        Label(self,text='意见').grid(row =1, column=4)
        Label(self,text='反馈').grid(row =1, column=5)
        # print(t)
        x = 0
        # print(t[0],t[1])
        for i in t:
            print(i)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)
            Label(self,text='{0}'.format(i[3])).grid(row=x+2,column=3)

            Button(self,text='允许',command=lambda i=i:self.GetUp(i[0])).grid(row = x+2,column=4)
            Button(self,text='反馈',command=lambda i=i:self.FeedBack(i[0])).grid(row = x+2,column=5)
            x=x+1
    def GetUp(self,appid):
            conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='2333',
                database="appmarket",
                charset='utf8'
            )
            cur = conn.cursor()
            appid = int(appid)
            cur.execute('select * from outsideapp where outsideappid=%s',(appid))
            t = np.array(cur.fetchall())
            print(t,appid,type(appid))
            # showwarning(title="警告",message="您是否决定下架此应用？")
            signal = askyesno("提示","您是否要上架该应用？")
            if signal:
                cur.execute('delete from outsideapp where outsideappid=%s',(appid))
                cur.execute('select * from insideapp order by insideappid desc limit 1')
                squeeze = np.array(cur.fetchall())
                print(t,t[0],t[0][0])
                print(squeeze[0][0],type(squeeze[0][0]))
                cur.execute('insert into insideapp values(%s,%s ,%s ,%s)', (int(squeeze[0][0])+1,t[0][1],t[0][2],t[0][3]))
                showinfo(title="提示",message="此应用已经上架")
                
            conn.commit()
            cur.close() 
    def FeedBack(self,appid):
        # self.appid =simpledialog.askinteger(title='应用ID',prompt='请确定您评论应用的ＩＤ')
        self.rating =simpledialog.askstring(title='反馈',prompt='请给出您的反馈意见')
        
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

        cur.execute('select * from feedback order by feedbackid desc limit 1')
        t = np.array(cur.fetchall())
        print(t,t[0],t[0][0])
        signal=askyesno(title="提示",message="您是否确定提交评论")
        if signal:
            cur.execute('insert into feedback values(%s,%s ,%s)', (int(t[0][0])+1, appid,self.rating))
        showinfo("提示","反馈已经提交！")
        # print(self.rating)
        conn.commit()
        cur.close()

class ManagerPage(object):  
    
    def __init__( self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (600, 600)) #设置窗口大小  
        self.CreatePage()  
  
    def CreatePage(self):  
        self.usermanagePage = UsermanageFrame(self.root)
        self.developermanagePage = DevelopermanageFrame(self.root)  
        self.checkPage = AppCheckFrame(self.root)
        self.firstPage = FirstFrame(self.root)
        self.systemmanagePage = SystemFrame(self.root)
        self.firstPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='应用管理', command = self.First)  
        menubar.add_command(label='应用审核', command = self.appCheck)  
        menubar.add_command(label='用户管理', command = self.usermanage)  
        menubar.add_command(label='开发者管理', command = self.developermanage)  
        menubar.add_command(label='系统概况', command = self.systemmanage)  
        self.root['menu'] = menubar  # 设置菜单栏  
  
  

    def appCheck(self):  
        self.checkPage.pack()
        self.firstPage.pack_forget()
        self.usermanagePage.pack_forget()
        self.developermanagePage.pack_forget()  
        self.systemmanagePage.pack_forget()
    def First(self):
        self.checkPage.pack_forget()
        self.firstPage.pack()
        self.usermanagePage.pack_forget()
        self.developermanagePage.pack_forget() 
        self.systemmanagePage.pack_forget()   
    def usermanage(self):
        self.checkPage.pack_forget()
        self.firstPage.pack_forget()
        self.usermanagePage.pack()
        self.developermanagePage.pack_forget()
        self.systemmanagePage.pack_forget()
    def developermanage(self):
        self.checkPage.pack_forget()
        self.firstPage.pack_forget()
        self.usermanagePage.pack_forget()
        self.developermanagePage.pack()
        self.systemmanagePage.pack_forget()
    def systemmanage(self):
        self.checkPage.pack_forget()
        self.firstPage.pack_forget()
        self.usermanagePage.pack_forget()
        self.developermanagePage.pack_forget()
        self.systemmanagePage.pack()
   

class SystemFrame(Frame): #首页
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


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
        # cur.execute('call return_sum')
        t = [1,2,3,4]
        row = cur.callproc("return_sum",(1,2,3,4))
        effect_row = cur.execute('select @_return_sum_0,@_return_sum_1,@_return_sum_2,@_return_sum_3')
        result = cur.fetchone()
        print(result)
        m1 = result[0]
        m2 = result[1]
        m3 = result[2]
        m4 = result[3]

        Label(self,text='上架应用数',font=("黑体",20)).grid(row=1,column=1,stick=W, pady=10)
        Label(self,text='待定应用数',font=("黑体",20)).grid(row=3,column=1,stick=W, pady=10)
        Label(self,text='开发者人数',font=("黑体",20)).grid(row=5,column=1,stick=W, pady=10)
        Label(self,text='用户人数',font=("黑体",20)).grid(row=7,column=1,stick=W, pady=10)
        Label(self,text='{}'.format(m1),font=("黑体",20)).grid(row=1,column=5,stick=W, pady=10)
        Label(self,text='{}'.format(m2),font=("黑体",20)).grid(row=3,column=5,stick=W, pady=10)
        Label(self,text='{}'.format(m3),font=("黑体",20)).grid(row=5,column=5,stick=W, pady=10)
        Label(self,text='{}'.format(m4),font=("黑体",20)).grid(row=7,column=5,stick=W, pady=10)
        Button(self,text='退出',command=self.quit).grid(row=9,column=1,stick=W, pady=10)
        
        conn.commit()
        cur.close() 