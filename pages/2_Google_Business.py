import streamlit as st

st.set_page_config(page_title="Google Business", page_icon="📍")

st.title("📍 Google Business Profile")

st.metric("Google Rating", "4.9 ⭐")
st.metric("Reviews", "170")

st.subheader("Business Information")

st.write("**Naina Opticals**")
st.write("👤 Owner: Md Jawed")
st.write("📍 H.B. Road, Infront of Mall Decor, Lalpur Chowk, Ranchi")
st.write("📞 9334264732")
st.write("📞 9852656983")

st.success("Business profile is active and performing well.")
