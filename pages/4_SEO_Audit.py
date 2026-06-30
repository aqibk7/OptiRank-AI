import streamlit as st

st.set_page_config(page_title="SEO Audit", page_icon="📈")

st.title("📈 SEO Audit")

score = st.slider("Current SEO Score", 0, 100, 82)

st.metric("SEO Score", f"{score}%")

st.subheader("SEO Checklist")

st.checkbox("Business description added")
st.checkbox("Website linked")
st.checkbox("Phone number verified")
st.checkbox("Products uploaded")
st.checkbox("Services updated")
st.checkbox("Weekly Google Posts")
st.checkbox("50+ Photos Uploaded")

if score >= 90:
    st.success("Excellent SEO! Keep it up.")
elif score >= 70:
    st.warning("Good SEO. Improve photos and posts.")
else:
    st.error("SEO needs improvement.")
