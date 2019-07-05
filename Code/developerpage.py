from tkinter import *  
import numpy as np
from tkinter import *  
from tkinter import simpledialog
from tkinter.messagebox import *  
import pymysql
# from main import user
class InsideappFrame(Frame):
      
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.developerid = IntVar()
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
        self.developerid =simpledialog.askinteger(title="提示",prompt="请确定您的个人信息，输入您的开发者ID")
        cur = conn.cursor()
        cur.execute('select * from insideapp where developerid=%s',(self.developerid))
        t = np.array(cur.fetchall())
        print(t)
        Label(self,text='已上架应用',font=("黑体",16)).grid(row=0)
        Label(self,text='应用ID').grid(row=1,column=0)
        Label(self,text='名字').grid(row=1,column=1)
        Label(self,text='功能').grid(row=1,column=2)
        # Label(self,text='开发者').grid(row=1,column=3)
        Label(self,text='查看评论').grid(row =1, column=4)
        # Label(self,text='查看评分').grid(row =1, column=5)
        Label(self,text='更新').grid(row =1, column=6)
        Label(self,text='撤包').grid(row =1, column=7)
        # print(self.user)
        # print(t)
        x = 0
        
        # print(t[0],t[1])
        print(zip(t,range(len(t))))
        for i,s in zip(t,range(len(t))):
            print(i,s)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)
            # Label(self,text='{0}'.format(i[3])).grid(row=x+2,column=3)

            Button(self,text='查看评价',command=lambda i=i:self.PeekScore(i[0])).grid(row = x+2,column=4)
            # but1[s].bind("<Button-1>",lambda:self.PeekScore(i[0]))
            # Button(self,text='查看评论').grid(row = x+2,column=5)
            Button(self,text='更新',command=lambda i=i:self.UpdateApp()).grid(row = x+2,column=6)
            Button(self,text='撤包',command=lambda i=i:self.TakeBackApp()).grid(row = x+2,column=7)
           
            x=x+1  
        
        cur.execute('select * from outsideapp where developerid=%s',(self.developerid))
        t = np.array(cur.fetchall())
        Label(self,text='未上架应用',font=('黑体',16)).grid(row=x+2)
        Label(self,text='应用ID').grid(row=3+x,column=0)
        Label(self,text='名字').grid(row=3+x,column=1)
        Label(self,text='功能').grid(row=3+x,column=2)
        # Label(self,text='开发者').grid(row=1,column=3)
        Label(self,text='查看反馈').grid(row =3+x, column=4)
        Label(self,text='更新').grid(row =3+x, column=6)
        Label(self,text='撤包').grid(row =3+x, column=7)
        # Label(self,text='查看评分').grid(row =1, column=5)
        # Label(self,text='更新').grid(row =1+x, column=6)
        x=x+4
        for i,s in zip(t,range(len(t))):
            print(i,s)
            Label(self,text='{0}'.format(i[0])).grid(row=x+2,column=0)
            Label(self,text='{0}'.format(i[1])).grid(row=x+2,column=1)
            Label(self,text='{0}'.format(i[2])).grid(row=x+2,column=2)
            # Label(self,text='{0}'.format(i[3])).grid(row=x+2,column=3)

            Button(self,text='查看反馈',command=lambda i=i:self.PeekFeedback(i[0])).grid(row = x+2,column=4)
            # but1[s].bind("<Button-1>",lambda:self.PeekScore(i[0]))
            Button(self,text='更新',command=lambda i=i:self.Update()).grid(row = x+2,column=6)
            Button(self,text='撤包',command=lambda i=i:self.TakeBackApp()).grid(row = x+2,column=7)
            x = x+ 1
        conn.commit()
        cur.close()    

    def UpdateApp(self):
        showinfo(title="提示",message="您开发的应用正在更新！")

    def TakeBackApp(self):
        showinfo(title="提示",message="您的应用已经撤包，请及时更新！")

        
    def Update(self):
            showinfo(title='更新提醒：', message='正在更新，请耐心等待，感谢您的使用！')
    def PeekFeedback(self,appid):
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
        cur.execute('select outsideappid from feedback')
        applist = np.array(cur.fetchall())[:,0]
        print(applist)
        print(appid,type(appid))

        if appid in applist:
            window2 = Toplevel(self.page)
            window2.geometry('%dx%d' % (210,260))
            window2.title("反馈")
            cur.execute('select feedback from feedback where outsideappid =%s ',(appid))
            # print(cur.fetchall(),np.array(cur.fetchall()))
            feedback = np.array(cur.fetchall())[:,0]
            print(feedback)
            Label(window2,text='反馈').grid(row=2,column=1)
        
            Label(window2,text='{}'.format(feedback[0])).grid(row=3,column=1)
        else:
            
            showinfo(title='错误', message="无反馈信息！")
        conn.commit()
        cur.close() 
    def PeekScore(self,appid):
                # self.trypage = Frame(self.root)
        conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='2333',
        database="appmarket",
        charset='utf8'
    )
        appid = int(appid)
        cur = conn.cursor()
        window2 = Toplevel(self.page)
        window2.geometry('%dx%d' % (210,260))
        window2.title("评价")
        cur = conn.cursor()
        cur.execute('select mark from commenttable where appid =%s',(appid))
        # print(cur.fetchall(),np.array(cur.fetchall()))
        marks = np.array(cur.fetchall())[:,0]
        cur = conn.cursor()
        cur.execute('select comment from commenttable where appid=%s',(appid))
        comments = np.array(cur.fetchall())[:,0]
        print(marks)
        print(comments)
        x = 2
        cur.execute('select appname from insideapp where insideappid=%s',(appid))
        insideappname = np.array(cur.fetchall())
        print(insideappname)
        Label(window2,text='应用名').grid(row=x-1,column=2)
        Label(window2,text='{}'.format(insideappname[0][0])).grid(row=x-1,column=3)
        Label(window2,text='评分').grid(row=x,column=2)
        Label(window2,text='评论').grid(row=x,column=3)
        # print(t[0],t[1])
        for mark,comment in zip(marks,comments):
            # print(i)
            Label(window2,text='{}'.format(mark)).grid(row=x+1,column=2)
            Label(window2,text='{}'.format(comment)).grid(row=x+1,column=3)
            x = x + 1
        conn.commit()
        cur.close() 
class OutsideappFrame(Frame):
  
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.outsideappid = IntVar()
        self.appname = StringVar()
        self.description = StringVar()
        self.developerid = IntVar()
        self.CreatePage()

    def CreatePage(self):
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
         
        # self.page.pack()  
        Label(self).grid(row=0, stick=W)  
        # Label(self, text = '应用ID: ').grid(row=1, stick=W, pady=10)  
        # Entry(self, textvariable=self.outsideappid).grid(row=1, column=1, stick=E)  
        Label(self, text = '应用名: ').grid(row=2, stick=W, pady=10)  
        Entry(self, textvariable=self.appname).grid(row=2, column=1, stick=E)  
        Label(self, text = '描述: ').grid(row=3, stick=W, pady=10)  
        Entry(self, textvariable=self.description).grid(row=3, column=1, stick=E)  
        Label(self, text = '开发者: ').grid(row=4, stick=W, pady=10)  
        Entry(self, textvariable=self.developerid).grid(row=4, column=1, stick=E)  
        Button(self, text='发布',command = self.Upload).grid(row=5, stick=W, pady=10)  
        
        
        conn.commit()
        cur.close()

    def Upload(self):
        # outsideappid = int(self.outsideappid.get())
        appname = self.appname.get()
        description = self.description.get()
        developerid = int(self.developerid.get())
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2333',
            database="appmarket",
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute('select * from outsideapp order by outsideappid desc limit 1')
        t = np.array(cur.fetchall())
        outsideappid = int(t[0][0])+1
        cur.execute('insert into outsideapp values(%s,%s,%s,%s)',(outsideappid,appname,description,developerid))
        showinfo(title="提醒",message="您的应用已经成功提交")
        conn.commit()
        cur.close()

class DeveloperPage(Frame):  
    def __init__(self,master=None):  
        self.root = master  
         #定义内部变量root  
        self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小  
        # self.user =user
        # developerid = int(developerid)
        self.createPage()  
        # self.user = user
        print(self.root,type(self.root))
    def createPage(self):  
        self.insideappPage = InsideappFrame(self.root)  
        self.outsideappPage = OutsideappFrame(self.root)  


        
        self.insideappPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='应用管理', command = self.inside)  
        menubar.add_command(label='应用发布', command = self.outside)  
        self.root['menu'] = menubar  # 设置菜单栏  

    def inside(self):
        self.insideappPage.pack()
        self.outsideappPage.pack_forget()

    def outside(self):
        self.insideappPage.pack_forget()
        self.outsideappPage.pack()




  
  


   

