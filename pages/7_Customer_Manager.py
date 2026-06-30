import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Manager", page_icon="👥")

st.title("👥 Customer Manager")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
frame = st.text_input("Frame Purchased")
amount = st.number_input("Amount (₹)", min_value=0)

if st.button("Save Customer"):
    st.success(f"{name} added successfully!")

st.divider()

data = pd.DataFrame({
    "Customer": ["Rahul", "Aman"],
    "Phone": ["9876543210", "9123456789"],
    "Frame": ["Titan", "Ray-Ban"],
    "Amount": [2500, 4200]
})

st.dataframe(data, use_container_width=True)
