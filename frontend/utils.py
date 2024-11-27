import streamlit as st


# Read the HTML content
def read_html_file(filepath):
    """Read the HTML content from the file"""
    with open(filepath, "r") as file:
        return file.read()


# Display the HTML content
def display_html(file_path):
    """
    Reads an HTML file, and displays the updated content in a Streamlit app.

    Args:
        file_path (str): Path to the HTML file to be read and updated.
    """
    html_content = read_html_file(file_path)
    st.markdown(html_content, unsafe_allow_html=True)
