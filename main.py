from tkinter import *
from tkinter import messagebox
import random, string
from functools import partial
import mysql.connector



mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root123',
    auth_plugin = 'mysql_native_password')
print(mydb)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("USE RESTAURANT_MANAGEMENT")

root =Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("DBMS Mini Project")

heading = Label(root, text = 'Restraunt Management' , font ='arial 15 bold').pack(pady = 25)
#strs = StringVar


def Reservation():
    root1 = Toplevel(root)
    root1.geometry("300x300")
    root1.resizable(0,0)
    root1.title("Reservation")
    
    #messagebox.showinfo("Acknowledgement" ,"helllo")
    nm = Label(root1, text ='Name', font ='arial 15 bold').pack(side = TOP)
    name = StringVar()
    nme = Entry(root1 ,textvariable = name, bd = 5).pack()

    ppl_label = Label(root1, text = 'No. of people', font = 'arial 10 bold').pack()
    ppl = IntVar()
    ppl_no = Spinbox(root1, from_ = 1, to_ = 30 , textvariable = ppl , width = 15).pack()

    
    def reserve(namee,pep):
        #cusid = random.choice(string.digits)
        mycursor.execute("SELECT customer_id FROM Table_Reserve")
        a = int()
        for i in mycursor:
            a = i[0]
            #for j in i:
             #   a = int(j)
        if a == 0:
            cusid = 1
        else:
            cusid = a + 1
        nm1 = (namee.get())
        ppl1 = (pep.get())
        #print("\t num1 = ",nm1)
        #print("\t ppl1 = ",ppl1)
    #name = str(input('Enter name :'))
    #ppl = int(input('Enter no. of persons : '))
        INS = "INSERT INTO Table_Reserve values (%s,%s,%s)"
        RES = (cusid,nm1,ppl1)
        mycursor.execute(INS,RES)
        mydb.commit()
    
        mycursor.execute("SELECT * FROM Table_Reserve")
        flag = False
        for i,j,k in mycursor:
            nmm = str(j)
            ppll = int(k)
            if int(cusid) == int(i) and nm1 == j:
                flag = True
                break
        if flag == True:
            root1.destroy()
            messagebox.showinfo('Acknowledgement', 'Reservation Successful!\n Name : %s \nNo. of persons :%d' %(nmm,ppll))
        
    reserve = partial(reserve, name, ppl) 
    Button(root1, text = 'RESERVE', command = reserve).pack(pady=5)

    root1.mainloop()

def Order():
    root2 = Toplevel(root)
    root2.geometry("500x500")
    root2.resizable(0,0)
    root2.title("Order Food")

    mycursor.execute("SELECT order_id FROM ORDERS")
    for x in mycursor :
        b = int()
        b = x[0]
        # for y in x:
        #     b = int(y)
        if b == 0:
            ord_no = 1
        else:
            ord_no = b + 1
    
    #print(ord_no)

    od = ord_no

    def start():
        strtrs = Toplevel(root2)
        strtrs.geometry("400x400")
        strtrs.resizable(0,0)
        strtrs.title("Starters")
        s = []
        for i in range(7):
            i = IntVar()
            s.append(i)

    
        starter_list = []

        mycursor.execute("SELECT * FROM starters")
        for j in mycursor:
            starter_list.append(j)

        c0 = Checkbutton(strtrs, text = (starter_list[0])[1] + '\t' + str((starter_list[0])[2]) + '/-', variable = s[0]).pack()
        c1 = Checkbutton(strtrs, text = (starter_list[1])[1] + '\t' + str((starter_list[1])[2]) + '/-', variable = s[1]).pack()
        c2 = Checkbutton(strtrs, text = (starter_list[2])[1] + '\t' + str((starter_list[2])[2]) + '/-', variable = s[2]).pack()
        c3 = Checkbutton(strtrs, text = (starter_list[3])[1] + '\t' + str((starter_list[3])[2]) + '/-', variable = s[3]).pack()
        c4 = Checkbutton(strtrs, text = (starter_list[4])[1] + '\t' + str((starter_list[4])[2]) + '/-', variable = s[4]).pack()
        c5 = Checkbutton(strtrs, text = (starter_list[5])[1] + '\t' + str((starter_list[5])[2]) + '/-', variable = s[5]).pack()
        c6 = Checkbutton(strtrs, text = (starter_list[6])[1] + '\t' + str((starter_list[6])[2]) + '/-', variable = s[6]).pack()

        def confirm():
            a = []
            for i,j in enumerate(s):
                if (j.get()) == 1:
                    a.append(i)
            #print('\ta = ',a)
            
            #print('\n\tOrder no. at starters - ',ord_no)

            for i in a:
                mycursor.execute("INSERT INTO ORDERS (order_id, starter_id) VALUES (%s,%s)" ,(ord_no,i+1))
                mydb.commit()
            
            strtrs.destroy()

            messagebox.showinfo('Acknowledgement', 'Order Confirmed!')

        Button(strtrs, text = "Confirm", command = confirm).pack()
        Button(strtrs, text = "Cancel", command = strtrs.quit).pack()


    def mainc():
        maic = Toplevel(root2)
        maic.geometry("400x400")
        maic.resizable(0,0)
        maic.title("Main Course")
        s = []
        for i in range(6):
            i = IntVar()
            s.append(i)

    
        maic_list = []

        mycursor.execute("SELECT * FROM main_course")
        for j in mycursor:
            maic_list.append(j)

        c0 = Checkbutton(maic, text = (maic_list[0])[1] + '\t' + str((maic_list[0])[2]) + '/-', variable = s[0]).pack()
        c1 = Checkbutton(maic, text = (maic_list[1])[1] + '\t' + str((maic_list[1])[2]) + '/-', variable = s[1]).pack()
        c2 = Checkbutton(maic, text = (maic_list[2])[1] + '\t' + str((maic_list[2])[2]) + '/-', variable = s[2]).pack()
        c3 = Checkbutton(maic, text = (maic_list[3])[1] + '\t' + str((maic_list[3])[2]) + '/-', variable = s[3]).pack()
        c4 = Checkbutton(maic, text = (maic_list[4])[1] + '\t' + str((maic_list[4])[2]) + '/-', variable = s[4]).pack()
        c5 = Checkbutton(maic, text = (maic_list[5])[1] + '\t' + str((maic_list[5])[2]) + '/-', variable = s[5]).pack()
        #c6 = Checkbutton(strtrs, text = (starter_list[6])[1] + '\t' + str((starter_list[6])[2]) + '/-', variable = s[6]).pack()

        def confirm():
            a = []
            for i,j in enumerate(s):
                if (j.get()) == 1:
                    a.append(i)
            #print('\ta = ',a)

            #print('\n\tOrder no. at main course - ',ord_no)

            for i in a:
                mycursor.execute("INSERT INTO ORDERS (order_id, main_course_id) VALUES (%s,%s)" ,(ord_no,i+1))
                mydb.commit()

            maic.destroy()

            messagebox.showinfo('Acknowledgement', 'Order Confirmed!')

        Button(maic, text = "Confirm", command = confirm).pack()
        Button(maic, text = "Cancel", command = maic.quit).pack()
    


    def bread():
        brd = Toplevel(root2)
        brd.geometry("400x400")
        brd.resizable(0,0)
        brd.title("Breads")
        s = []
        for i in range(5):
            i = IntVar()
            s.append(i)

    
        bread_list = []

        mycursor.execute("SELECT * FROM breads")
        for j in mycursor:
            bread_list.append(j)

        c0 = Checkbutton(brd, text = (bread_list[0])[1] + '\t' + str((bread_list[0])[2]) + '/-', variable = s[0]).pack()
        c1 = Checkbutton(brd, text = (bread_list[1])[1] + '\t' + str((bread_list[1])[2]) + '/-', variable = s[1]).pack()
        c2 = Checkbutton(brd, text = (bread_list[2])[1] + '\t' + str((bread_list[2])[2]) + '/-', variable = s[2]).pack()
        c3 = Checkbutton(brd, text = (bread_list[3])[1] + '\t' + str((bread_list[3])[2]) + '/-', variable = s[3]).pack()
        c4 = Checkbutton(brd, text = (bread_list[4])[1] + '\t' + str((bread_list[4])[2]) + '/-', variable = s[4]).pack()
        #c5 = Checkbutton(maic, text = (maic_list[5])[1] + '\t' + str((maic_list[5])[2]) + '/-', variable = s[5]).pack()
        #c6 = Checkbutton(strtrs, text = (starter_list[6])[1] + '\t' + str((starter_list[6])[2]) + '/-', variable = s[6]).pack()

        def confirm():
            a = []
            for i,j in enumerate(s):
                if (j.get()) == 1:
                    a.append(i)
            #print('\ta = ',a)

            #print('\n\tOrder no. at breads - ',ord_no)

            for i in a:
                mycursor.execute("INSERT INTO ORDERS (order_id, breads_id) VALUES (%s,%s)" ,(ord_no,i+1))
                mydb.commit()
            
            brd.destroy()

            messagebox.showinfo('Acknowledgement', 'Order Confirmed!')

        Button(brd, text = "Confirm", command = confirm).pack()
        Button(brd, text = "Cancel", command = brd.quit).pack()
    
    def ricee():
        rb = Toplevel(root2)
        rb.geometry("400x400")
        rb.resizable(0,0)
        rb.title("Rice & Biryanis")
        s = []
        for i in range(2):
            i = IntVar()
            s.append(i)

    
        rice_list = []

        mycursor.execute("SELECT * FROM rice")
        for j in mycursor:
            rice_list.append(j)

        c0 = Checkbutton(rb, text = (rice_list[0])[1] + '\t' + str((rice_list[0])[2]) + '/-', variable = s[0]).pack()
        c1 = Checkbutton(rb, text = (rice_list[1])[1] + '\t' + str((rice_list[1])[2]) + '/-', variable = s[1]).pack()
        #c2 = Checkbutton(brd, text = (bread_list[2])[1] + '\t' + str((bread_list[2])[2]) + '/-', variable = s[2]).pack()
        #c3 = Checkbutton(brd, text = (bread_list[3])[1] + '\t' + str((bread_list[3])[2]) + '/-', variable = s[3]).pack()
        #c4 = Checkbutton(brd, text = (bread_list[4])[1] + '\t' + str((bread_list[4])[2]) + '/-', variable = s[4]).pack()
        #c5 = Checkbutton(maic, text = (maic_list[5])[1] + '\t' + str((maic_list[5])[2]) + '/-', variable = s[5]).pack()
        #c6 = Checkbutton(strtrs, text = (starter_list[6])[1] + '\t' + str((starter_list[6])[2]) + '/-', variable = s[6]).pack()

        def confirm():
            a = []
            for i,j in enumerate(s):
                if (j.get()) == 1:
                    a.append(i)
            #print('\ta = ',a)

            #print('\n\tOrder no. at rice - ',ord_no)

            for i in a:
                mycursor.execute("INSERT INTO ORDERS (order_id, rice_id) VALUES (%s,%s)" ,(ord_no,i+1))
                mydb.commit()
            
            rb.destroy()

            messagebox.showinfo('Acknowledgement', 'Order Confirmed!')

        Button(rb, text = "Confirm", command = confirm).pack()
        Button(rb, text = "Cancel", command = rb.quit).pack()


    def dessert():
        ds = Toplevel(root2)
        ds.geometry("400x400")
        ds.resizable(0,0)
        ds.title("Rice & Biryanis")
        s = []
        for i in range(12):
            i = IntVar()
            s.append(i)

    
        dessert_list = []

        mycursor.execute("SELECT * FROM dessert")
        for j in mycursor:
            dessert_list.append(j)

        c0 = Checkbutton(ds, text = (dessert_list[0])[1] + '\t' + str((dessert_list[0])[2]) + '/-', variable = s[0]).pack()
        c1 = Checkbutton(ds, text = (dessert_list[1])[1] + '\t' + str((dessert_list[1])[2]) + '/-', variable = s[1]).pack()
        c2 = Checkbutton(ds, text = (dessert_list[2])[1] + '\t' + str((dessert_list[2])[2]) + '/-', variable = s[2]).pack()
        c3 = Checkbutton(ds, text = (dessert_list[3])[1] + '\t' + str((dessert_list[3])[2]) + '/-', variable = s[3]).pack()
        c4 = Checkbutton(ds, text = (dessert_list[4])[1] + '\t' + str((dessert_list[4])[2]) + '/-', variable = s[4]).pack()
        c5 = Checkbutton(ds, text = (dessert_list[5])[1] + '\t' + str((dessert_list[5])[2]) + '/-', variable = s[5]).pack()
        c6 = Checkbutton(ds, text = (dessert_list[6])[1] + '\t' + str((dessert_list[6])[2]) + '/-', variable = s[6]).pack()
        c7 = Checkbutton(ds, text = (dessert_list[7])[1] + '\t' + str((dessert_list[7])[2]) + '/-', variable = s[7]).pack()
        c8 = Checkbutton(ds, text = (dessert_list[8])[1] + '\t' + str((dessert_list[8])[2]) + '/-', variable = s[8]).pack()
        c9 = Checkbutton(ds, text = (dessert_list[9])[1] + '\t' + str((dessert_list[9])[2]) + '/-', variable = s[9]).pack()
        c10 = Checkbutton(ds, text = (dessert_list[10])[1] + '\t' + str((dessert_list[10])[2]) + '/-', variable = s[10]).pack()
        c11 = Checkbutton(ds, text = (dessert_list[11])[1] + '\t' + str((dessert_list[11])[2]) + '/-', variable = s[11]).pack()

        def confirm():
            a = []
            for i,j in enumerate(s):
                if (j.get()) == 1:
                    a.append(i)
            #print('\ta = ',a)

            #print('\n\tOrder no. at desserts - ',ord_no)

            for i in a:
                mycursor.execute("INSERT INTO ORDERS (order_id, dessert_id) VALUES (%s,%s)" ,(ord_no,i+1))
                mydb.commit()

            ds.destroy()
            
            messagebox.showinfo('Acknowledgement', 'Order Confirmed!')

        Button(ds, text = "Confirm", command = confirm).pack()
        Button(ds, text = "Cancel", command = ds.quit).pack()

    def shw():
        #for starters
        starter_query = '''
        SELECT orders.order_id, starters.name, starters.price from orders join starters where
        orders.starter_id = starters.starter_id AND orders.order_id = %d
        ''' %(od)

        ordd = str()

        ordd = ' Order no - ' + str(od)
    
        mycursor.execute(starter_query)
        for x,y,z in mycursor:
            ordd = ordd + '\n ' + y + '\t ' + str(z) + '\-'

        #for main_course
        main_course_query = '''
        SELECT orders.order_id, main_course.name, main_course.price from orders join main_course where
        orders.main_course_id = main_course.main_course_id AND orders.order_id = %d
        ''' %(od)
    
        mycursor.execute(main_course_query)
        for x,y,z in mycursor:
            ordd = ordd + '\n ' + y + '\t ' + str(z) + '\-'
        
        #for breads
        breads_query = '''
        SELECT orders.order_id, breads.name, breads.price from orders join breads where
        orders.breads_id = breads.breads_id AND orders.order_id = %d
        ''' %(od)
    
        mycursor.execute(breads_query)
        for x,y,z in mycursor:
            ordd = ordd + '\n ' + y + '\t ' + str(z) + '\-'

        #for rice
        rice_query = '''
        SELECT orders.order_id, rice.name, rice.price from orders join rice where
        orders.rice_id = rice.rice_id AND orders.order_id = %d
        ''' %(od)
    
        mycursor.execute(rice_query)
        for x,y,z in mycursor:
            ordd = ordd + '\n ' + y + '\t ' + str(z) + '\-'

        #for dessert
        dessert_query = '''
        SELECT orders.order_id, dessert.name, dessert.price from orders join dessert where
        orders.dessert_id = dessert.dessert_id AND orders.order_id = %d
        ''' %(od)
    
        mycursor.execute(dessert_query)
        for x,y,z in mycursor:
            ordd = ordd + '\n ' + y + '\t ' + str(z) + '\-'

        root2.destroy()

        messagebox.showinfo("Your Order" , '%s ' %(ordd))
    
    def cn():
        mycursor.execute('''
        DELETE FROM ORDERS WHERE order_id = %d
        ''' %(od))
        root2.destroy()


    Button(root2, text = "Starter", command = start).pack(pady = 5)
    Button(root2, text= "Main Course", command = mainc).pack(pady = 5)
    Button(root2, text = "Breads", command = bread).pack(pady = 5)
    Button(root2, text = "Rice" , command = ricee).pack(pady = 5)
    Button(root2, text = "Dessert" , command = dessert).pack(pady = 5)
    Button(root2, text = "Show Order", command = shw).pack(pady = 20 )
    Button(root2, text = "Cancel", command = cn).pack()

Button(root, text = "Reserve Table" , width = 14 , height = 2, command = Reservation ).pack(pady= 20)
Button(root, text = "Order Food" , width = 14 , height = 2, command = Order ).pack(pady= 20)

root.mainloop()