#CONNECTION 
import mysql.connector 
x=mysql.connector.connect(host="localhost",user="root",password="tamal",database="comp",auth_plugin='mysql_native_password')
cbj=x.cursor() 
# FOR VIEWING MENU SECTION... 
def vmen(): 
    q="select*from menu" 
    cbj.execute(q) 
    menu=cbj.fetchall()
    if len(menu)>0:
        print("\n\n\n--------Available Dishes-------\n\n\n")
        for i in menu:
            print("DISH NUMBER",i[0],"\n","--->",i[1],"(TYPE:",i[3],")","\n","PRICE",i[2])
        print("\n\n") 
    x.commit() 

    yn=int(input("YOU WANT TO ORDER AN ITEM? type(l for yes/2 for going back to main page):")) 
    if yn==1:
        byo() 
    else: 
        print("THANK YOU") 
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE") 
        return
#...FOR BOOKING 
def byo(): 
    b=0
    NAME=input("ENTER YOUR NAME:") 
    MOBNO=int(input("ENTER YOUR MOBILE NUMBER:")) 
    ADDRESS=input("ENTER YOUR ADDRESS:")
    vc=0
    while True:
        ID=int(input('ENTER DISH NO. OF THE ITEM YOU WANT TO ORDER:')) 
        QUANTITY=int(input("ENTER QUANTITY:"))      
        cbj.execute("select*from menu where ID={}".format(ID)) 
        z=cbj.fetchall()
        b=z[0][2]
        c=QUANTITY*b 
        vc+=c
        ins="insert into cusdet values({},{},'{}',{},'{}',{})".format(ID,QUANTITY,NAME,MOBNO,ADDRESS,c)
        cbj.execute(ins) 
        ASK=input("WANT TO QRDER MORE   TYPE---> YES/NO:")
        if ASK in ['no','NO']:
            break
    print("\n",'THANKS FOR YOUR ORDER' ,"\n\n","YOUR ORDER HAS BEEN ORDERED SUCCESSFULLY","\n\n")
    print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE") 
    x.commit()
    print('TOTAL AMOUNT TO PAY RS',vc)
#---------------FOR VIEWING ORDER----------------------
def vyo() :
    c=int(input("Enter your number :")) 
    r=" Select*from menu,cusdet where MOBNO={} and menu.ID=cusdet.ID".format(c) 
    cbj.execute(r) 
    e=cbj.fetchall() 
    if e==[]:
        print('NUMBER NOT FOUND')
    else:
        for j in e:
            print( "ID:", j[0], "\n", 'NAME:', j[6], "\n", " ITEM NAME:", j[1], "\n", " ITEM TYPE:", j[3], "\n", " TOTAL PRICE:", j[9], "\n", " MOBILE NUMBER:", j[7], "\n", " ADDRESS:", j[8], "\n") 
            x.commit()
#----------------------FOR CANCELLING ORDER--------------------

def cyo():
    c=int(input(" enter your number:"))
    r=" Select*from menu,cusdet where MOBNO={} and menu.ID=cusdet.ID".format(c)
    cbj.execute(r) 
    e=cbj.fetchall() 
    if e==[]:
        print('NUMBER NOT FOUND')
    else:
        b=" delete from cusdet where MOBNO={}".format(c)
        cbj.execute(b)
        print("\n\n","YOUR ORDER HAS BEEN CANCELLED")
    print("HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n\n")    
    x.commit()
#-----------------&&FEEDBACK&&--------------    
def fdbck():
    fd=input(" Enter your name:")
    print("Write something about us --")
    fdi=input()
    q=" insert into feedback values('{}','{}')".format(fd,fdi)
    cbj.execute(q)
    print(" \n")
    print("Thanks for your feedback :) ")
    print(" \n")
    print("HAVE BEEN REDIRECTED TO THE MAIN PAGE")
    print("\n")
    print("\n")
    x.commit()
#..........WELCOME
def start():
    print("\n")
    print("\n")
    print("                                 ______________")
    print("                              ********************")
    print("               ,,,,,,,,,,,,,,,,,,,,,WELCOME TO,,,,,,,,,,,,,,,,,,,,,")
    print("                          ::::::::::::::::::::::::::::::")
    print("                   [:::::::::>GROVE STREET RESTAURANT<::::::::]")
    print("                           ::::::::::::::::::::::::::::::")
    print("                                *******")
    print("                 ................................................")
    print("\n")
    print("Press assigned keys for going forward")
    print("1.CUSTOMER")
    print("2.EXIT")
#----------------WELCOME PAGE II ------------------
def start1 ():
    while True:
        print("\n")
        print("1.VIEW MENU AND ORDER FOOD")
        print("2.VIEW YOUR ORDERS")
        print("3.CANCEL ORDER")
        print("4.FEEDBACK")
        print("5.EXIT")
        chl=int(input("enter your choice:"))
        if chl==1:
            vmen()
            
        elif chl==2:
            vyo()
        elif chl==3:
            cyo()
        elif chl==4:
            fdbck()
        elif chl==5:
            print('thanks for ordering')
            break
        else:
            print("\n" ,"INVALID CHOICE","\n","TRY AGAIN","\n")
            start1()
start()
#------------------WELCOME PAGE INFINITE LOOP----------------

while True:
    ch=int(input("enter your choice?:"))
    if ch==1:
        start1()
    elif ch==2:
        print("thank you")
        break
    else:
        print("INVALID CHOICE","\n","TRY AGAIN")
        start()
    
