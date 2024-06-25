import mysql.connector
#import random,string
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root123',
    auth_plugin = 'mysql_native_password')
print(mydb)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("DROP DATABASE IF EXISTS RESTAURANT_MANAGEMENT")
mycursor.execute("CREATE DATABASE RESTAURANT_MANAGEMENT")
mycursor.execute("USE RESTAURANT_MANAGEMENT")

mycursor.execute("DROP TABLE IF EXISTS STARTERS")
mycursor.execute('''
CREATE TABLE STARTERS (
    starter_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL)
    ''')
mycursor.execute('''INSERT INTO STARTERS VALUES	 
    (1,'Spring Roll',145),
    (2,'Chilly Paneer Dry',195),
    (3,'Veg. Manchurian Dry',153),
    (4,'Potatoes in Honey & Chilly',175),
    (5,'Fried Vegetables in Salt & Papper',190),
    (6,'Crispy Spinach & Baby - Corn',198),
    (7,'Chilly Mushroom Dry',193)''')



mycursor.execute("DROP TABLE IF EXISTS MAIN_COURSE")
mycursor.execute('''
CREATE TABLE MAIN_COURSE (
    main_course_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL)
    ''')
mycursor.execute('''INSERT INTO MAIN_COURSE VALUES
    (1,'Veg Chopsouey',195),
    (2,'Chilly Paneer Gravy',205),
    (3,'Manchurian Gravy',175),
    (4,'Sweet & Sour Veg.',175),
    (5,'Mix. Veg. in Hot Garlic Sauce',185),
    (6,'Shreded Potatoes in Hot Garlic Sauce',153)''')


mycursor.execute("DROP TABLE IF EXISTS BREADS")
mycursor.execute('''
CREATE TABLE BREADS (
    breads_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL)
    ''')
mycursor.execute('''INSERT INTO BREADS VALUES	 
    (1,'Tandoori Roti',30),
    (2,'Roomali Roti',17),
    (3,'Butter Roti',36),
    (4,'Plain Naan',43),
    (5,'Butter Naan',58)''')


mycursor.execute("DROP TABLE IF EXISTS RICE")
mycursor.execute('''
CREATE TABLE RICE (
    rice_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL)
    ''')
mycursor.execute('''INSERT INTO RICE VALUES	 
    (1,'Veg. Fried Rice',165),
    (2,'Chilly Garlic Rice',165)''')

mycursor.execute("DROP TABLE IF EXISTS DESSERT")
mycursor.execute('''
CREATE TABLE DESSERT (
    dessert_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL)
    ''')
mycursor.execute('''INSERT INTO DESSERT VALUES	 
    (1,'Vanilla/Strawberry',51),
    (2,'Tutti Fruti',60),
    (3,'Pineapple',60),
    (4,'Chocolate',60),
    (5,'Butter Scotch',60),
    (6,'Kaju Kishmish',60),
    (7,'Vanilla Chocochips',60),
    (8,'Mango',60),
    (9,'Anjeer Honey',60),
    (10,'Chocolate Almond Fudge',60),
    (11,'Kesar Pista',60),
    (12,'Black Currant',60)''')


mycursor.execute("DROP TABLE IF EXISTS Table_Reserve")
mycursor.execute('''
    CREATE TABLE Table_Reserve( 
        customer_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
        customer_name VARCHAR(255),
        persons INTEGER NOT NULL);
    ''')

mycursor.execute("DROP TABLE IF EXISTS ORDERS")
odrq = '''
    CREATE TABLE ORDERS (
        order_id INTEGER,
        starter_id INTEGER NULL,
        main_course_id INTEGER NULL,
        breads_id INTEGER NULL,
        rice_id INTEGER NULL,
        dessert_id INTEGER NULL)
    '''
mycursor.execute(odrq)


mycursor.execute('INSERT INTO ORDERS (order_id) VALUES (0)')

mydb.commit()