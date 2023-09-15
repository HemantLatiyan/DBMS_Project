import streamlit as st


def query5():
    st.write("Update the discount to 20"+"%"+" on all products with discount = 5%")
    return "Update Product set offer = offer + 15 where offer = 5;"    

def query16():
    st.write("List all products in a closest warehouse to a customer c1")
    return "Select pid from storedIn where wid in (select W.wid from customers C, Warehouse W where C.cid = 100 and W.pincode-C.pincode = (select min(W1.pincode-C’.pincode) from customers C’ , warehouse W1 where C’.cid = 100));"

def query15():
    st.write("List all employees from city London with designation Manager in increasing order of salary")
    city = st.text_input("Enter city", value="London")
    desi = st.text_input("Enter designation", value="MANAGER")
    return "Select * from Employee where city = '{}' and designation = '{}' order by salary;".format(city, desi)
