
import streamlit as st


def query9():
    st.write("List Products from highest to lowest price in a category c1")
    category = st.text_input("Enter category", value="CLOTHING");
    return "Select * from Product where category = '{}' order by price DESC".format(category)
