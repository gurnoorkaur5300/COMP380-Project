import tkinter as tk
from tkinter import messagebox
import sqlite3
from customer import Customer
from administrator import Administrator
import hashlib

class Database:
    """
    Manages interactions with the SQLite database.
    :author: Gregory Calderon and Gurnoor Kaur
    :version: 2.0

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
        self.conn =sqlite3.connect(dbFile, check_same_thread=False)
        self.buildTable()
        self.insert_sample_data()

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
                       reserveId INTEGER PRIMARY KEY AUTOINCREMENT,
                       customerId,
                       customerName TEXT,
                       hotelName TEXT,
                       roomId TEXT, 
                       roomNum INTEGER,
                       checkIn TEXT,
                       checkOut TEXT,
                       paid REAL, 
                       FOREIGN KEY (customerId) REFERENCES customers,
                       FOREIGN KEY (customerName) REFERENCES customers(name),
                       FOREIGN KEY (roomId) REFERENCES rooms(roomId)
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS hotels (
                       hotelId INTEGER,
                       hotelName TEXT,
                       location TEXT,
                       amenities TEXT,
                       priceRange TEXT,
                       photoLink TEXT
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                       roomId INTEGER,
                       roomNum TEXT,
                       hotelName TEXT,
                       location TEXT,
                       cost REAL
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                       paidId INTEGER PRIMARY KEY,
                       customerName TEXT,
                       cardNumber INTEGER,
                       securityHash TEXT,
                       expireDate TEXT,
                       address TEXT,
                       city TEXT,
                       zip INTEGER,
                       amount REAL, 
                       paidDate TEXT
                   
       )''')
        self.conn.commit()

        #check for default administrator. create if none exists.
        cursor.execute("SELECT COUNT(*) FROM administrators")
        count = cursor.fetchone()[0]

        if count == 0:
            defaultPassword = "default2Pass"
            defaultHashPass = hashlib.sha256(defaultPassword.encode()).hexdigest() 
            defaultAdmin = ("defAdmin", "defadmin@example.com", defaultHashPass)
            cursor.execute("INSERT INTO administrators (adminName, adminEmail, hashPass) VALUES (?,?,?)", (defaultAdmin))
        self.conn.commit()
    
    def insertPayment(self, payment):
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO payments (customerName, cardNumber, securityHash, expireDate, address, city, zip, amount, paidDate) VALUES (?,?,?,?,?,?,?,?,?)''', (payment.name, payment.number, payment.code, payment.expireDate, payment.address, payment.city, payment.zip, payment.paidAmount, payment.currentDate))
            self.conn.commit()
            messagebox.showinfo("Success", "Payment Accepted")
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"Database operation failed: {e}")
            
            
    def insertCustomer(self, customer): 
        """
        Inserts a new customer into the 'customers' table.

        Args:
            customer (Customer): The Customer object to be inserted into the database.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO customers (customerId, name, email, dob, phoneNumber, hashPass) VALUES (?,?,?,?,?,?)''', (customer.id,customer.name, customer.email, customer.dob, customer.phoneNumber, customer.hashPass))
            self.conn.commit()
            messagebox.showinfo("Success", "Account Created")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already in use. Please try a different email.")
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"Database operation failed: {e}") 



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
            foundCustomer = Customer(customer[0],customer[1],customer[2],customer[3],customer[4], customer[5])
            # cursor.execute('''SELECT checkIn FROM reservations WHERE customerId=?''', (id,))
            # reservations = cursor.fetchall()
            # foundCustomer.addReservations(reservations)
            return foundCustomer
        else:
            print("not found")
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
            foundCustomer = Customer(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5])
            
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
            print("not email match")
            return False
        
        if str(user.hashPass) == str(checkForHashPasswrd):
            # print("hash match")
            return True 
        else:
            print("not hash match" + str(checkForHashPasswrd))
            print("user hash", str(user.hashPass))
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
    
    # def getResInfo(self):
    #     """
    #     Retrieves reservation information from the 'reservations' table.

    #     Returns:
    #         list: A list of tuples containing reservation IDs, check-in/out dates, and payment status.
    #     """
    #     cursor=self.conn.cursor()
    #     cursor.execute("SELECT reserveId, checkIn, checkOut, paid FROM reservations")
    #     reservations = cursor.fetchall()
    #     return reservations
    
    
    # Formatting of Database spreadsheet fixed - Gurnoor (JOIN on Customer and ResInfo to put data together)
    def getResInfo(self):
        """
        Retrieves reservation information from the 'reservations' table, joined with the 'customers' table
        to include customer IDs.

        Returns:
            list: A list of tuples containing customer IDs, customer names, reservation IDs, check-in/out dates, and payment status.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT c.customerId, c.name, r.reserveId, r.checkIn, r.checkOut, r.paid 
            FROM reservations r
            INNER JOIN customers c ON c.name = r.customerName
        """)
        reservations_info = cursor.fetchall()
        return reservations_info


    
    def insertRoom(self, room):
        """Inserts a new room into the 'room' table.


        Args:
            room (Room): The Room object to be inserted into the database.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO rooms (roomId, hotelName, roomNum, location, cost) VALUES (?,?,?,?,?)''', (room.roomId, room.hotelName, room.roomNum, room.location, room.cost))
            self.conn.commit()
            messagebox.showinfo("Success", "Room added.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Duplicate entry or integrity constraint violation.")
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"Database operation failed: {e}") 
            
            
    def insertReservation(self, reservation):
        """
        Inserts a new reservation into the 'reservations' table.

        Args:
            
            customerName (str): The ID of the customer making the reservation.
            roomId (str): The ID of the room being reserved.
            paidId (int): The ID of the payment associated with the reservation.
            checkIn (str): The check-in date of the reservation.
            checkOut (str): The check-out date of the reservation.
            paid (float): The amount paid for the reservation.
            payDate (str): The date when the payment was made.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO reservations (customerId,customerName, hotelName, roomId, roomNum, checkIn, checkOut, paid)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                        (reservation.customerId, reservation.name, reservation.hotelName, reservation.roomId, reservation.roomNum,
                            reservation.checkIn, reservation.checkOut, reservation.cost))
            self.conn.commit()
            messagebox.showinfo("Success", "Reservation added.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Integrity constraint violation: Duplicate reservation ID.")
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"Database operation failed: {e}")


    def fetchHotelsByLocation(self, location):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM hotels WHERE location=?", (location,))
        return [{'hotelName': row[1], 'amenities': row[3].split(', '), 'price_range': row[4], 'photoLink': row[5]} for row in cursor.fetchall()]

    def fetchRoomByHotelAvail(self, hotel_name, checkin_date, checkout_date):
        cursor = self.conn.cursor()
        query = """
        SELECT r.roomId, r.roomNum, r.hotelName, r.location, r.cost FROM rooms r
        INNER JOIN hotels h ON r.hotelName = h.hotelName
        WHERE h.hotelName = ? AND r.roomId NOT IN (
            SELECT roomId FROM reservations
            WHERE NOT (checkOut <= ? OR checkIn >= ?)
        )
        """
        cursor.execute(query, (hotel_name, checkin_date, checkout_date))
        return [{'roomId': row[0], 'roomNum': row[1], 'hotelName': row[2], 'location': row[3], 'cost': row[4]} for row in cursor.fetchall()]

    def returnImgPath(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT photoLink FROM hotels")
        
        photoLink = cursor.fetchall()
        return photoLink
        

    def insert_sample_data(self):
        """Insert sample data if the hotels table is empty."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM hotels")
        if cursor.fetchone()[0] == 0:
            # Sample hotels data for each location
            hotels = [
                # New York Hotels
                ('11', 'Empire State Hotel', 'New York', 'Free WiFi, Pool', '$300-$500','assets/noImage.png'),
                ('12', 'Big Apple Hotel', 'New York', 'Gym, Free Breakfast', '$200-$400','assets/noImage.png'),
                ('13', 'Central Park Lodge', 'New York', 'Pet Friendly, Gym', '$350-$550','assets/noImage.png'),
                ('14', 'Times Square Suites', 'New York', 'Pool, Spa', '$400-$600','assets/noImage.png'),
                ('15', 'Liberty Inn', 'New York', 'Free WiFi, Free Parking', '$150-$350','assets/noImage.png'),
                ('16', 'Hudson River Hotel', 'New York', 'Restaurant, Bar', '$220-$420','assets/noImage.png'),
                ('17', 'Broadway Stay', 'New York', 'Luxury Spa, Fine Dining', '$500-$700','assets/noImage.png'),
                ('18', 'Wall Street Rooms', 'New York', 'Business Lounge, Express Check-in', '$450-$650','assets/noImage.png'),
    
                # Los Angeles Hotels
                ('21', 'Hollywood Lights Hotel', 'Los Angeles', 'Pool, Spa, Pet Friendly', '$320-$580','assets/holiday.png'),
                ('22','Beverly Hills Retreat', 'Los Angeles', 'Luxury Spa, Free WiFi', '$350-$650','assets/noImage.png'),
                ('23','Venice Beachfront Hotel', 'Los Angeles', 'Ocean View, Bar', '$300-$500','assets/noImage.png'),
                ('24','Downtown LA Apartments', 'Los Angeles', 'Gym, Urban View', '$250-$450','assets/noImage.png'),
                ('25','Sunset Boulevard Inn', 'Los Angeles', 'Rooftop Pool, Restaurant', '$400-$600','assets/noImage.png'),
                ('26','Santa Monica Pier Hotel', 'Los Angeles', 'Ocean View, Pool', '$350-$550','assets/noImage.png'),
                ('27','California Dreams', 'Los Angeles', 'Free Breakfast, Parking', '$200-$400','assets/noImage.png'),
                ('28','LA Grand Hotel', 'Los Angeles', 'Conference Rooms, Pool', '$450-$700','assets/noImage.png'),
    
                # Chicago Hotels
                ('31', 'Windy City Hotel', 'Chicago', 'Free WiFi, Gym', '$220-$400','assets/noImage.png'),
                ('32', 'Lake Shore Hotel', 'Chicago', 'Lake View, Restaurant', '$250-$450','assets/noImage.png'),
                ('33','Magnificent Mile High', 'Chicago', 'Shopping District, Spa', '$300-$500','assets/noImage.png'),
                ('34','Chicago River Hotel', 'Chicago', 'City View, Bar', '$350-$550','assets/noImage.png'),
                ('35','The Loop Loft', 'Chicago', 'Modern Gym, Business Suites', '$200-$300','assets/noImage.png'),
                ('36','Skyline Suites', 'Chicago', 'Skyline Views, Luxury Dining', '$400-$600','assets/noImage.png'),
                ('37','Grant Park Hotel', 'Chicago', 'Near Major Attractions, Pool', '$320-$520','assets/noImage.png'),
                ('38','Navy Pier Inn', 'Chicago', 'Near Attractions, Free WiFi', '$280-$480','assets/noImage.png'),
    
                # Houston Hotels
                ('41', 'Space City Inn', 'Houston', 'Free Parking, Gym', '$200-$350','assets/noImage.png'),
                ('42', 'Bayou City Hotel', 'Houston', 'River View, Spa', '$250-$400','assets/noImage.png'),
                ('43', 'Houston Heights Hotel', 'Houston', 'Urban Style, Bar', '$220-$420','assets/noImage.png'),
                ('44', 'Gulf Coast Suites', 'Houston', 'Pet Friendly, Free WiFi', '$180-$380','assets/noImage.png'),
                ('45', 'Energy Corridor Hotel', 'Houston', 'Business Facilities, Pool', '$300-$500','assets/noImage.png'),
                ('46', 'Medical Center Inn', 'Houston', 'Quiet Area, Accessible', '$250-$450','assets/noImage.png'),
                ('47', 'Star Houston Hotel', 'Houston', 'Luxury Amenities, Fine Dining', '$350-$550','assets/noImage.png'),
                ('48', 'Houston Station Stay', 'Houston', 'Historic Building, Modern Amenities', '$320-$520','assets/noImage.png'),
    
                # Miami Hotels
                ('51', 'Sunny Florida Resort', 'Miami', 'Ocean View, Pool, Spa', '$250-$450','assets/noImage.png'),
                ('52', 'Miami Beach Hotel', 'Miami', 'Beach Access, Pool', '$300-$500','assets/noImage.png'),
                ('53', 'Coral Gables Retreat', 'Miami', 'Luxury Spa, Fine Dining', '$350-$650','assets/noImage.png'),
                ('54', 'Downtown Miami Suites', 'Miami', 'Urban View, Free WiFi', '$200-$400','assets/noImage.png'),
                ('55', 'South Beach Inn', 'Miami', 'Nightlife Access, Bar', '$400-$600','assets/noImage.png'),
                ('56', 'Biscayne Bay Hotel', 'Miami', 'Bay View, Restaurant', '$220-$420','assets/noImage.png'),
                ('57', 'Key Biscayne Resort', 'Miami', 'Island Setting, Luxury Spa', '$450-$700','assets/noImage.png'),
                ('58', 'Ocean Drive Stay', 'Miami', 'Art Deco Style, Ocean Front', '$500-$800','assets/noImage.png'),
            ]
            cursor.executemany('INSERT INTO hotels (hotelId, hotelName, location, amenities, priceRange, photoLink) VALUES (?,?,?,?,?,?)', hotels)
    
            # Sample rooms for each hotel
            roomTemplate = [(hotel[0], hotel[1], f'{num:03}', hotel[1], round(float(hotel[4].split('-')[0].strip('$')) + num * 10, 2)) for hotel in hotels for num in range(101, 106)]
            cursor.executemany('INSERT INTO rooms (roomId, hotelName, roomNum, location, cost) VALUES (?,?,?,?,?)', roomTemplate)
            # self.insertRoom(roomTemplate)
    
            self.conn.commit()
    