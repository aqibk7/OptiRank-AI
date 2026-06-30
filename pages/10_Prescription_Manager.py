import streamlit as st

st.set_page_config(page_title="Prescription Manager", page_icon="👁️")

st.title("👁️ Prescription Manager")

customer = st.text_input("Customer Name")

st.subheader("Right Eye (OD)")
od_sph = st.text_input("SPH (OD)")
od_cyl = st.text_input("CYL (OD)")
od_axis = st.text_input("AXIS (OD)")

st.subheader("Left Eye (OS)")
os_sph = st.text_input("SPH (OS)")
os_cyl = st.text_input("CYL (OS)")
os_axis = st.text_input("AXIS (OS)")

pd = st.text_input("Pupillary Distance (PD)")
doctor = st.text_input("Doctor / Optometrist")

if st.button("Save Prescription"):
    st.success("Prescription Saved Successfully!")

    st.write("### Prescription")
    st.write("Customer:", customer)
    st.write(f"OD: SPH {od_sph}, CYL {od_cyl}, AXIS {od_axis}")
    st.write(f"OS: SPH {os_sph}, CYL {os_cyl}, AXIS {os_axis}")
    st.write("PD:", pd)
    st.write("Doctor:", doctor)
