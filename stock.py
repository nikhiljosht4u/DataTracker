import mysql.connector
import time
import webbrowser

# CREATING DATBASE IF NOT EXISTS
try:

    con=mysql.connector.connect(host='localhost',user='root',passwd='5800')

    curs=con.cursor()

    curs.execute("CREATE DATABASE IF NOT EXISTS project")
    
       
except:
    print('\t\t\t\t\t LOGIN UNSUCCESSFUL')
    print('\t\t\t\t\t   TRY AGAIN......')
    time.sleep(2)

# CONNECTING TO DATABASE AND
# CREATING TABLES IF NOT EXISTS 

try:
    con=mysql.connector.connect(host='localhost',user='root',passwd='5800',database='project')
    curs=con.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS stock_summary (item_name varchar(20),nos int,hsn_code int)")
        
except Exception as e:
    exit()

# DEFINING MAIN

def main():
    ent = input("\t WELCOME TO STOCK SUMMARY DATABASE MANAGER !! Press ENTER to continue")
    if ent == "enter":
        print("Please check Again!")
    else:
        print(" ")
        while True:
            print("\t\t\t1 ADD NEW STOCK\n")
            print("\t\t\t2 EDIT STOCK\n") 
            print("\t\t\t3 DELETE STOCK ITEM\n")
            print("\t\t\t4 SHOW STOCK\n") 
            print("\t\t\t5 DELETE COMPLETE STOCK\n")
            print("\t\t\t6 FIND HSN CODE OF ITEMS\n")
            print("\t\t\t7 CALCULATE GST PRICE\n")
            print("\t\t\t8 FIND GST RATES\n")
            print("\t\t\t0 Exit\n")
            ch=int(input("Enter your choice(1-5):"))
            if ch == 1:
                print(" ")
                add()
            elif ch == 2:
                print(" ") 
                update() 
            elif ch == 3:
                print(" ") 
                delete() 
            elif ch == 4:
                print(" ") 
                show() 
            elif ch == 5:
                print(" ") 
                drop()
            elif ch == 6:
                print(" ")
                browse()
            elif ch == 7:
                print(" ")
                gstcalc()
            elif ch == 8:
                print(" ")
                gstrate()
            elif ch == 0:
                break
            else:
                print('Enter valid choice')
                time.sleep(2)
                
# ADDING NEW STOCK

def add():
    hsn_code=int(input('Enter HSN Code :'))
    primary(hsn_code)
    item_name=input('Enter Name Of The Item :')
    nos=int(input('Enter NOS/QUANTITY :'))
    try:
        curs.execute("insert into stock_summary values('{}',{},{})".format(item_name,nos,hsn_code))
        con.commit()
        print("Record Added Successfully")
    except:
        print("Record Added Unsuccessfully.Check The Details Again")
        main()
        
# EDITING STOCK

def update():
    print("\t\t\t1 UPDATE ITEM NAME")
    print("\t\t\t2 UPDATE NOS      ")
    print("\t\t\t3 UPDATE HSN CODE ")
    ch=int(input("Enter your choice(1 OR 2 OR 3):"))
    print(" ")
    if ch==1:
        hsn_code=int(input('Enter HSN Code'))
        primary4update(hsn_code)  
        NEW_item_name=input('Enter NEW Item Name')
        try:
            curs.execute("UPDATE stock_summary set item_name='{}' where hsn_code='{}';".format(NEW_item_name,hsn_code))
            con.commit()
            print("Record Added Successfully")
        except:
            print("Record Added Unsuccessfully.Check The Details Again")
            update()
            
    elif ch==2:
        hsn_code=int(input('Enter HSN Code'))
        primary4update(hsn_code)
        NEW_item_NOS=int(input('Enter NEW Item NOS/QUANTITY :'))
        try:
            curs.execute("UPDATE stock_summary set nos='{}' where hsn_code='{}';".format(NEW_item_NOS,hsn_code))
            con.commit()
            print("Record Updated Successfully")
        except:
            print("Record Added Unsuccessfully.Check The Details Again")
            update()
            
    elif ch==3:
        hsn_code=int(input('Enter HSN Code'))
        primary4update(hsn_code)
        NEW_hsn_code=int(input('Enter NEW HSN Code'))
        try:
            curs.execute("UPDATE stock_summary set hsn_code={} where hsn_code={};".format(NEW_hsn_code,hsn_code))
            con.commit()
            print("Record Updated Successfully")
        except:
            print("Record Added Unsuccessfully.Check The Details Again")

# DELETING STOCK

def delete():
    hsn_code=int(input('Enter HSN Code Of Item To Delete:'))
    primary4delete(hsn_code)
    try:
        curs.execute("delete from stock_summary where hsn_code='{}'".format(hsn_code))
        con.commit()
        print("Stock Summary Updated Successfully")
    except:
        print("Deletion Unsuccessfully")

#RECORD
        
def show():
    curs.execute("SELECT * FROM stock_summary;")
    rec=curs.fetchall()
    if rec=='Null':
        print("EMPTY SUMMARY")
    else:
        for i in rec:   
            print('NOS/QUANTITY:-',i[1],'|','HSN CODE:-',i[2],'|','ITEM NAME:-',i[0])
            print('            ------------------------------             ')
            
# DELETING STOCK RECORD

def drop():
    c=input("Are you sure ?? (y/n)")
    if c=="Y" or c=="y":
        urs=con.cursor()
        curs.execute("drop table stock_summary")
        con.commit()
        print("Stock Summary deleted!")
    else:
        print("ERROR! Please try again!")
        main()

# USER DEFINED FUNCTION

def primary(hsn_code): 
    curs.execute("SELECT * FROM stock_summary where hsn_code='{}';".format(hsn_code))
    rec=curs.fetchall()
    if curs.rowcount==0:
        print('Primary key Turned On')
    else:
        print('Duplication Found. There is an item already added using the same HSN Code! ')
 
# USER DEFINED FUNCTION

def primary4update(hsn_code):
    curs.execute("SELECT * FROM stock_summary where hsn_code='{}';".format(hsn_code))
    rec=curs.fetchall()
    if curs.rowcount==0:
        print('No record Found for the given HSN CODE')
      
# USER DEFINED FUNCTION

def primary4delete(hsn_code):
    curs.execute("SELECT * FROM stock_summary where hsn_code='{}';".format(hsn_code))
    rec=curs.fetchall()
    if curs.rowcount==0:
        print('No record Found for the given name')
        
# HSN CODE

def browse():
    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT WEB BROWSER WITHIN SECONDS.PLEASE WAIT!")
    time.sleep(2)
    webbrowser.open("https://www.exportgenius.in/hs-code/india/building-materials")

# GST PRICE

def gstrate():
    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT WEB BROWSER WITHIN SECONDS.PLEASE WAIT!")
    time.sleep(2)
    webbrowser.open("https://cbic-gst.gov.in/gst-goods-services-rates.html")
 
# GST RATE

def gstcalc():
 J=float(input('Enter Original Price Of Good/Item'))
 R=float(input('Enter Rate'))
 FP=J+(J*R/100)
 print('RATE=',FP)


main()


    
       
    
       
    
        

      
