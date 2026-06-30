import streamlit as st
from database import add_customer, get_customers

st.title("📂 Customer Database")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
prescription = st.text_area("Prescription")

if st.button("Save Customer"):
    add_customer(name, phone, address, prescription)
    st.success("Customer Saved!")

st.divider()

st.subheader("Saved Customers")

for customer in get_customers():
    st.write(customer)
