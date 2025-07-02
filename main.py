import mysql.connector 
from prettytable import PrettyTable
import datetime

mycon=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="atharva@09")
mycursor=mycon.cursor()

def database_creation():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS canteen_alpha")
    mycursor.execute("USE canteen_alpha")
    print("CONNECTION TO DATABASE SUCCESSFULL")
    print()
    print()

def create_menu():
    
    mycursor.execute("CREATE TABLE if not exists menu(Sno integer primary key,Itemname varchar(45),Price float(10,3))")
    insertquery="INSERT INTO menu(Sno,Itemname,Price)VALUES(%s,%s,%s)"
    items=[ (1,'Tea',10.00),(2,'Coffee',15.00),(3,'plain dosa',7.00),(4,'Masala Dosa',50.00),\
               (5,'Chicken Biriyani',140.00),(6,'Beef Biriyani',110.00),(7,'Veg Biriyani',80.00),\
               (8,'Fish Biriyani',160.00),(9,'Meals(veg)',50.00),(10,'Chicken fried rice',130.00),\
               (11,'Veg fried rice',100.00),(12,'Chicken noodles',130.00),(13,'Veg noodles',100.00),\
               (14,'Ghee rice',60.00),(15,'Fish fry',90.00),(16,'Chicken 65',120.00),\
               (17,'Chicken lollipop',40.00),(18,'Butter chicken',160.00),(19,'Ginger chicken',150.00),\
               (20,'Malabar chicken curry',150.00),(21,'Chicken tandoori(full)',290.00),\
               (22,'Beef fry',120.00),(23,'Beef roast',120.00),(24,'Mutton kuruma',210.00),\
               (25,'mutton stew',200.00),(26,'Egg curry',60.00),(27,'Paneer butter masala',110.00),\
               (28,'Palak paneer',120.00),(29,'Paneer tikka masala',120.00),(30,'tomato curry',80.00),\
               (31,'Cauliflower manchurian',90.00),(32,'Cauliflower dry fry',90.00),\
               (33,'Mushroom masala',90.00),(34,'Vegetable stir fry',140.00),(35,'Naan(plain)',12.00),\
               (36,'Butter naan',15.00),(37,'Chapatti',6.00),(38,'Porotta',10.00),\
               (39,'Porotta(wheat)',12.00),(40,'Omelette',12.00),(41,'Chicken sandwich',40.00),\
               (42,'Veg sandwich',25.00),(43,'Samosa',10.00),(44,'Chicken cutlet',10.00),\
               (45,'Veg cutlet',8.00),(46,'Fresh juice',30.00),(47,'Lime juice',10.00),\
               (48,'Lime soda',20.00),(49,'Frooti',20.00),(50,'Mineral Water(1Ltr)',15.00)]
    table1=mycursor.executemany(insertquery,items)
    mycon.commit()
    print()
    print('MENU TABLE SUCESSFULLY CREATED')
    print()
    print()

database_creation()

mycursor.execute("show tables")
myresult = mycursor.fetchall()

if ('menu',) in myresult:
    pass

else :
    create_menu()
'''
mycursor.execute("select * from menu")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''

try:
    def pwd_check(a):
        f=open("passwords.txt","r")
        b=f.read()
        if a==b:
            return True
        else:
            return False
        f.close()

    def order_func():
        
        mycursor.execute("CREATE TABLE if not exists orders(Date varchar(30),Item varchar(45),Quantity int(3),Price float(5,3))")
        
        y=str(datetime.datetime.today())
        
        
        food_item= input("Enter the Food Item: ")
        food_qty = int(input("Enter the Food Quantity: "))

        food_date=""
        for i in range(10):
            food_date= food_date+y[i]
        
        mycursor.execute("select * from menu")
        myresult= mycursor.fetchall()

        for x in myresult:
            
            if x[1]==food_item:
                price= x[2]* food_qty
            

        values = (food_date,food_item,food_qty,price)

        sql= "insert into orders(Date,Item,Quantity,Price) values('{}','{}',{},{})".format(food_date,food_item,food_qty,price)
        mycursor.execute(sql)
        mycon.commit()

    def billing_details():
        n= int(input("Do you Want Complete Bill History(1) or Datawise Bill(2)?"))
        if n==1:
            mycursor.execute("select * from orders")
            myresult= mycursor.fetchall()
            total_till_day=0

            for x in myresult:
                print(x)
                total_till_day=total_till_day+x[-1]
            print("Total Earning till date is: ", total_till_day)

        elif n==2:
            date= input("Enter Date in (YYYY-MM-DD) format: ")
            print(date)
            sql= "select * from orders where Date = %s"

            mycursor.execute(sql,(date,))
            myresult= mycursor.fetchall()
            total_till_day=0
            for x in myresult:
                total_till_day=total_till_day+x[-1]
                print(x)
            print("Total Earning for ",date," is : ", total_till_day)
        else :
            print("Invalid Entry")
        
    def update_addToMenu():
        Sno = int(input("Enter the Serial No: "))
        item= input("Enter the item: ")
        price = float(input("Enter the Price: "))
        values = (Sno,item,price)

        sql= "insert into menu(Sno,itemname,price) values({},'{}',{})".format(Sno,item,price)
        mycursor.execute(sql)
        mycon.commit()

    def update_deleteFromMenu():
        itemname =input("Enter the ItemName To be Deleted: ")
        sql= "delete from menu where itemname = %s"
        mycursor.execute(sql,(itemname,))
        
    
    def update_current():
        i_del = input("Enter the ItemName for which price is to be updated: ")
        new_price= float(input("Enter the new price: "))
        
        sql= "select * from menu where ItemName = %s"

        mycursor.execute(sql,(i_del,))
        myresult= mycursor.fetchall()
        
        sql= "delete from menu where itemname = %s"
        mycursor.execute(sql,(i_del,))
        
        sql= "insert into menu(Sno,itemname,price) values({},'{}',{})".format(myresult[0][0],i_del,new_price)
        mycursor.execute(sql)
        mycon.commit()
        
    def pwd_creation():
        f1= open("passwords.txt","w")
        n= input("Enter New password: ")
        f1.write(n)
        f1.close()

        
            

##########################################################################################User Input Part#################################

    while True:
            print("************** WELCOME TO AHLCON PUBLIC SCHOOL CANTEEN ******************")
            print("PLEASE ENTER THE CORRECT PASSWORD TO UNLOCK ADMIN PRIVILAGES OR ENTER HIT ENTER TO CONTINUE AS STUDENT ")
            password=input("ENTER PASSWORD :")
            f=pwd_check(password)
            if f==True:
                print("YOU WILL NOW HAVE ADMINISTRATIVE PRIVILAGES")
                admin=1
            else:
                print("YOU WILL NOW HAVE STUDENT PRIVILAGES ONLY")
                admin=0
            print("PLEASE SELECT THE KIND OF OPERATION YOU ARE ABOUT TO PERFORM")
            t1=PrettyTable(["CHOICE","OPERATION"])
            t1.add_row([1,"VIEW MENU"])
            t1.add_row([2,"PLACE A ORDER"])
            t1.add_row([3,"VIEW ALL PLACED ORDERS(ADMIN)"])
            t1.add_row([4,"UPDATION IN MENU(ADMIN)"])
            t1.add_row([5,"CHANGE ADMIN PASSWORD(ADMIN)"])

            print(t1)
            ch1=int(input("Enter your choice :"))
            print()
            try:
                if ch1==4 and admin==1:
                    while True:
                        print("YOU HAVE OPTED TO EDIT THE DATABSE")
                        print("NOW SELECT THE REQUIRED EDITIVE TASK")
                        t2=PrettyTable(["CHOICE","OPERATION"])
                        t2.add_row([1,"ADD NEW FOOD ITEM INTO MENU"])
                        t2.add_row([2,"UPDATE PRICE OF EXISTING ITEM"])
                        t2.add_row([3,"DELETE AN EXISTING FOOD ITEM FROM THE MENU"])
                        print(t2)
                        ch2=int(input('Enter your choice :'))                    
                        if ch2==1:
                            update_addToMenu()
                        elif ch2==2:
                            update_current()
                        elif ch2==3:
                            update_deleteFromMenu()
                        else:
                            print("***PLEASE ENTER THE CORRECT CHOICE***")
                            print()                        
                        if input('Do you want to continue "MANUPILATION IN THE DATABASE"(Y/N) :').upper()!='Y':
                            break
                elif ch1==2:
                    while True:
                        order_func()
                        if input('Do you want to Order more?(Y/N) :').upper()!='Y':
                            mycursor.execute("select * from orders")
                            myresult= mycursor.fetchall()
                            print("Your Order is Placed successfully, ")
                            print("Your Order No. is : ",str(len(myresult)))
                            print("Please wait for number to display on board!")
                            print("Happy To Serve!") 
                            break
                elif ch1==3 and admin==1:
                    while True:
                        billing_details()
                        if input('Do you want to Check more Billings?(Y/N) :').upper()!='Y':
                            break      

                elif ch1==5 and admin==1:
                    pwd_creation()

                elif ch1==1:
                    mycursor.execute("select * from menu")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                    
                elif admin==0 and ch1==1 or ch1==3 or ch1==4:
                    print("Sorry, INVALID OPERATION and you are only a GUEST USER")    
                else:
                     print("***PLEASE ENTER THE CORRECT CHOICE***")
            except:
                print("***PLEASE ENTER THE CORRECT CHOICE***")
            if input("WOULD YOU LIKE TO GO TO MAIN MENU??(Y/N) :").upper()!='Y':
                break
            
except Exception as err:
    print(err)
print()
print("THANK YOU FOR VISITING PLEASE COME AGAIN")
print()

## proprietary code of Atharva Srivastava
## NOT TO BE COPIED