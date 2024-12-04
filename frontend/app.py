import os
import sys

import pandas as pd
import requests
import streamlit as st

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
    "Very Strong": ("#00FF00", 100),
}

st.set_page_config(
    page_title="GenLock",
    page_icon="https://lesolson.com/wp-content/uploads/2019/08/Asset-1strong-password.png",
    layout="wide",
)


display_html("frontend/app.html")

st.title("GenLock")
st.write("Password Management System")

new = st.container(height=40, border=False)

# Create tabs
tab1, tab2, tab3 = st.tabs(
    ["Generate Password", "Check Password Security", "Stored Passwords"]
)

# Generate Password
with tab1:
    st.header("Generate Password")
    box_col1, _, box_col2 = st.columns([2, 1, 3])
    with box_col1:
        length = st.number_input("Password Length", 8, 32, 12)
    include_special = st.checkbox("Include Special Characters", True)
    if st.button("Generate Password"):
        response = requests.post(
            f"{BASE_URL}/generate-password",
            json={"length": length, "include_special": include_special},
        )
        with box_col2:
            if response.status_code == 200:
                # Parse and display the JSON response
                try:
                    json_data = response.json()
                    st.json(json_data)

                    # Display Strength Progress Bar using custom HTML
                    generated_password = response.json().get("password", "")
                    security_level = response.json().get("security_level", "Unknown")
                    color, progress = STRENGTH_COLORS.get(
                        security_level, ("#000000", 0)
                    )

                    # Creating a custom progress bar
                    progress_html = f"""
                    <div style="width: 100%; background-color: #e0e0e0; border-radius: 5px; height: 30px;">
                        <div style="width: {progress}%; background-color: {color}; height: 100%; border-radius: 5px; text-align: center; color: white; line-height: 30px;">
                            <b>{security_level}</b>
                        </div>
                    </div>
                    """
                    st.markdown(progress_html, unsafe_allow_html=True)
                except ValueError:
                    st.error("Failed to decode JSON response.")
            else:
                # Handle errors, including 429
                if response.status_code == 429:
                    st.error(f"Rate limit exceeded: {response.json().get('message')}")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")

# Check Password Security
with tab2:
    st.header("Check Password Security")
    box_col1, _, box_col2 = st.columns([2, 1, 3])
    with box_col1:
        password_to_check = st.text_input("Enter Password to Check")
        if st.button("Check Security"):
            with box_col2:
                response = requests.post(
                    f"{BASE_URL}/check-security", json={"password": password_to_check}
                )
                st.write(response.json())
                # Display Strength Progress Bar using custom HTML
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

# List Stored Passwords
with tab3:
    st.header("Stored Passwords")
    if st.button("View Passwords"):
        response = requests.get(f"{BASE_URL}/passwords")
        if response.status_code == 200:
            try:
                # Convert response JSON to a pandas DataFrame
                passwords = response.json()  # Assuming it returns a list of dicts
                df = pd.DataFrame(passwords)

                # Display the DataFrame
                st.dataframe(df)
            except ValueError:
                st.error("Failed to decode JSON response.")
        else:
            st.error(f"Failed to fetch passwords: {response.status_code}")
