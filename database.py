import tkinter as tk
from tkinter import messagebox
import sqlite3
from customer import Customer


class Database:
    def __init__(self, dbFile="defaultDatabase.db"):
        self.conn =sqlite3.connect(dbFile)
        self.buildTable()

    def buildTable(self):
        cursor = self.conn.cursor() #create a cursor object to traverse records
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                       customerId INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT,
                       email TEXT UNIQUE,
                       dob TEXT, 
                       phoneNumber TEXT,
                       hashPass TEXT

        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                       reserveId INTEGER PRIMARY KEY,
                       customerId INTEGER, 
                       roomId TEXT, 
                       paidId INTEGER, 
                       checkIn TEXT,
                       checkOut TEXT,
                       paid REAL,
                       payDate TEXT,
                       FOREIGN KEY (customerId) REFERENCES customers(customerId),
                       FOREIGN KEY (roomId) REFERENCES rooms(roomId),
                       FOREIGN KEY (paidId) REFERENCES payment(paidId)
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                       roomId TEXT PRIMARY KEY,
                       roomNumber INTEGER,
                       roomType TEXT,
                       capacity INTEGER,
                       hotelId TEXT,
                       hotelName TEXT,
                       location TEXT,
                       cost REAL
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                       paidId INTEGER PRIMARY KEY,
                       customerId INTEGER,
                       amount REAL, 
                       paidDate TEXT,
                       FOREIGN KEY (customerId) REFERENCES customers(customerId)
                       

       )''')
    

    def insertCustomer(self, customer): 
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO customers (name, email, dob, phoneNumber, hashPass) VALUES (?,?,?,?,?)''', (customer.name, customer.email, customer.dob, customer.phoneNumber, customer.hashPass))
            self.conn.commit()
            messagebox.showinfo("Success", "Account Created")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already in use. Please try a different email.")


    def getEmail(self, email):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM customers WHERE email=?''', (email,))
        customer = cursor.fetchone()

        if customer is not None:
            foundCustomer = Customer(customer[1],customer[2],customer[3],customer[4], customer[5])
            return foundCustomer
        else:
            return None 
    

    def getReservations(self, customerId):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT checkIn FROM reservations WHERE customerId=?''', (customerId,))
        reservations = cursor.fetchall()
        return [res[0] for res in reservations] # return first checkIn date 
    
    def deleteReservation(self, reserveId):
        cursor = self.conn.cursor()
        try:
            cursor.execute('''DELETE FROM reservations WHERE reserveId=?''', (reserveId,))
            self.conn.commit()
            messagebox.showinfo("Success", "Reservation cancelled successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to cancel reservation: {e}")

    def isVerified(self, checkForEmail, checkForHashPasswrd):
        customer = self.getEmail(checkForEmail)

        if customer is None:
            #print("not email match")
            return False
        
        if str(customer.hashPass) == str(checkForHashPasswrd):
            #print("hash match")
            return True 
        else:
            #print("not hash match" + "" + str(customer.hashPass)+ "" + str(checkForHashPasswrd))
            return False
    

