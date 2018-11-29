# -*- coding: utf-8 -*-
"""
This is a visual solution to the hanoi tower problom
"""

#引入所需要的库
import turtle as t #引入turtle，起简名为t
import random #引入random库

#更新屏幕
def clear_screen():
    t.pensize(1) #设置画笔大小
    t.pencolor('black') #设置画笔颜色
    t.clear() #清屏
    #屏幕划分，隐藏画笔，快速绘制
    t.setup(screenwidth,screenheight) #移动画笔到指定位置
    t.tracer(False) #取消绘画延迟
    t.hideturtle() #隐藏画笔
    t.penup() #抬起画笔
    t.setpos(-screenwidth/2,0) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenwidth) #向前移动指定距离
    t.tracer(True) #打开绘画延迟
    
#设置画笔初始位置
def pen_seat(area):
    global screenwidth,screenheight #全局变量
    #判断绘制区域
    if area == 0:
        t.penup() #抬起画笔
        t.setpos(0,screenheight/4) #移动画笔到指定位置
        t.seth(0) #奖画笔指向右（即正东，上北下南左西右东）
        t.pendown() #放下画笔
    elif area == 1:
        t.penup() #抬起画笔
        t.setpos(0,-screenheight/4) #移动画笔到指定位置
        t.seth(0) #奖画笔指向右（即正东，上北下南左西右东）
        t.pendown() #放下画笔
        
#绘制底物
def draw_substrate1(n,src,dst,area):
    global count,screenwidth,screenheight #全局变量
    pen_seat(area) #设置画笔初始位置
    t.pensize(5) #设置画笔大小
    t.pencolor('black') #设置画笔颜色
    t.hideturtle() #隐藏画笔
    t.tracer(False) #取消绘画延迟
    #绘制底座
    t.penup() #抬起画笔
    t.setpos(-screenwidth/2,screenheight/4-screenheight/6) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenwidth) #向前移动画笔指定距离
    #绘制A柱
    t.penup() #抬起画笔
    t.setpos(-(screenwidth/2-screenwidth/4),screenheight/4-screenheight/6) #移动画笔到指定位置
    t.left(90) #奖画笔指向左转90度
    t.pendown()  #放下画笔
    t.fd(screenheight/2-(screenheight/4-screenheight/6)) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(-(screenwidth/2-screenwidth/4),(screenheight/4-screenheight/6)-20) #移动画笔到指定位置
    t.write("A",False) #书写”A"
    #绘制B柱
    t.setpos(0,screenheight/4-screenheight/6) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd((screenheight/2-(screenheight/4-screenheight/6))) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(0,screenheight/4-screenheight/6-20) #移动画笔到指定位置
    t.write("B",False) #书写“B”
    #绘制C柱
    t.setpos(screenwidth/2-screenwidth/4,screenheight/4-screenheight/6) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenheight/2-(screenheight/4-screenheight/6)) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(screenwidth/2-screenwidth/4,screenheight/4-screenheight/6-20) #移动画笔到指定位置
    t.write("C",False) #书写“C”
    #书写操作过程
    t.setpos(0,20) #移动画笔到指定位置
    t.write("{}:{}--->{}".format(n,src,dst),False,align="center",font=("boldface",10,"normal")) #书写操作过程，画笔不移动，居中，黑体，10号大小，正常（不倾斜、加粗等）
    #书写篇幅页码
    t.setpos(screenwidth/2-50,20) #移动画笔到指定位置
    t.write("{}".format(count),False,font=(10)) #书写页码，画笔不移动，10号大小
    t.tracer(True) #打开绘画延迟
    pen_seat(area) #设置画笔初始位置
    
#绘制底物
def draw_substrate2(n,src,dst,area):
    global count,screenwidth,screenheight #全局变量
    pen_seat(area) #设置画笔初始位置
    t.pensize(5) #设置画笔大小
    t.pencolor('black') #设置画笔颜色
    t.hideturtle() #隐藏画笔
    t.tracer(False) #取消绘画延迟
    #绘制底座
    t.penup() #抬起画笔
    t.setpos(-screenwidth/2,(-screenheight/2)+(screenheight/4-screenheight/6)) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenwidth) #向前移动画笔指定距离
    #绘制A柱
    t.penup() #抬起画笔
    t.setpos(-(screenwidth/2-screenwidth/4),(-screenheight/2)+(screenheight/4-screenheight/6)) #移动画笔到指定位置
    t.left(90) #画笔指向左转90度
    t.pendown() #放下画笔
    t.fd(screenheight/2-(screenheight/4-screenheight/6)) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(-(screenwidth/2-screenwidth/4),(-screenheight/2)+(screenheight/4-screenheight/6)-20) #移动画笔到指定位置
    t.write("A",False) #写下“A”
    #绘制B柱
    t.setpos(0,(-screenheight/2)+(screenheight/4-screenheight/6)) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenheight/2-(screenheight/4-screenheight/6)) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(0,(-screenheight/2)+(screenheight/4-screenheight/6)-20) #移动画笔到指定位置
    t.write("B",False) #写下“B”
    #绘制C柱
    t.setpos(screenwidth/2-screenwidth/4,(-screenheight/2)+(screenheight/4-screenheight/6)) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenheight/2-(screenheight/4-screenheight/6)) #向前移动画笔指定距离
    t.penup() #抬起画笔
    t.setpos(screenwidth/2-screenwidth/4,(-screenheight/2)+(screenheight/4-screenheight/6)-20) #移动画笔到指定位置
    t.write("C",False)#写下“C”
    #书写操作过程
    t.setpos(0,-screenheight/2+20) #移动画笔到指定位置
    t.write("{}:{}--->{}".format(n,src,dst),False,align="center",font=("boldface",10,"normal")) #书写操作过程，画笔不移动，居中，黑体，10号大小，正常（不倾斜、加粗等）
    #书写篇幅页码
    t.setpos(screenwidth/2-50,-screenheight/2+20) #移动画笔到指定位置
    t.write("{}".format(count),font=(10)) #书写页码，画笔不移动，10号大小
    t.tracer(True) #打开绘画延迟
    pen_seat(area) #设置画笔初始位置
    
#计算圆盘个数
def nu(A,B):
    global src_number,dst_number,mid_number
    if A == 'A':
        src_number -=1
    elif A =='B':
        dst_number -=1
    elif A =='C':
        mid_number -=1
    if B == 'A':
        src_number +=1
    elif B == 'B':
        dst_number +=1
    elif B == 'C':
        mid_number +=1
        
#画圆盘    
def draw_disk(n):
    for i in range(n):
        t.penup() #抬起画笔
        t.left(90)
        t.fd(15) #向前移动画笔指定距离
        t.right(90)
        t.pencolor('red')
        t.pensize('10')
        t.fd(-100) #向前移动画笔指定距离
        t.pendown() #放下画笔
        t.fd(200) #向前移动画笔指定距离
        t.penup() #抬起画笔
        t.fd(-100) #向前移动画笔指定距离
        t.left(90)
        t.fd(15) #向前移动画笔指定距离
        t.right(90)
        t.pendown() #放下画笔


#汉诺塔问题计算
def hanoi(n,src,dst,mid):
    global count,src_number,dst_number,mid_number
    if n==1:
        count += 1 #篇幅页数加一
        nu(src,dst) #计算各住圆盘个数
        draw_area = count % 2 #选择绘制区域
        draw_hanoi(1,src,dst,draw_area) #绘制汉诺塔问题
        t.delay(10)#更新延迟
        #如果是0区域，则更新屏幕
        if draw_area == 0:
            clear_screen()
    else:
        hanoi(n-1,src,mid,dst)
        count += 1
        nu(src,dst)
        draw_area = count % 2
        draw_hanoi(n,src,dst,draw_area)
        t.delay(10)
        if draw_area == 0:
            clear_screen()
        hanoi(n-1,mid,dst,src)
        
#绘制汉诺塔
def draw_hanoi(n,src,dst,area):
    global src_number,dst_number,mid_number
    if area == 0:
        draw_substrate2(n,src,dst,area)
        #绘制A柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(-screenwidth/2+screenwidth/4,-screenheight/2+(screenheight/4-screenheight/6))
        draw_disk(src_number)
        #绘制B柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(0,-screenheight/2+(screenheight/4-screenheight/6))
        draw_disk(dst_number)
        #绘制C柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(screenwidth/2-screenwidth/4,-screenheight/2+(screenheight/4-screenheight/6))
        draw_disk(mid_number)
    elif area == 1:
        draw_substrate1(n,src,dst,area)
        #绘制A柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(-screenwidth/2+screenwidth/4,screenheight/4-screenheight/6)
        draw_disk(src_number)
        #绘制B柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(0,screenheight/4-screenheight/6)
        draw_disk(dst_number)
        #绘制C柱圆盘
        pen_seat(area)
        t.penup() #抬起画笔
        t.setpos(screenwidth/2-screenwidth/4,screenheight/4-screenheight/6)
        draw_disk(mid_number)
        
if __name__ == "__main__":
    #异常处理和汉诺塔层数选择
    way = None #初始汉诺塔层数选择方案
    Error_n = 0 #初始输入错误次数
    while True:
        print("There are two options : self-select and return a random integer from 1 to 6.")
        #获取方案
        way = input("Do you choose to input a number from 1 to 6 as the number of floors of Tower of Hanoi by yourself?:(y/n)")
        if way == 'y':
            number = eval(input("Please input a number from 1 to 6: ")) #获得圆盘数
            break
        elif way == 'n':
            number = random.randint(1,6) #随机给出圆盘数
            break
        #如果汉诺塔方案选择出错次数超过4次，则报错
        Error_n = Error_n + 1
        if Error_n >= 4:
            try:
                error
            except NameError :
                print("INPUT ERROR!")
            break
            
    #屏幕划分
    screenwidth = 1200 #屏幕宽度
    screenheight = 600 #屏幕高度
    t.setup(screenwidth,screenheight) #设置屏幕
    #隐藏画笔，快速划分屏幕，分成上下两块，上为1区，下为0区
    t.tracer(False) #取消绘画延迟
    t.hideturtle() #隐藏画笔
    t.penup() #抬起画笔
    t.setpos(-screenwidth/2,0) #移动画笔到指定位置
    t.pendown() #放下画笔
    t.fd(screenwidth) #向前移动画笔指定距离
    t.tracer(True) #打开绘画延迟
    
    count=0 #初始化绘制篇幅页数
    src_number = number #初始化A柱圆盘个数
    dst_number = 0 #初始化B柱圆盘个数
    mid_number = 0 #初始化C柱圆盘个数
    
    hanoi(number,'A','B','C') #传递参数，可视化解决汉诺塔问题
    print(count) #输出总页数（即汉诺塔问题运算次数）
    t.done() #结束绘制