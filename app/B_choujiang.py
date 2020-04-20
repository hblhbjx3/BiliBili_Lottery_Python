import random
from tkinter import *

BOARD_WIDTH = 400
BOARD_HEIGHT = 600
main = Tk()
str_jieguo = StringVar()
main.title("B站—评论抽奖")
main.geometry('450x600')
# 禁止改变窗口大小
main.resizable(width=False, height=False)
# 修改图标
main.iconbitmap('logo.ico')
# print(random.randint(0,9))

c1 = Canvas(main, background='white',
    width=BOARD_WIDTH, height=BOARD_HEIGHT)
c1.pack()
bg_img = PhotoImage(file='image/bg.png')#程序背景图
paiBtn = PhotoImage(file='image/bt.png')#按钮背景
zhong = PhotoImage(file='image/gongxi.png')#恭喜文字

c1.create_image(BOARD_WIDTH /2, BOARD_HEIGHT/2, image=bg_img)
#输入页数
pages = Entry(main, font=("SourceHanSansHWTC-Bold",16),foreground = '#00a1d6',insertofftime = 1000,\
              bd = 0,insertbackground = '#00a1d6',bg = "#f2f2f2" )#页数,background="#f2f2f2"
pages.place(relx=0.288, rely=0.26, width=40, height=40, anchor=CENTER)
#输入最后一页个数
num =  Entry(main, font=("SourceHanSansHWTC-Bold",17),foreground = '#00a1d6',insertofftime = 1000,\
             bd = 0,insertbackground = '#00a1d6',bg = "#f2f2f2" )#剩余评论个数
num.place(relx=0.58, rely=0.26, width=25, height=40, anchor=CENTER)

str_zongshu = StringVar()
str_zhongjiang = StringVar()
str_yeshu = StringVar()
str_geshu = StringVar()

#抽奖函数
def Gan():
    a = int(pages.get())
    b = int(num.get())
    sum = a*20+b
    str_zongshu.set(str(sum))#总数
    zhongjiang = random.randint(1, sum)#1-sum总数 生成一个随机数
    str_zhongjiang.set(str(zhongjiang)) #中奖号
    #显示逻辑
    if (zhongjiang % 20) == 0 :
        pages2 = zhongjiang // 20
        num2 = 20
    else :
        pages2 = zhongjiang // 20 + 1
        num2 = zhongjiang % 20
    str_yeshu.set(str(pages2))      #对应页数
    str_geshu.set(str(num2))        #对应该页个数
    Label(main, image = zhong
          ).place(relx=0.46, rely=0.75, anchor=CENTER)  # 总数显示

Label(main, textvariable = str_zongshu, font = ("SourceHanSansHWTC-Bold",16), foreground = '#fb7299'
      ).place(relx=0.5, rely=0.4, anchor= CENTER)#总数显示
Label(main, textvariable = str_zhongjiang, font = ("SourceHanSansHWTC-Bold",22), foreground = '#fb7299'
      ).place(relx=0.55, rely=0.5, anchor= CENTER)#中奖号显示
Label(main, textvariable = str_yeshu, font = ("SourceHanSansHWTC-Bold",18), foreground = '#fb7299'
      ).place(relx=0.3, rely=0.6, anchor= CENTER, height=30)#中奖号对应页数
Label(main, textvariable = str_geshu, font = ("SourceHanSansHWTC-Bold",18), foreground = '#fb7299'
      ).place(relx=0.63, rely=0.6, anchor= CENTER, height=30)#中奖号对应该页的第几个

# 设置按钮的宽度
Button(main, text = '开始抽奖', command = Gan, relief = FLAT, cursor = "hand2",\
       image = paiBtn).place(relx=0.47, rely=0.85, anchor=CENTER) #按钮


main.mainloop()