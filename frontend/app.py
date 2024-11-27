import streamlit as st
import requests
import os
import sys

# Dynamically add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import display_html


BASE_URL = "http://127.0.0.1:5000"

# Password Strength Color Mapping
STRENGTH_COLORS = {
    "Very Weak": ("#FF0000", 20),
    "Weak": ("#FFA500", 40),
    "Moderate": ("#FFFF00", 60),
    "Strong": ("#00FF00", 80),
    "Very Strong": ("#00FF00", 100)
}

st.set_page_config(
    page_title="GenLock",
    page_icon="https://lesolson.com/wp-content/uploads/2019/08/Asset-1strong-password.png",
    layout="wide"
    )


display_html("frontend/app.html")

st.title("GenLock")
st.write("Password Management System")

new = st.container(height=40, border=False)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Generate Password", "Check Password Security", "Stored Passwords"])

# Generate Password
with tab1:
    st.header("Generate Password")
    box_col1, box_col2 = st.columns([1, 5])
    with box_col1:
        length = st.number_input("Password Length", 8, 32, 12)
    include_special = st.checkbox("Include Special Characters", True)
    if st.button("Generate Password"):
        response = requests.post(f"{BASE_URL}/generate-password", json={
            "length": length,
            "include_special": include_special
        })
        st.json(response.json())

        # Display Strength Progress Bar using custom HTML
        generated_password = response.json().get("password", "")
        security_level = response.json().get("security_level", "Unknown")
        color, progress = STRENGTH_COLORS.get(security_level, ("#000000", 0))

        # Creating a custom progress bar
        progress_html = f"""
        <div style="width: 100%; background-color: #e0e0e0; border-radius: 5px; height: 30px;">
            <div style="width: {progress}%; background-color: {color}; height: 100%; border-radius: 5px; text-align: center; color: white; line-height: 30px;">
                <b>{security_level}</b>
            </div>
        </div>
        """
        st.markdown(progress_html, unsafe_allow_html=True)

# Check Password Security
with tab2:
    st.header("Check Password Security")
    password_to_check = st.text_input("Enter Password to Check")
    if st.button("Check Security"):
        response = requests.post(f"{BASE_URL}/check-security", json={"password": password_to_check})
        st.json(response.json())

# List Stored Passwords
with tab3:
    st.header("Stored Passwords")
    if st.button("View Passwords"):
        response = requests.get(f"{BASE_URL}/passwords")
        st.json(response.json())
