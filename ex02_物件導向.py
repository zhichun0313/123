cm=None
kg=None
bmi=None

def 輸入身高():
    global cm
    cm=int(input('請輸入身高(cm):'))

def 輸入體重():
    global kg
    kg=int(input('請輸入體重(kg):'))

def 計算bmi():
    global cm,kg,bmi
    m=cm/100
    bmi=kg/(m*m)

def 顯示bmi():
    print('bmi',bmi)

def 顯示評語():
    if bmi<18.5:
        print('體重過輕')
    elif 18.5<bmi<24:
        print('正常範圍')
    elif 24<bmi:
        print('體重過重')



#主程式
輸入身高()
輸入體重()
計算bmi()
顯示bmi()
顯示評語()