from datetime import date
    
def question(q) :
    if q=="y" or q=="Y":
        start()

def checkCondition (birthyear,birthmonth,birthday,now):
    day30=[4,6,9,11]
    day31=[1,3,5,7,8,10,12]
    check=birthmonth
    if birthmonth<1 or birthmonth >12 :
        print("--------------------------------")
        print("Please try again !")
        q=input("Answer (y/n): ")
        print("--------------------------------") 
        question(q)
    if birthyear %4==0 and birthmonth == 2:
        if birthday < 1 or birthday > 29 :
            print("--------------------------------")
            print("Please try again !")
            q=input("Answer (y/n): ")
            print("--------------------------------")
            question(q)
        else :
            Lastday = 29
            calculation (birthyear,birthmonth,birthday,now,Lastday)
    elif birthyear %4!=0 and birthmonth == 2:
        if birthday < 1 or birthday > 28 :
            print("--------------------------------")
            print("Please try again !")
            q=input("Answer (y/n): ")
            print("--------------------------------")
            question(q)
        else :
            Lastday = 28
            calculation (birthyear,birthmonth,birthday,now,Lastday)
    if check in day30 :
        if birthday < 1 or birthday > 30 :
            print("--------------------------------")
            print("Please try again ! ")
            q=input("Answer (y/n): ")
            print("--------------------------------")
            question(q)
        else :
            Lastday = 30
            calculation (birthyear,birthmonth,birthday,now,Lastday)
            
    if check in day31 :
        if birthday < 1 or birthday > 31 :
            print("--------------------------------")
            print("Please try again !")
            q=input("Answer (y/n): ")
            print("--------------------------------")
            question(q)
        else :
            Lastday = 31
            calculation (birthyear,birthmonth,birthday,now,Lastday)
def calculation (birthyear,birthmonth,birthday,now,Lastday):
    yearzodiac=['ปีหนู','ปีวัว','ปีเสือ','ปีกระต่าย','ปีมังกร','ปีูงู','ปีม้า','ปีแพะ','ปีลิง','ปีไก่','ปีหมา','ปีหมู']
    # find age
    if int(now[2]) >= birthday:
        age_d = int(now[2])-birthday
        if int(now[1])>=birthmonth:
            age_m = int(now[1])-birthmonth
            age_y = int(now[0])-birthyear
        else :
            age_m = 12+int(now[1])-birthmonth
            age_y = int(now[0])-birthyear-1
    else :
        age_d = int(now[2])-birthday+Lastday
        if int(now[1])>=birthmonth:
            age_m = int(now[1])-birthmonth
            age_y = int(now[0])-birthyear
        else :
            age_m = 12+int(now[1])-birthmonth-1
            age_y = int(now[0])-birthyear-1
    year=4
    while birthyear>year :
        year=year+12
    if birthyear==year:
        zodiac=yearzodiac[0]
    else:
        i=birthyear-year
        zodiac=yearzodiac[i]
    print("*************")    
    print ('วันปัจจุบัน ',date.today().strftime('%d-%m-%Y'))
    print ('วันเกิด %d-%d-%d'%(birthday,birthmonth,birthyear))
    print ('อายุของคุณ %d ปี %d เดือน %d วัน' %( age_y,age_m,age_d))
    print('ปีนักษัตรของคุณคือ ', zodiac)

def start():
    birthyear =int(input("Birth Year :")) 
    birthmonth = int(input("Birth Month :"))
    birthday = int(input("Birth Day :"))
    now = date.today().strftime('%Y - %m - %d').split('-')
    checkCondition(birthyear,birthmonth,birthday,now)

print(start())




