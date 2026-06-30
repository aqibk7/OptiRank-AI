import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Billing System", page_icon="🧾")

st.title("🧾 Naina Opticals Billing System")

# Connect to database
conn = sqlite3.connect("optirank.db", check_same_thread=False)
cursor = conn.cursor()

# Generate Invoice Number
year = datetime.now().year
cursor.execute("SELECT COUNT(*) FROM bills")
count = cursor.fetchone()[0] + 1
invoice_no = f"NO-{year}-{count:04d}"

st.info(f"Invoice No: {invoice_no}")

customer = st.text_input("Customer Name")
phone = st.text_input("Phone Number")

frame_brand = st.text_input("Frame Brand")
frame_model = st.text_input("Frame Model")

lens_brand = st.text_input("Lens Brand")
lens_type = st.text_input("Lens Type")

frame_price = st.number_input("Frame Price (₹)", min_value=0)
lens_price = st.number_input("Lens Price (₹)", min_value=0)
discount = st.number_input("Discount (₹)", min_value=0)

payment_mode = st.selectbox(
    "Payment Mode",
    ["Cash", "UPI", "Card", "Bank Transfer"]
)

total = frame_price + lens_price - discount

st.subheader(f"💰 Total Amount : ₹{total}")

if st.button("💾 Save Bill"):

    cursor.execute("""
        INSERT INTO bills (
            invoice_no,
            customer_name,
            phone,
            frame_brand,
            frame_model,
            lens_brand,
            lens_type,
            frame_price,
            lens_price,
            discount,
            total,
            payment_mode,
            bill_date
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        invoice_no,
        customer,
        phone,
        frame_brand,
        frame_model,
        lens_brand,
        lens_type,
        frame_price,
        lens_price,
        discount,
        total,
        payment_mode,
        datetime.now().strftime("%d-%m-%Y")
    ))

    conn.commit()

    st.success("✅ Bill Saved Successfully!")

    st.write("### Invoice Summary")
    st.write("🧾 Invoice:", invoice_no)
    st.write("👤 Customer:", customer)
    st.write("📞 Phone:", phone)
    st.write("👓 Frame:", frame_brand, "-", frame_model)
    st.write("🔍 Lens:", lens_brand, "-", lens_type)
    st.write("💳 Payment:", payment_mode)
    st.write(f"💰 Total: ₹{total}")
