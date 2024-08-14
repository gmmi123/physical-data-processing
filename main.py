import  numpy
from tkinter import *
from re import *
#判断数字小数点后的有效数位的函数
def CheckNumStr(Number:str):
    Val = -2
    for i in Number:
        if i == '.':
            Val = -1
        if Val >= -1:
            Val += 1
    if Val > 0:
        return Val
    else:
        return 0
#创建窗口
window = Tk()
window.config(background='#FFE0C0')
window.title('大物实验数据处理(广油专用)')
window.geometry('1186x624')
window.iconbitmap('favicon.ico')
#创建标签“输入数据”
Label1 = Label(window, text='输入实验数据', anchor='w', background='#FFE0C0', font=('宋体',15))
Label1.place(relx=0.005, rely=0.046, relwidth=0.108, relheight=0.048)
Label2 = Label(window, text='输入仪器误差', anchor='w', background='#FFE0C0', font=('宋体', 15))
Label2.place(relx=0.005, rely=0.182, relwidth=0.108, relheight=0.048)
Label3 = Label(window, text='原始结果', anchor='w', background='#FFE0C0', font=('宋体', 15))
Label3.place(relx=0.020, rely=0.342, relwidth=0.084, relheight=0.048)
Label6 = Label(window, text='自动取值数据结果', anchor='w', background='#FFE0C0', font=('宋体', 15))
Label6.place(relx=0.438, rely=0.34, relwidth=0.137, relheight=0.066)
Label7 = Label(window, text='实验数据用空格分隔开', anchor='center', background='yellow', font=('宋体', 15))
Label7.place(relx=0.638, rely=0.84, relwidth=0.307, relheight=0.066)
Label8 = Label(window, text='注意仪器误差与实验数据单位一致', anchor='center', background='yellow', font=('宋体', 15))
Label8.place(relx=0.638, rely=0.9, relwidth=0.307, relheight=0.066)
#创建输入栏
Text1Var = StringVar(value='')
Text1 = Entry(window, textvariable=Text1Var, font=('宋体',15))
Text1.place(relx=0.116, rely=0.023, relwidth=0.865, relheight=0.093)
Text2Var = StringVar(value='')
Text2 = Entry(window, textvariable=Text2Var, font=('宋体', 15))
Text2.place(relx=0.116, rely=0.159, relwidth=0.865, relheight=0.093)
# 收集观测数据

# 处理数据
Date = StringVar()
Average =0
Label4Var = StringVar(value="（+。+）/还没有结果")
Label5Var = StringVar(value="（+。+）/还没有结果")
def Command1_Cmd():
    DateTest = Text1.get()#获取实验数据（字符串）
    DateTest2 = Text2.get()  # 获取仪器误差（字符串）
    # global Average     #平均值
    Numes =[] #总的实验数据（数字）
    ErrNumes =[]#仪器误差
    NumCount = len(findall(r"(-\d+\.\d+|\d+\.\d+|-\d+|\d+)",DateTest))    #获取的实验数字个数
    ErrNumCount = len(findall(r"(-\d+\.\d+|\d+\.\d+|-\d+|\d+)", DateTest2))
    for i in range(NumCount):
    #     # 计算平均值
        Numes.append(eval(findall(r"(-\d+\.\d+|\d+\.\d+|-\d+|\d+)",DateTest)[i]))
    for i in range(ErrNumCount):
        #     # 计算平均值
        ErrNumes.append(eval(findall(r"(-\d+\.\d+|\d+\.\d+|-\d+|\d+)", DateTest2)[i]))
    AverageNum = numpy.average(Numes)
    stdNumA = numpy.std(Numes, ddof=1)
    stdNumB = ErrNumes[0]/numpy.sqrt(3)
    stdNumAll = numpy.sqrt(numpy.power(stdNumA,2)+numpy.power(stdNumB,2))
    rNum = ((numpy.ceil(stdNumAll*1000)/1000)/(numpy.ceil(AverageNum*1000)/1000))*100
    # print("平均值:",AverageNum)
    # print("A类不确定度:", stdNumA)
    # print("B类不确定度",stdNumB)
    # print("总不确定度", stdNumAll)
    # print("rNum",rNum)
    # print(Numes[0])
    effNum = CheckNumStr(findall(r"(-\d+\.\d+|\d+\.\d+|-\d+|\d+)",DateTest)[0])


    Label4Var.set("平均值:"+str(round(AverageNum,effNum+2))
                  +"\r\n" + "A类不确定度:" + str(round(stdNumA, effNum+2))
                  +"\r\n" + "B类不确定度:" + str(round(stdNumB, effNum+2))
                  +"\r\n" + "总不确定度:" + str(round(stdNumAll, effNum+2))
                  )
    Label5Var.set("U="+'('+str(round(AverageNum, effNum))+"±"+str(numpy.ceil(stdNumAll*(numpy.pow(10,effNum)))/numpy.pow(10,effNum))+')单位'
                  +"\r\n"+"Ur=" + '±' +str(numpy.ceil(rNum*100)/100)+'%'
                  )
#创建按键
Command1 = Button(window, text='计算', command=Command1_Cmd,  font=('宋体', 15))
Command1.place(relx=0.116, rely=0.703, relwidth=0.152, relheight=0.139)

Label4 = Label(window, textvariable=Label4Var,  anchor='center', background='#FFFFFF', font=('宋体', 15))
Label4.place(relx=0.11, rely=0.34, relwidth=0.321, relheight=0.29)
Label5 = Label(window, textvariable=Label5Var,  anchor='center', background='#FFFFFF', font=('宋体', 15))
Label5.place(relx=0.585, rely=0.34, relwidth=0.347, relheight=0.29)
if __name__ == '__main__':
    window.mainloop()