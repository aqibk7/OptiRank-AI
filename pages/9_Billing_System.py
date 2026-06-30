import streamlit as st

st.set_page_config(page_title="Billing System", page_icon="🧾")

st.title("🧾 Optical Billing System")

customer = st.text_input("Customer Name")

frame = st.text_input("Frame Name")
lens = st.text_input("Lens Type")

frame_price = st.number_input("Frame Price", min_value=0)
lens_price = st.number_input("Lens Price", min_value=0)

total = frame_price + lens_price

st.subheader(f"Total Amount: ₹{total}")

if st.button("Generate Bill"):
    st.success("Bill Generated Successfully!")
    st.write("Customer:", customer)
    st.write("Frame:", frame)
    st.write("Lens:", lens)
    st.write("Total:", f"₹{total}")
