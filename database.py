import tkinter as tk
from tkinter import messagebox
import sqlite3
from customer import Customer
from administrator import Administrator
import hashlib

class Database:
    """
    Manages interactions with the SQLite database.
    :author: Gregory Calderon
    :version: 1.0

    Attributes:
        conn (sqlite3.Connection): Connection to the SQLite database.
    
    Methods:
        __init__: Initializes the Database object.
        buildTable: Builds the necessary tables in the database if they don't exist.
        insertCustomer: Inserts a new customer into the 'customers' table.
        getEmail: Retrieves customer information based on their email address.
        getReservations: Retrieves reservations for a specific customer.
        deleteReservation: Deletes a reservation from the 'reservations' table.
        getAdminEmail: Retrieves administrator information based on their email address.
        isVerified: Verifies the login credentials of a customer or administrator.
        getCustomerInfo: Retrieves customer IDs and names from the 'customers' table.
        getResInfo: Retrieves reservation IDs, check-in/out dates, and payment status from the 'reservations' table.
    """
    def __init__(self, dbFile="defaultDatabase.db"):
        """
        Initializes the Database object.

        Args:
            dbFile (str): The name of the SQLite database file.
        """
        self.conn =sqlite3.connect(dbFile)
        self.buildTable()

    def buildTable(self):
        """
        Creates necessary tables in the database if they don't exist.
        """
        cursor = self.conn.cursor() #create a cursor object to traverse records
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                       customerId INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT,
                       email TEXT UNIQUE,
                       dob TEXT, 
                       phoneNumber TEXT,
                       hashPass TEXT

        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS administrators (
                       adminId INTEGER PRIMARY KEY AUTOINCREMENT, 
                       adminName TEXT,
                       adminEmail TEXT UNIQUE,
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

        #check for default administrator. create if none exists.
        cursor.execute("SELECT COUNT(*) FROM administrators")
        count = cursor.fetchone()[0]

        if count == 0:
            defaultPassword = "default2Pass"
            defaultHashPass = hashlib.sha256(defaultPassword.encode()).hexdigest() 
            defaultAdmin = ("defAdmin", "defadmin@example.com", defaultHashPass)
            cursor.execute("INSERT INTO administrators (adminName, adminEmail, hashPass) VALUES (?,?,?)", (defaultAdmin))
        self.conn.commit()

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
        """
        Inserts a new customer into the 'customers' table.

        Args:
            customer (Customer): The Customer object to be inserted into the database.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO customers (name, email, dob, phoneNumber, hashPass) VALUES (?,?,?,?,?)''', (customer.name, customer.email, customer.dob, customer.phoneNumber, customer.hashPass))
            self.conn.commit()
            messagebox.showinfo("Success", "Account Created")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already in use. Please try a different email.")


    def getById(self, id):
        """
        Retrieves customer information based on their customerId.

        Args:
            customerId (str): The customerId of the customer.

        Returns:
            Customer: A Customer object containing the customer's information, or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM customers WHERE customerId=?''', (id,))
        customer = cursor.fetchone()

        if customer is not None:
            foundCustomer = Customer(customer[1],customer[2],customer[3],customer[4], customer[5])
            return foundCustomer
        else:
            return None 
        

    def getEmail(self, email):
        """
        Retrieves customer information based on their email address.

        Args:
            email (str): The email address of the customer.

        Returns:
            Customer: A Customer object containing the customer's information, or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM customers WHERE email=?''', (email,))
        customer = cursor.fetchone()

        if customer is not None:
            foundCustomer = Customer(customer[1],customer[2],customer[3],customer[4], customer[5])
            return foundCustomer
        else:
            return None 
        
    

    def getReservations(self, customerId):
        """
        Retrieves reservations for a specific customer.

        Args:
            customerId (int): The ID of the customer.

        Returns:
            list: A list of check-in dates for the customer's reservations.
        """
        cursor = self.conn.cursor()
        cursor.execute('''SELECT checkIn FROM reservations WHERE customerId=?''', (customerId,))
        reservations = cursor.fetchall()
        return [res[0] for res in reservations] # return first checkIn date 
    
    def deleteReservation(self, reserveId):
        """
        Deletes a reservation from the 'reservations' table.

        Args:
            reserveId (int): The ID of the reservation to be deleted.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''DELETE FROM reservations WHERE reserveId=?''', (reserveId,))
            self.conn.commit()
            messagebox.showinfo("Success", "Reservation cancelled successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to cancel reservation: {e}")

    def getAdminEmail(self, adminEmail):
        """
        Retrieves administrator information based on their email address.

        Args:
            adminEmail (str): The email address of the administrator.

        Returns:
            Administrator: An Administrator object containing the administrator's information, or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM administrators WHERE adminEmail=?''', (adminEmail,))
        adminData = cursor.fetchone()

        if adminData is not None:
            admin = Administrator(adminData[1],adminData[2],adminData[3])
            return admin
        else:
            return None 

    def isVerified(self, checkForEmail, checkForHashPasswrd, isCustomer):
        """
        Verifies the login credentials of a customer or administrator.

        Args:
            checkForEmail (str): The email address to be verified.
            checkForHashPasswrd (str): The hashed password to be verified.
            isCustomer (int): Indicates whether the user is a customer (1) or an administrator (0).

        Returns:
            bool: True if the credentials are verified, False otherwise.
        """
        if isCustomer==1:
            user = self.getEmail(checkForEmail)
            
        else: 
            user = self.getAdminEmail(checkForEmail)

        if user is None:
            #print("not email match")
            return False
        
        if str(user.hashPass) == str(checkForHashPasswrd):
            #print("hash match")
            return True 
        else:
            #print("not hash match" + "" + str(customer.hashPass)+ "" + str(checkForHashPasswrd))
            return False
        

    def getCustomerInfo(self):
        """
        Retrieves customer IDs and names from the 'customers' table.

        Returns:
            list: A list of tuples containing customer IDs and names.
        """
        cursor=self.conn.cursor()
        cursor.execute("SELECT customerId, name FROM customers")
        customers = cursor.fetchall()
        return customers
    
    def getResInfo(self):
        """
        Retrieves reservation information from the 'reservations' table.

        Returns:
            list: A list of tuples containing reservation IDs, check-in/out dates, and payment status.
        """
        cursor=self.conn.cursor()
        cursor.execute("SELECT reserveId, checkIn, checkOut, paid FROM reservations")
        reservations = cursor.fetchall()
        return reservations
    
    

    