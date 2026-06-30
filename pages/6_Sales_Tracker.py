import streamlit as st
from datetime import date

st.set_page_config(page_title="Sales Tracker", page_icon="💰")

st.title("💰 Daily Sales Tracker")

today = date.today()

st.write(f"Date: {today}")

sales = st.number_input("Today's Sales (₹)", min_value=0)
customers = st.number_input("Customers Served", min_value=0)
eye_tests = st.number_input("Eye Tests Done", min_value=0)

if st.button("Save Today's Record"):
    st.success("Today's data saved successfully!")

st.divider()

st.metric("Today's Sales", f"₹{sales:,.0f}")
st.metric("Customers", customers)
st.metric("Eye Tests", eye_tests)
