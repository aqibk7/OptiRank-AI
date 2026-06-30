import streamlit as st

st.set_page_config(page_title="AI Review Reply", page_icon="⭐")

st.title("⭐ AI Review Reply Generator")

review = st.text_area("Paste a customer review")

tone = st.selectbox(
    "Reply Style",
    ["Professional", "Friendly", "Premium"]
)

if st.button("Generate Reply"):
    if review:
        st.success("Suggested Reply")
        st.write(
            f"Thank you for your valuable feedback! We truly appreciate your review. "
            f"We're delighted to know you had a great experience at Naina Opticals. "
            f"We look forward to serving you again soon."
        )
    else:
        st.warning("Please paste a review first.")
