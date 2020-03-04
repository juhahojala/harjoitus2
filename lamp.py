#!/usr/bin/env python

import os
'''
#luetaan globaaleja ympäristömuuttujia käyttöjärjestelmästä
'''
print(os.environ["USER"])
print(os.environ["MY_DATE"])
apu1=os.environ["USER"]
apu2=os.environ["MY_DATE"]


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testaaja",
  passwd="salasana",
  database="testi"
)

mycursor = mydb.cursor()

sql = "INSERT INTO loki (kayttaja, aika) VALUES (%s, %s)"
val = (apu1, apu2)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
