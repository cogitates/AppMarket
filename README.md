# 安卓应用商城管理系统

数据库课程设计，时间紧张，做的一般，也不想再完善了
---

使用说明


环境:python 3.6.5


必要模块:pymysql,tkinter,numpy


数据库版本：mysql 5.7.21


若您打算使用本程序，请保证您已经配置好环境


由终端进入程序所在目录下，运行main.py程序


数据库文件已经导出到演示程序文件夹中


---
# 基本表

## commentttable

|commentid  |appid      |mark  |comment|
|-----------|-----------|------|-------|
|primary key|foreign key|      |       |

## feedback

|feedbackid |outsideappid|feedback  |
|-----------|------------|----------|
|primary key|foreign key |          |       
---
## outsideapp
|outsideappid|appname|appdescription|developerid|
|------------|---------|------------|-----------|
|primary key |         |            |foreign key|

## insideapp
|insideappid |appname|appdescription|developerid|
|------------|---------|------------|-----------|
|primary key |         |            |foreign key|

## user 
|userid     |username  | userpwd |
|-----------|----------|---------|
|primary key|          |         |

## manager
|manageid   |managername  | managerpwd |
|-----------|-------------|------------|
|primary key|             |            |

## developer
|developerid|developername|developerpwd|
|-----------|-------------|------------|
|primary key|             |            |



