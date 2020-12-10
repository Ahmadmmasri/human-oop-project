import sqlite3
import time
import os


class humans:
    # Default Constructer
    def __init__(self, Name, LastName, Email, Age, Gender):
        name = Name
        Lastname = LastName
        email = Email
        age = Age
        gender = Gender

        print("Welcome "+name)

# setter and getter for each attribute.
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, Gender):
        self.gender = Gender

    def getGender(self):
        return self.gender

    def setLastName(self, Last_Name):
        self.Lastname = Last_Name

    def getLastName(self):
        return self.Lastname
# end /////////////////////////////////


class start(humans):

    
    # input data
    def Test():
        userList = list()
        name = input("Enter your name please: ")
        last_name = input("enter your last name please: ")
        email = input("Enter your e-mail please: ")
        age = input("enter your age please: ")
        gender = input("enter your gender please: ")
        print()
        

    
    # testCase
        p= [name, last_name, email, age, gender]
        copy = humans(p[0], p[1], p[2], p[3], p[4])
        copy.setName(p[0])
        copy.setLastName(p[1])
        copy.setEmail(p[2])
        copy.setAge(p[3])
        copy.setGender(p[4])

        
        userList.append(p)

   # print(copy.getName()," ", copy.getLastName()," ", copy.getEmail()," ", copy.getAge()," ", copy.getGender())
   # or u can use this code
        print(userList[0])
        time.sleep(1)
        print(f"{p[0]} {p[1]} has added successfully")
        

#save data in text
        fname = input('Enter file name to save: ')
        if ( len(fname) < 1 ) : fname = 'default.txt'
        print("default.text...")
        time.sleep(1)
        fh = open(fname,"w+")
        for i in range(1):
            fh.write(f"{userList} %d\r\n" % (i+1))
        print("data added successfully to \"default\" file text")
        fh.close() 
	   
	    
        key = p
# create sql database
        conn = sqlite3.connect('humans.sqlite')
        cur = conn.cursor()
        
        
        cur.execute('''
            DROP TABLE IF EXISTS humans''')

# excute commands
        cur.execute('''
            CREATE TABLE Humans (name TEXT, lastName TEXT, email TEXT,age INTEGER,gender INTEGER)''')

        cur.execute('''INSERT INTO Humans (name, email, age, gender, lastName)
			VALUES ( ?, ?, ?, ?, ? )''', (key[0], key[1], key[2], key[3], key[4]))
        row = cur.fetchone()
        if row is not None:
            cur.execute('SELECT name FROM Humans WHERE name = ? ', (k[0], ))
        conn.commit()
        print("writing data to your database...")
        time.sleep(1)
        print("data added successfully to default human database.")
        Test()

    Test()

   