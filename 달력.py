#year = 2020
#month=7
#day_of_week = 3
year = int(input('년도를 입력하세요: '))
month = int(input('달을 입력하세요:'))

weekdays = ['일','월','화','수','목','금','토']
#for day in weekdays:
    #print(' ',day,end = ' ')
#print()
#for i in range(day_of_week):
    #print('     ',end='')
def leapyear(y):
    if((y % 4 == 0 and y% 100 !=0)or y % 400 ==0):
        return True
    else:
        return False

def daysOfMonthy(y,m):
    numOfDays = 31
    if(m in [4,6,9,11]):
        numOfDays = 30
    if (m==2):
        if(leapyear(year)):
            numOfDays = 29
        else:
            numOfDays = 28
    return numOfDays
numOfmonth = daysOfMonthy(year,month)

#for day in range(1, numOfmonth +1):
   # if(day<10):
   #     print('  ',day, end = ' ')
   # else:
   #     print(' ',day,end=' ')
   # if ((day_of_week+day)%7 == 0):
   #     print()
#print()
def dayOfWeek(y, m ,d):
    # 전 년도 구하기 함수
    t1 = y - (14 - m) // 12
    # 전 년도 포함 전 년도까지의 날짜 구하기(윤년 포함)
    t2 = t1 +(t1//4) -(t1 // 100)+ (t1//400)
    # 
    t3= m + 12*((14-m)//12)-2
    return(d+t2+(31*t3//12))%7
#year = 2020
#month = 7
#day=1
#print(dayOfWeek(year,month,day))


def calander(year,month):
    numOfmonth = daysOfMonthy(year,month)
    day_of_week = dayOfWeek(year,month,1)
    print(year,'년',month,'월')
    for day in weekdays:
        print(' ',day,end = ' ')
    print('')
    for i in range(day_of_week):
        print('     ',end='')
    for day in range(1, numOfmonth +1):
        if(day<10):
            print('  ',day, end = ' ')
        else:
            print(' ',day,end=' ')
        if ((day_of_week+day)%7 == 0):
            print()
    print()
print(int(dayOfWeek(year,month,1)))
calander(year,month)
    