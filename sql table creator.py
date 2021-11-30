###MYSQL CONTENT###
import mysql.connector
db1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
cur=db1.cursor()

cur.execute("create database if not exists hotel")

cur.execute("use hotel")

cur.execute("create table if not exists guest"
            "("
            "ID int(11) primary key,"
            "FIRSTNAME varchar(20),"
            "LASTNAME varchar(20),"
            "MDATE date,"
            "ADDRESS varchar(30),"
            "CITY varchar(20),"
            "PIN char(6),"
            "MOBILENO char(10)"
            ")"
            )



cur.execute("create table if not exists room"
            "("
            "ID int(11) primary key,"
            "ROOMNO int(20) ,"
            "FUNC_STATUS tinyint(20),"
            "ROOM_TYPE_ID int(11) "
            ")")



cur.execute("create table if not exists reservation"
            "("
            "ID int(11) primary key,"
            "CINDATE date,"
            "COUTDATE date,"
            "MADEBY varchar(20),"
            "GUESTID int(11) ,"
            "RESERVATIONDATE date,"
            "CANCELLED tinyint(1),"
            "CANCELLEDDATE date,"
            "NO_OF_DAYS_STAY int(11),"
            "NOOFROOMS int(11),"
            "ROOMTYPEID int(11),"
            "BILLPAID tinyint(1)"
            ")")


cur.execute("create table if not exists hostedat"
            "("
            "ID int(11) primary key,"
            "GUESTID int(20) ,"
            "OCCUPIEDROOMID int(11) "
            ")")



cur.execute("create table if not exists occupiedroom"
            "("
            "ID int(11) primary key,"
            "CINDATE  date,"
            "COUTDATE  date,"
            "CINTIME varchar(15),"
            "COUTTIME varchar(15),"
            "ROOMID int(11) ,"
            "RESERVATIONID int(11) "
            ")")


cur.execute("create table if not exists reservedroom"
            "("
            "ID int(11) primary key,"
            "ROOMNO int(11) ,"
            "ROOMTYPEID int(11) ,"
            "RESERVATIONID int(11) ,"
            "STATUS tinyint(1) "
            ")")



cur.execute("create table if not exists roomtype"
            "("
            "ID int(11) primary key,"
            "TYPE varchar(30) ,"
            "CAPACITY int(11),"
            "RENTPD decimal(10,0) "
            ")")

