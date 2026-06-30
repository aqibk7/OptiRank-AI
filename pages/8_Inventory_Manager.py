import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Manager", page_icon="📦")

st.title("📦 Inventory Manager")

brand = st.selectbox(
    "Brand",
    ["Titan", "Ray-Ban", "Vincent Chase", "Fastrack", "Crizal", "Other"]
)

model = st.text_input("Frame Model")
price = st.number_input("Selling Price (₹)", min_value=0)
stock = st.number_input("Stock Quantity", min_value=0)

if st.button("Add Frame"):
    st.success(f"{brand} - {model} added successfully!")

st.divider()

inventory = pd.DataFrame({
    "Brand": ["Titan", "Ray-Ban", "Fastrack"],
    "Model": ["T101", "RB3025", "FT210"],
    "Price": [2500, 5500, 1800],
    "Stock": [12, 5, 18]
})

st.dataframe(inventory, use_container_width=True)

low_stock = inventory[inventory["Stock"] < 10]

st.subheader("⚠️ Low Stock")

if len(low_stock) > 0:
    st.dataframe(low_stock, use_container_width=True)
else:
    st.success("No low stock items.")
