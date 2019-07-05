from tkinter import * 
from tkinter.messagebox import *
import pymysql
from userpage import *
from managerpage import *
from developerpage import * 
from tkinter import simpledialog
# 创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='2333',
    database="appmarket",
    charset='utf8'
)
cur = conn.cursor()
# user = 0
class LoginPage(object):  
    def __init__(self, master):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (320,200)) #设置窗口大小  
        
        self.username = StringVar()  
        self.password = StringVar()  
        self.nickname = StringVar()
        self.CreateGuidance()  

# 引导页---------------------------------------------------------------------------------
    def CreateGuidance(self):
        self.Page = Frame(self.root) #创建Frame  
        self.Page.pack() 
        Label(self.Page, text = '请选择您的身份').grid(row=3,column=2,pady=14,stick=E) 
        Button(self.Page, text='用户', command=self.CreateUserPage).grid(row=5, column=1,pady=10)  
        Button(self.Page, text='管理员', command=self.CreateManagerPage).grid(row=5, column=2)  
        Button(self.Page, text='开发者', command=self.CreateDeveloperPage).grid(row=5, column=3) 
        

    def CreateUserPage(self):
        self.Page.destroy()  
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登陆', command=self.UserLogin).grid(row=3, stick=W, pady=10)  
        Button(self.page, text='注册', command=self.UserRegister).grid(row=3, column=1, stick=E)  

    def CreateManagerPage(self):
        self.Page.destroy()  
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登陆', command=self.ManagerLogin).grid(row=3, stick=W, pady=10)  
        Button(self.page, text='注册', command=self.ManagerRegister).grid(row=3, column=1, stick=E)  

    def CreateDeveloperPage(self):
        self.Page.destroy()  
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登录', command=self.DeveloperLogin).grid(row=3, stick=W, pady=10)  
        Button(self.page, text='注册', command=self.DeveloperRegister).grid(row=3, column=1, stick=E)  
#　用户----------------------------------------------------------------------------------
    def UserLogin(self):  
       
        user = int(self.username.get())
        psw = self.password.get()  
        # print(user,psw,type(user),type(psw))
        # cur.execute('delete from user where userid=4')
        cur.execute('select userid,userpwd from user')
       
        if (user, psw) in cur.fetchall():
            # print(cur.fetchall())
            self.page.destroy() 
            
            UserPage(self.root)
        else:
            showinfo(title = '错误', message="用户ID或密码有误！")
         

    def UserRegister(self):
        userid = int(self.username.get()  )
        # print(type(user))
        psw = self.password.get()
        cur.execute('select userid,userpwd from user')
        t = np.array(cur.fetchall())[:,0]
        # print(t)
        if str(userid) in t  :
            showinfo(title='错误', message='该用户ID已注册！请输入其他用户ID') 
        else: 
            showinfo(title = '成功', message="注册成功！".format(userid))
            self.nickname =simpledialog.askstring(title="提示",prompt="请完善您的用户名信息")
            self.page.destroy()  
            cur.execute('insert into user values(%s,%s, %s)', (userid,self.nickname, psw))
            showinfo(title='您的信息已成功录入',message="请您选择登录")
            LoginPage(self.root)
            
# 管理员---------------------------------------------------------------------------------
    def ManagerLogin(self):  
        user = int(self.username.get())
        psw = self.password.get()  
        # print(user,psw,type(user),type(psw))
        cur.execute('select managerid,managerpwd from manager')
       
        if (user, psw) in cur.fetchall():
            print(cur.fetchall())
            self.page.destroy()  
            ManagerPage(self.root)
        else:
            showinfo(title = '错误', message="用户ID或密码有误！")

    def ManagerRegister(self):

        showinfo(title='警告', message='请新管理员在数据库中设置账户！！')          
# 开发者---------------------------------------------------------------------------------
    def DeveloperLogin(self):  
        user = int(self.username.get())
        psw = self.password.get()  
        cur.execute('select developerid, developerpwd from developer')
       
        if (user, psw) in cur.fetchall():
            print(cur.fetchall())
            self.page.destroy()  
            DeveloperPage(self.root)
        else:
            showinfo(title = '错误', message="开发者ID或密码有误！")
         
    def DeveloperRegister(self):
        user = int(self.username.get()  )
        psw = self.password.get()
        cur.execute('select developerid from developer')
        t = np.array(cur.fetchall())[:,0]
        print(t)
        if user in t  :
            showinfo(title='错误', message='该开发者ID已注册！请输入其他开发者ID') 
        else: 
            showinfo(title = '成功', message="注册成功！已以{}身份登入".format(user))
            self.nickname =simpledialog.askstring(title="提示",prompt="请完善您的用户名信息")
            cur.execute('insert into developer values(%s,%s, %s)', (user,self.nickname, psw))
            self.page.destroy()  
            showinfo(title='您的信息已成功录入',message="请您选择登录")
            LoginPage(self.root)
            
            


root = Tk()  



root.title('Android App Market')  
LoginPage(root)  
root.mainloop() 

conn.commit()
cur.close()
