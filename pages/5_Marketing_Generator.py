import streamlit as st

st.set_page_config(page_title="Marketing Generator", page_icon="📢")

st.title("📢 AI Marketing Generator")

offer = st.text_input("Today's Offer", "20% OFF on Frames")

festival = st.selectbox(
    "Occasion",
    ["Normal Day", "Eid", "Diwali", "Durga Puja", "Christmas", "New Year"]
)

if st.button("Generate Marketing Post"):
    post = f"""
🎉 {festival} Special at Naina Opticals!

👓 {offer}

✅ Premium Frames
✅ Branded Sunglasses
✅ Computer Glasses
✅ Eye Testing Available

📍 HB Road, Lalpur Chowk, Ranchi
📞 9334264732 | 9852656983

Visit today!
"""

    st.success("
