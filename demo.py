from time import sleep
import AAQueries
import streamlit as st 
import mysql.connector
import queries
import queriesPY
import queries_Hemant
import queries_sahil

mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database = "proj"
)

def results():
    try:
        print("Called")
        myresult = mycursor.fetchall()
        for i in myresult:
            st.write(i)
    except Exception as e:
        print(e)

mycursor = mydb.cursor()

def Query12():
    print("Executing query12")
    mycursor.execute(queriesPY.query12())
    print("Data after updation")
    mycursor.execute("select * from Account")
    results()

def Query13():
    print("Executing query13")
    mycursor.execute(queriesPY.query13())
    results()
    print("Data after updatetion")
    mycursor.execute("select * from Product")
    results()
    
def Query14():
    print("Executing query14")
    mycursor.execute(queriesPY.query14())
    print("Data after updation")
    mycursor.execute("select * from Product")
    results()

def query7():
    print("Executing query7")
    mycursor.execute(queries.query7())
    results()

def query8():
    print("Executing query8")
    mycursor.execute(queries.query8())
    results()

def query17():
    print("Executing query17")
    mycursor.execute(queries.query17())
    results()

def query9():
    print("Executing query9")
    mycursor.execute(queries_sahil.query9())
    results()

def query5():
    print("Executing query5")
    mycursor.execute(queries_Hemant.query5())
    print("Data after updation")
    mycursor.execute("Select * from product;")
    results()

def query15():
    print("Executing query15")
    mycursor.execute(queries_Hemant.query15())
    results()

def query16():
    print("Executing query16")
    mycursor.execute(queries_Hemant.query16())
    results()

def queryA1():
    st.header("Advanced Aggregate functions")
    print("executing aa queries 1")
    mycursor.execute(AAQueries.queryA1())
    results()

def queryA2():
    print("executing aa queries 2")
    mycursor.execute(AAQueries.queryA2())
    results()

def queryA3():
    print("executing aa queries 3")
    mycursor.execute(AAQueries.queryA3())
    results()

def queryA4():
    print("executing aa queries 4")
    mycursor.execute(AAQueries.queryA4())
    results()

def main():
    st.title("DBMS Project")
    query5()
    sleep(1)
    query15()
    sleep(1)
    query16()
    sleep(1)
    query7()
    sleep(1)
    query8()
    sleep(1)
    query17()
    sleep(1)
    query9()
    sleep(1)
    Query12()
    sleep(1)
    Query13()
    sleep(1)
    Query14()
    sleep(1)
    queryA1()
    sleep(1)
    queryA2()
    sleep(1)
    queryA3()
    sleep(1)
    queryA4()


main()
print("Closing the cursor")
mycursor.close()
