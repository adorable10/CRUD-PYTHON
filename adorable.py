import pymysql
import sys

 
connection = pymysql.connect(
    host='localhost',
    user='elmie',
    password='adorable',
    db='crud',
)

def add():
    First_Name = input("Enter first_name: ")
    Last_Name = input("Enter last name: ")
    Address = input("Enter address: ")
    Number = input("Enter number: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO phonebook(`First_Name`, `Last_Name`, `Address`, `Number`) VALUES (%s, %s, %s ,%s)"
            try:
                cursor.execute(sql, (First_Name, Last_Name, Address, Number))
                print("Contact added successfully")
            except:
                print("Fill-in all the entry!")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("phonebook data\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from phonebook"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("id\tFirst_name\t\tLast_name\tAddress\t\tNumber")
            for row in results :
                print(str(row[0]), "\t",row[1],"\t\t\t",(row[2]),"\t\t",row[3],"\t",row[4])

        connection.commit()
    finally:
        print ("\n")
        return
def update():
    read()
    print("")
    ID = input("Enter the id of the phonebook to update: ")
    First_Name = input("Enter new firstname: ")
    Last_Name = input("Enter new lastname: ")
    Address = input("Enter new address: ")
    Number = input("Enter new number: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE phonebook SET `First_name`=%s, `Last_name`=%s , `Address`=%s , `Number`=%s  WHERE `id`=%s"
            try:
                cursor.execute(sql, (First_Name, Last_Name, Address, Number, ID))
                print("Successfully Updated...")
            except:
                print("Fill-in all the entry!")
 
        connection.commit()
    finally:
        print ("\n")
        return
def delete():
    read()
    print("")
    ID = input("Enter the id of the phonebook to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Phonebook WHERE id = %s"
            try:
                cursor.execute(sql, (ID))
                print("Successfully Deleted...")
            except:
                print("Fill-in all the entry!")
 
        connection.commit()
    finally:
        print ("\n")
        return

def exit():
    sys.exit(0)

choice = 1
while choice:
    print ("\n\nPhonebook\n\n")
    print ("[a] = Create a new data\n")
    print ("[b] = Read data\n")
    print ("[c] = Update data\n")
    print ("[d] = Delete data\n")
    print ("[e] = Exit\n")

    choice = input("Choices: ")

    if choice in "Aa":
        add()
    elif choice in "Bb":
        read()
    elif choice in "Cc":
        update()
    elif choice in "Dd":
        delete()
    elif choice in "Ee":
        exit()
        
    else:
        print ("Invalid Input!\n")
        choice = 1
