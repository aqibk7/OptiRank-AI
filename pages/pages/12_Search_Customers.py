import streamlit as st
from database import get_customers

st.set_page_config(page_title="Search Customers", page_icon="🔍")

st.title("🔍 Search Customers")

search = st.text_input("Search by Name or Phone")

customers = get_customers()

if search:
    found = False
    for customer in customers:
        # customer = (id, name, phone, address, prescription)
        if search.lower() in customer[1].lower() or search in customer[2]:
            st.success("Customer Found")
            st.write(f"👤 Name: {customer[1]}")
            st.write(f"📞 Phone: {customer[2]}")
            st.write(f"🏠 Address: {customer[3]}")
            st.write(f"👓 Prescription: {customer[4]}")
            found = True

    if not found:
        st.error("No customer found.")
else:
    st.info("Enter a customer name or phone number.")
