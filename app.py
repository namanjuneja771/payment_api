from flask import Flask, redirect, url_for, request,render_template,jsonify
import json
import os
import sqlite3
app=Flask(__name__)
@app.route("/signup",methods=['POST'])
def signup():
	req=request.get_json()
	ph=req["phone_number"]
	pas=req["password"]
	bal=req["initial_balance"]
	if(bal>=5000):		
		connection=sqlite3.connect("project.db")
		cursor=connection.cursor()
		req=cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';").fetchall()
		flg1=0
		flg2=0		
		for i in req:		
			if("money" in i[0]):
				flg1=1
			if("logs" in i[0]):
				flg2=1
		if(flg1==0):
			cursor.execute("CREATE TABLE money(phone_number INTEGER PRIMARY KEY, password TEXT, balance INTEGER)")
		if(flg2==0):
			cursor.execute("CREATE TABLE logs(phone_number INTEGER, transaction_type TEXT, amount INTEGER, balance_before INTEGER,balance_after INTEGER)")
		rows=cursor.execute("SELECT phone_number FROM money").fetchall()
		for row in rows:		
			if(ph==row[0]):
				return "Wallet account for "+str(ph)+" already exists"
		cursor.execute("INSERT INTO money VALUES({0},'{1}',{2})".format(ph,str(pas),bal))
		cursor.execute("INSERT INTO logs VALUES({0},'{1}',{2},{3},{4})".format(ph,"credit",bal,0,bal))
		connection.commit()
		return "Wallet created succesfully with balance "+str(bal)
	else:
		return "Wallet account can not be create das initial balance should be greater than 5000"
	return str(ph)
@app.route("/credit",methods=['POST'])
def credit():
	req=request.get_json()
	ph=req["phone_number"]
	pas=req["password"]
	amt=req["amount"]
	connection=sqlite3.connect("project.db")
	cursor=connection.cursor()
	numbers=cursor.execute("SELECT * FROM money").fetchall()
	flg=0	
	for num in numbers:
		if(num[0]==ph and num[1]==pas):
			flg=1
			break
		elif(num[0]==ph and num[1]!=pas):
			return "Incorrect password"
	if(flg==0):
		return str(ph)+" doesn't have a wallet account yet"
	curbal=cursor.execute("select balance from money where phone_number={0}".format(ph)).fetchall()
	curbal=curbal[0][0]
	newamt=curbal+amt
	cursor.execute("update money set balance={0} where phone_number={1}".format(newamt,ph))
	cursor.execute("INSERT INTO logs VALUES({0},'{1}',{2},{3},{4})".format(ph,"credit",amt,curbal,curbal+amt))
	connection.commit()	
	return "Wallet account credited with Rs "+str(amt)+".\n"+"Available balance = "+str(newamt)
@app.route("/debit",methods=['POST'])
def debit():
	req=request.get_json()
	ph=req["phone_number"]
	pas=req["password"]
	amt=req["amount"]
	connection=sqlite3.connect("project.db")
	cursor=connection.cursor()
	numbers=cursor.execute("SELECT * FROM money").fetchall()
	flg=0	
	for num in numbers:
		if(num[0]==ph and num[1]==pas):
			flg=1
			break
		elif(num[0]==ph and num[1]!=pas):
			return "Incorrect password"
	if(flg==0):
		return str(ph)+" doesn't have a wallet account yet"
	curbal=cursor.execute("select balance from money where phone_number={0}".format(ph)).fetchall()
	curbal=curbal[0][0]
	if(curbal-amt<5000):
		return "This transaction can't be performed as it causes the balance to go below 5000"
	newamt=curbal-amt
	cursor.execute("update money set balance={0} where phone_number={1}".format(newamt,ph))
	cursor.execute("INSERT INTO logs VALUES({0},'{1}',{2},{3},{4})".format(ph,"debit",amt,curbal,curbal-amt))
	connection.commit()	
	return "Wallet account debited with Rs "+str(amt)+".\n"+"Available balance = "+str(newamt)
@app.route("/checkb",methods=['POST'])
def checkb():
	req=request.get_json()
	ph=req["phone_number"]
	pas=req["password"]
	connection=sqlite3.connect("project.db")
	cursor=connection.cursor()
	numbers=cursor.execute("SELECT * FROM money").fetchall()
	flg=0	
	for num in numbers:
		if(num[0]==ph and num[1]==pas):
			flg=1
			break
		elif(num[0]==ph and num[1]!=pas):
			return "Incorrect password"
	if(flg==0):
		return str(ph)+" doesn't have a wallet account yet"
	curbal=cursor.execute("select balance from money where phone_number={0}".format(ph)).fetchall()
	curbal=curbal[0][0]
	return "The wallet account linked with number "+str(ph)+" has current balance = "+str(curbal)
if __name__=='__main__':
	app.run(port=7000)
