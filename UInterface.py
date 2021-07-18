# import tkinter as tk
from tkinter import *
import time
import Pygeturl
import ClassDoPa
import py2exe

##--------------------------------------------------------------
TkMainWindow=Tk()
TkMainWindow.geometry("900x750")
TkMainWindow.title("Spi_Web_Data")
TkMainWindow.resizable(0,0)
##--------------------------------------------------------------
BigFrame=Frame(TkMainWindow,bg="lightblue")
BigFrame.place(width=900,height=620)

BigCanvas=Canvas(BigFrame,bg="black")
BigCanvas.place(width=900,height=620,x=0,y=0)
# BigCanvas.place(width=880,height=600,x=20,y=20)

Xscrollbar_F=Scrollbar(BigFrame)
Yscrollbar_F=Scrollbar(BigFrame)

Xscrollbar_F.config(command=BigCanvas.xview,orient="horizontal")
Yscrollbar_F.config(command=BigCanvas.yview)

BigCanvas.config(xscrollcommand=Xscrollbar_F.set,yscrollcommand=Yscrollbar_F.set)
BigCanvas.columnconfigure(0,weight=1)
Xscrollbar_F.pack(side="bottom",fill=X)
Yscrollbar_F.pack(side="right",fill=Y)
##--------------------------------------------------------------
Label_UrlText_Str=StringVar()
# Label_UrlText_Str.set("輸入希望查詢的網址!")
label1=Label(BigFrame,text="輸入網址(Key in Address):",bg="black",fg="white",font=("標楷體",12),justify=LEFT)
label1.place(width=240,height=20,x=20,y=20)

Label_Url_Text=Entry(BigFrame,bg="lightgreen",font=("April",12),textvariable=Label_UrlText_Str)
Label_Url_Text.place(width=560,height=20,x=280,y=20)

Label_Url_scrollX=Scrollbar(Label_Url_Text)
Label_Url_scrollX.config(command=Label_Url_Text.xview,orient="vertical")
Label_Url_scrollX.pack(side="right",fill=Y)
# Label_Url_scrollX.place(width=560,height=10,y=25)
Label_Url_Text.config(xscrollcommand=Label_Url_scrollX.set)
Label_UrlText_Str_Value=Label_UrlText_Str.get()

Result_Text_Str=[]
label2=Label(BigFrame,text="網頁源代碼搜尋結果顯示窗:",bg="black",fg="white",font=("標楷體",12))
label2.place(width=240,height=20,x=20,y=90)
#
label3=Label(BigFrame,text="選擇搜尋條件:",bg="black",fg="white",font=("標楷體",12))
label3.place(width=240,height=20,x=20,y=410)

##--------------------------------------------------------------

Label_Result_Text=Text(BigFrame,font=("標楷體",12,"normal"),bg="lightyellow",)

Xscrollbar_Text = Scrollbar(Label_Result_Text, orient="horizontal")
Xscrollbar_Text.pack(side=BOTTOM,fill=X)

Yscrollbar_Text = Scrollbar(Label_Result_Text, orient="vertical")
Yscrollbar_Text.pack(side=RIGHT,fill=Y)

Xscrollbar_Text.config(command=Label_Result_Text.xview,orient='horizontal')
Yscrollbar_Text.config(command=Label_Result_Text.yview)
Label_Result_Text.config(xscrollcommand=Xscrollbar_Text.set,yscrollcommand=Yscrollbar_Text.set,state="disable")

Xscrollbar_Text.pack(side=BOTTOM,fill=X)
Yscrollbar_Text.pack(side=RIGHT,fill=Y)
# TkMainWindow.columnconfigure(0,weight=1)
Label_Result_Text.place(width=560,height=300,x=280,y=90)
##--------------------------------------------------------------
textlist=[]
flag=0
def doFunc():
    # global flag
    # if(flag==1):
    #     i=""
    #     stopdokey=input(i)
    #     if(flag==0):
    #         i="start"
    #         stopdokey = input(i)
    # else:
    Label_Result_Text.config(state="normal")
    clearFunc()

    URL = Label_UrlText_Str.get()
    # print(URL)
    KeyStr = Pygeturl.PygetURL(URL)
    textlist = KeyStr.Pygeturl(URL)
    # dofunc__ = ClassDoPa.WinControl().run()
    for i in textlist:
        Label_Result_Text.insert(END, i)
    print("Finish the search!")
    if Label_Result_Text is not []:
        Label_Result_Text.config(state="disable")

def clearFunc():
    if Label_Result_Text is []:
        return print("it's empty!")
    else:
        Label_Result_Text.config(state="normal")
        Label_Result_Text.delete(0.0,END)
        print("Finish the clearwork!")
def closeFunc():
    TkMainWindow.destroy()

# import os
# flag=0
def StopFunc():
    pause = ClassDoPa.WinControl().pause()
    # global flag
    # do=ClassDoPa.WinControl.run()
    # if(flag==0):
    #     flag+=1
    # else:
    #     flag-=1
        # return flag
        # return 0

BtnFrame=LabelFrame(TkMainWindow,text="Btn_Section")
doBtn=Button(BtnFrame,text="Just Do",command=doFunc)
clearBtn=Button(BtnFrame,text="Clear Face",command=clearFunc)
closeBtn=Button(BtnFrame,text="Close Wins",command=closeFunc)
stopBtn=Button(BtnFrame,text="Stop Doing",command=StopFunc)

doBtn.place(x=40,y=10)
clearBtn.place(x=140,y=10)
stopBtn.place(x=240,y=10)
closeBtn.place(x=340,y=10)
BtnFrame.place(x=420,y=650,width=450,height=70)

##--------------------------------------------------------------

def sendToDB():
    pass
def saveData():
    pass



WebBTNSection=LabelFrame(TkMainWindow,text="WEB_DB",width=300,height=70)
DelieveDB=Button(WebBTNSection,text="Send to DB",command=sendToDB)
DelieveDB.place(x=40,y=10)
SaveData=Button(WebBTNSection,text="Save data",command=saveData)
SaveData.place(x=180,y=10)
WebBTNSection.place(x=20,y=650)

TkMainWindow.mainloop()