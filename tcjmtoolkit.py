#打包命令 python -m PyInstaller -F -c D:\desktop\cal\calculator.py --icon=D:\desktop\cal\tcjm.ico

import math
import random
print("===============================================================================\n\n欢迎使用 | 台场建设株式会社\n\n===============================================================================")

print("这是一个基物实验计算器，也可以用于其他实验报告的撰写")
print("这个计算器可以帮你计算不确定度和回归相关的数据，以及平均值之类一切你可能需要的东西，它可以一次处理多组甚至两组数据")
print("填数据不要用科学计数法，但是它会出科学计数法的数据")
print("这玩意自动重复运行了，要是想停止的话，随便按按回车就行")
print("如果你使用的是exe版本，那么图标是大秽的台场静马，请支持大崎梦游大江岛奇遇记（bushi）")
#前置工具
def squ(x):
    return x**2
def shurushujv():
    datas = []
    datas = input("在下面输入你的数据，用英文逗号隔开，记得单位换算，尤其是算回归的时候").split(",")
    datas = [float(item) for item in datas]
    return datas
def shujvchuli(datas):
    #输入数据
    ub = float(input("输入ub，常用游标卡尺ub（单位为m）为0.000011547，天平是（单位为kg）0.0000057735（算回归的话，随便填个数就行）"))
    #数据个数
    length = len(datas)
    #和以及平均值
    summ = sum(datas)
    ave = summ/length
    #平方和以及方均值
    datas2 = map(squ,datas)
    sum2 = sum(datas2)
    ave2 = sum2/length
    #需要用到上面的前置工具
    def ddata(x):
        return x-ave
    #dds就是每个数据减平均值，deltadatas
    dds = map(ddata,datas)
    dds2 = map(squ,dds)
    sumdds2 = sum(dds2)
    #不确定度计算
    ua = math.sqrt(sumdds2/(length*(length-1)))
    u = math.sqrt(squ(ua)+squ(ub))
    #不确定度的百分比？
    pu = u/ave
    return length,summ,ave,ave2,sumdds2,ua,u,pu,dds,ub

signin = ["台场建设株式会社 代表取缔役 台场静马","新木场侦探社 大崎■■","新木场侦探社 新木场","新木场侦探社 品川",
          "外包人员 有明胜太郎（为了大崎先生，我会努力的……！）","外包人员 竹芝叶藏（计算这种东西，根本不是我能做的啊///）",
          "？？？ 大江杏//////ERROR......RELOADING......ERROR","台场佐清♥感谢使用~","|诚！|新选组局长-近藤勇",
          "新选组副长-土方岁三","会津藩-斋藤一","试卫馆-冲田总司","新选组总长-山南敬助",">某匿名审神者<",
          ">-数字啊，风雅地消散吧！-歌仙兼定<","/人理保障机构迦勒底/玛修","/人理保障机构迦勒底/罗马尼","/人理保障机构迦勒底/藤丸立香",
          "红月☽ 莲巳敬人","红月☽ 鬼龙红郎","红月☽ 神崎飒马","|辉光之境|W.M氏|我们指引前路，我们照明驱暗，我们无有怜悯之心|","LOBOTOMY_CORP_CHESED","盖尔.德卡里奥斯","塔拉"]
#选择计算模式。。。
def modd():
    print(" .•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•.\n\n数据处理员：",random.choice(signin),"\n\n .•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•..•♫•♬••♬•♫•.")
    mod = input("你想要的模式，回归模式处理两组数据，自变量和因变量。不确定度模式处理多组数据。输入回归或不确定度选择计算模式")
    if mod == "回归":
        print("先输入x再输入y，输入的x和y要一一对应，比如x1,x2,x3，那y也是y1,y2,y3。")

        datasx = shurushujv()
        resultx = shujvchuli(datasx)
        datasy = shurushujv()
        resulty = shujvchuli(datasy)
        sumdds2x = resultx[4]
        sumdds2y = resulty[4]
        sumx = resultx[1]
        sumy = resulty[1]
        ave_x = resultx[2]
        ave_y = resulty[2]

        #协方差计算
        ddssum = 0
        for i in range(len(datasx)):
            ddssum += (datasx[i] - ave_x) * (datasy[i] - ave_y)

        #回归系数计算
        r = ddssum / math.sqrt(sumdds2x * sumdds2y)
        b = ddssum / sumdds2x
        a = ave_y - b * ave_x

        print("相关系数 r =", r)
        print("回归方程：y =", b, "x +", a)
        uabs = (1/(len(datasx)-2))*((1/(r**2))-1)
        
        uab = b*math.sqrt(uabs)
        print("b的a类不确定度：",uab)
    
    elif mod == "去哪吃饭":
        fan = ["合一二楼","合一三楼","合一四楼","新北一楼","新北二楼","新北三楼","学二？","外食"]
        soto =["牛肉面","小笼包","其他外食"]
        chifan = random.choice(fan)
        if chifan == "外食":
            print (random.choice(soto))
        else:
            print(chifan)
        print("要好好吃饭哦~♥")

        
    else:
        n = int(input("你想要输入多少组数据，输0的话，自动跳过，进入总不确定度计算"))
        
        for i in range(n):
            datasn = shurushujv()
            lenn,sumn,aven,ave2n,sumdds2n,uan,un,pun,ddsn,ub = shujvchuli(datasn)
            print("数据组数",i+1,"\n数据个数",lenn,"\n和",sumn,"\n均值",aven,"\n均方值",ave2n,"\n方差乘数据个数",sumdds2n,"\n方差",sumdds2n/lenn)
            print("a类不确定度ua",uan,"\nb类不确定度ub",ub,"\n不确定度u(x)",un,"不确定度比数据均值u(x)/x",pun)
            
        print("接下来求总不确定度，由于不确定度公式很灵活，这里没法复刻，需要手动输入添加的每个不确定度比值，以及你得到的数据")
        uns = input("输入你需要添加的每个不确定度比数据均值（参见总不确定度求法），用英文逗号隔开").split(",")
        uns = [float(item) for item in uns]
        uns2 = map(squ,uns)
        uall = math.sqrt(sum(uns2))
        print("总不确定度比数据均值",uall)
        fin = float(input("输入你的总不确定度对应的数据均值"))
        print("总不确定度",fin*uall)    
    print("===============================================================================\n\n感谢使用 | 台场建设株式会社\n\n===============================================================================")
    lover = random.randint(1,108)
    if lover == 108:
        print("其实，我有一百零八个情人~♥")

while True:
    modd()
            


