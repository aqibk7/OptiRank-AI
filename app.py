import streamlit as st

st.set_page_config(page_title="OptiRank AI", page_icon="👓", layout="wide")

st.title("👓 OptiRank AI")
st.subheader("Welcome to Naina Opticals")

st.success("Your Optical Business Growth Assistant")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("SEO Score", "82%", "+3%")

with col2:
    st.metric("Google Rating", "4.8 ⭐")

with col3:
    st.metric("Reviews", "127")

st.divider()

st.header("Today's Tasks")

st.checkbox("Reply to Google Reviews")
st.checkbox("Upload 3 Photos")
st.checkbox("Publish Google Post")
st.checkbox("Add New Product")

if st.button("Generate Review Reply"):
    st.success("Thank you for choosing Naina Opticals. We appreciate your feedback!")
