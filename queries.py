import streamlit as st

def query7():
    st.write("List all the customers who has Premium subscription")
    return "Select name from Customers where cid in (select cid from account where premiumsubscription=1)"

def query8():
    st.write("Products from highest to lowest rating in a category c1")
    cat = st.text_input("Enter Category", value="BOOKS")
    return "Select * from product where category='{}' order by rating DESC".format(cat)

def query17():
    st.write("Which mode of payment was used most")
    return "Select Mode_of_Payment,count(Mode_of_Payment) from orders group by Mode_of_Payment having count(Mode_of_Payment) in (select max(mycount) from (Select Mode_of_Payment, count(Mode_of_Payment) mycount from orders group by Mode_of_Payment) as T1);"
