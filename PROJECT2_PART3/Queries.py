# AUTHOR RISHI KUMAR SONI , UTA ID : 1001774020
import mysql.connector
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine
import datetime as dt
from mysql.connector import errorcode
import traceback
from prettytable import PrettyTable
from texttable import Texttable
from dateutil.relativedelta import *
import time
from datetime import date

def db_connection():
    try:
        global mydb
        mydb = mysql.connector.connect(
            host="acadmysqldb001p.uta.edu", # HOST NAME
            user="rxs4020", 	#USERNAME
            password="Rishisoni@16", #PASSWORD 
            database="rxs4020",	# DATABASE NAME
            db='mydb'
        )
   
        global cursor 
        cursor = mydb.cursor()
        global engine
        engine = create_engine('mysql+mysqlconnector://rxs4020:Rishisoni@16@:3306/rxs4020')
        return "DB Connected!"
    except Exception as e:
        return e
 
def display_library_staff():
    table = PrettyTable(['Index','SSN','Name','Staff Type'])
    sql_select_Query = "select * from library_staff"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1
    for row in records:
        table.add_row([index,row[0],row[1],row[2]])
        index+=1

    print(table)

def display_book():
    table = PrettyTable(['Index','ISBN','Title','Author','Subject Area','Language','Binding Type','Edition'])
    sql_select_Query = "select * from book"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        index+=1

    print(table)    

def display_books_available_in_lib():
    table = PrettyTable(['Index','ISBN','Can be rented flag','Total No Copies','No of copies lented','Book Description','Book Type'])
    sql_select_Query = "select * from books_available_in_lib"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4],row[5]])
        index+=1

    print(table)
    
def display_books_required():
   # table = PrettyTable(['Index','ISBN','No of required copies'])
    table = PrettyTable(['ISBN','No of required copies'])

    sql_select_Query = "select * from books_required"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1
    for row in records:
        table.add_row([index,row[0],row[1]])
        index+=1

    print(table)
    
def display_library_member():
    table = PrettyTable(['Index','SSN','Name','Campus Address','Home Address','Phone Number','Card Number','Card Expiry Date','Is Professor Flag','Member Type'])
    sql_select_Query = "select * from library_member"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        index+=1

    print(table)
    
def display_issue_book():
    table = PrettyTable(['Index','Issue Id','Member SSN','Staff SSN','ISBN','Issue Date','Notice Date','Grace Period Days','Book Due Date'])
    sql_select_Query = "select * from issue_book"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
        index+=1

    print(table)
    
def insert_library_member():
    try:
        print("\n\nEnter the Library member information: ")
        ssn = input("Enter Your'e SSN (not more than 10 digits/characters) :")
        name = input("Enter Person's name: ")
        camp_add = input("Enter First Address: ")
        home_add = input("Enter Second address: ")
        phone = input("Enter phone number(only Digits) : ")
        card = input("Enter Youre Card number: ")
        card_date = input("Enter card expiry date(mm/dd/yy) : ")
        member_flag = input("Is member work as professor(1 means yes/0 means no): ")
        member_type = input("Enter member type(active or Inactive): ")

        mycursor = mydb.cursor()
        card_date = pd.to_datetime(card_date)
        sql = "INSERT INTO library_member VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (ssn, name, camp_add, home_add, phone, card, card_date, member_flag, member_type)
        mycursor.execute(sql, val)

        mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)
        print("\n")
        
    except mysql.connector.Error as error :
        print("Failed to insert into MySQL table {}".format(error))
        print("\n")
        
        
def insert_book():
    try:
        print("\n\nEnter new Book information: ")
        isbn = input("Enter Book ISBN: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        sub_area = input("Enter Book Genre: ")
        lang = input("Enter language in which Book is written: ")
        binding_type = input("Enter Binding type: ")
        edition = input("Enter Book edition: ")

        mycursor = mydb.cursor()
        
        sql = "INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (isbn, title, author, sub_area, lang, binding_type, edition)
        mycursor.execute(sql, val)

        mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)
        print("\n")
        
    except mysql.connector.Error as error :
        print("Failed to insert into MySQL table {}".format(error))
        print("\n")
        
def borrow_book():
    print("\nBorrowing Book information!")
    flag = True
    while(flag):
        ssn = input("Enter member ssn: ")
        sql_select_Query = "select * from library_member where SSN='{}'".format(ssn)
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        memberRecords = cursor.fetchall()
        if(len(memberRecords)==0):
            print("No member found! Enter valid ssn.")
            print("\n")
        else:

            flag = False

    flag = True
    while(flag):
        isbn = input("Enter Book ISBN: ")
        sql_select_Query = "select * from book where ISBN='{}'".format(isbn)
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        bookRecords = cursor.fetchall()
        if(len(bookRecords)==0):
            print("No Book Found! Please Enter valid ISBN.")
            print("\n")
        else:

            flag = False

    sql_select_Query = "select max(issue_id) from issue_book"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    issue_id = records[0][0]+1
    issue_date = dt.datetime.now()

    issue_date = pd.to_datetime(issue_date)

    is_professor_flag = memberRecords[0][7]

    if(is_professor_flag==1):
        due_date = issue_date + relativedelta(months=+3)
        grace_period = 14
        notice_date = due_date + relativedelta(days=-14)
    else:
        due_date = issue_date + relativedelta(days=+21)
        grace_period = 7
        notice_date = due_date + relativedelta(days=-7)

    mycursor = mydb.cursor()
    #card_date = pd.to_datetime(card_date)
    sql = "INSERT INTO issue_book VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (issue_id, ssn, '1451648537', isbn, issue_date, notice_date, grace_period, due_date)
    mycursor.execute(sql, val)

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

    
def return_book():
    print("\nReturn a book!")
    flag = True
    while(flag):
        ssn = input("Enter Member SSN: ")
        sql_select_Query = "select * from issue_book where MEMBER_SSN='{}'".format(ssn)
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        memberRecords = cursor.fetchall()

        if(len(memberRecords)==0):
            print("You dont have any book issued!")
        else:
            flag = False

    flag = True
    while(flag):
        isbn = input("Enter book ISBN: ")
        sql_select_Query = "select * from issue_book where ISBN='{}'".format(isbn)
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        bookRecords = cursor.fetchall()

        if(len(bookRecords)==0):
            print("No book found! Enter valid ISBN.")
        else:
            flag = False


    file=open("receipt.txt","w+")

    file.write("Return Receipt\n\n")
    file.write("Member SSN: {}\n".format(memberRecords[0][1]))
    file.write("Book ISBN: {}\n".format(bookRecords[0][3]))
    file.write("Issue date: {}\n".format(bookRecords[0][4]))
    file.write("Return date: {}".format(pd.to_datetime(dt.datetime.now())))
    file.close()
    print("Data is saved to receipt.txt file.")
    mycursor = mydb.cursor()
    sql = "DELETE FROM issue_book WHERE MEMBER_SSN='{}' and ISBN='{}'".format(ssn,isbn)

    mycursor.execute(sql)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def renew_membership():
    todays_date = date.today()
    now_date = dt.datetime.now()
    memberDate = input("Enter card expiry date(yyyy-mm-dd) :")
    year, month, day = map(int, memberDate.split('-'))
    date1 = dt.date(year, month, day)

    sql_select_Query = "select * from library_member where CARD_EXPIRY_DATE='{}'".format(date1)
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    memberRecords = cursor.fetchall()

    new_date = date1 + relativedelta(years=+4)

    mycursor = mydb.cursor()
    sql = "UPDATE library_member SET CARD_EXPIRY_DATE = '{}' WHERE CARD_EXPIRY_DATE = '{}'".format(new_date,date1)
    mycursor.execute(sql)
    mydb.commit()


    table = PrettyTable(['Index','Name','SSN','Card Number','Old Card Expiry Date','New Card Expiry date'])
    index = 1
    for row in memberRecords:
        table.add_row([index,row[1],row[0],row[5],row[6],new_date])
        index+=1
    print(table)
    
def weekly_report():
    print("Generate report!")
    start = input("Enter start date(yyyy-mm-dd): ")
    end = input("Enter end date(yyyy-mm-dd): ")

    sql_select_Query = "select b.isbn, ib.issue_date, count(*) as number_of_copies, datediff(ib.book_due_date, ib.issue_date) as no_of_days, b.author, b.title, lm.ssn, lm.name from issue_book as ib, library_member as lm, book as b where ib.issue_date between '{}' and '{}' and b.isbn=ib.isbn and lm.ssn=ib.member_ssn group by b.isbn".format(start,end)
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1
    table = PrettyTable(['Index','Book Title','Book Author','Book ISBN','Member Name','Member SSN','Issue Date','No of Copies','Loan Days'])

    for row in records:
        table.add_row([index,row[5],row[4],row[0],row[7],row[6],row[1],row[2],row[3]])
        index+=1

    print("Report generated to report.txt file!")
    file=open("WeeklyReport.txt","w+",encoding='utf-8')

    file.write("Weekly Report!\n\n")

    file.write(str(table))

    file.close()


def trigger_membership_renewal():
    print("Triggering ---> Generating Membership Renewal trigger!")
    todays_date = date.today()
    '''ssn = input("Enter member SSN : ")
    sql_select_Query = "select ssn,name, phone_number,card_number,card_expiry_date from library_member where ssn = '{}' card_expiry_date < '{}'".format(ssn,todays_date)'''
    sql_select_Query = "select ssn,name, phone_number,card_number,card_expiry_date from library_member where card_expiry_date < '{}'".format(todays_date)
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1
    table = PrettyTable(['Index','SSN','Name','Phone Number','Card Number','Card expiry date'])

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4]])
        index+=1

    print("\n MemberShip Renewal Report generated to MembershipRenewal.txt File!")
    file=open("MembershipRenewal.txt","w+",encoding='utf-8')

    file.write("Membership Renewal Report!\n\n")

    file.write(str(table))

    file.close()

def trigger_outstanding_overdue_book():
    print("Generating Outstanding Overdue book trigger!\n")
    todays_date = date.today()
    sql_select_Query = "select l.ssn, l.name, i.isbn,b.title,b.author,i.issue_date,i.book_due_date from library_member as l, issue_book as i,book as b where i.member_ssn = l.ssn and i.isbn = b.isbn and i.book_due_date < '{}'".format(todays_date)
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    index = 1
    table = PrettyTable(['Index','SSN','Name','ISBN','Book Title','AuthorName','Issue_Date','Book_Due_Date'])

    for row in records:
        table.add_row([index,row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        index+=1

    print("OverDue book Report generated to OverDueBook.txt file!")
    file=open("OverDueBook.txt","w+",encoding='utf-8')

    file.write("Outstanding OverDueBook Report!\n\n")

    file.write(str(table))

    file.close()
    