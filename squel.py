
import mysql.connector
from hdbcli import dbapi
from flask import Flask, request, render_template
import pymysql
import  mysql

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ULGROWTH20",
)



cursor = connection.cursor()
query ="create table practice"

cursor.execute(query)
cursor.close()
connection.close()