import streamlit as st

def query12():
    st.write("Update premium subscription of a customer with id a1")
    pid = st.number_input("Enter aid", value=12);
    return "Update Account set premiumsubscription = 1 where aid = '{}' and premiumsubscription = 0;".format(pid)

def query13():
    st.write("Update stock of a product p1")
    cat = st.number_input("Enter pid for updation", value=212)
    return "Update Product set stock = stock + 1 where pid = {}".format(cat)

def query14():
    st.write("Update rating of a product")
    cat = st.number_input("Enter pid for updation in rating", value=212);
    return "Update Product set rating = rating + 1 where pid = {} and rating < 5;".format(cat)
