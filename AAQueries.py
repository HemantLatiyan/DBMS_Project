import streamlit as st

def queryA1():
    st.write("Calculate the sparsity of offers in products")
    return "Select stddev(product.offer) from product;"

def queryA2():
    st.write("Rank product based on rating")
    return "Select pid, rank() over (order by rating)ratingRank from product;"

def queryA3():
    st.write("Variance of prices of all products.")
    return "Select VARIANCE(price) from product;"

def queryA4():
    st.write("Percent rank of employee in a warehouse");
    return "SELECT eid, percent_rank() OVER ( order by salary desc )AS 'percent_rank' FROM employee;"

