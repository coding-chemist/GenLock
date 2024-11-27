from flask import Blueprint, request, jsonify
from .password_utils import generate_password, check_password_security
from .excel_manager import read_passwords, add_password, delete_password
import logging

api = Blueprint('api', __name__)

@api.route('/generate-password', methods=['POST'])
def generate_password_route():
    data = request.json

    # Extract parameters from the request
    length = data.get('length', 12)
    include_special = data.get('include_special', True)

    try:
        # Generate the password and check its security level
        password = generate_password(length, include_special)
        security = check_password_security(password)
        
        # Store password and security info (if applicable)
        add_password(password, security)
        logging.info(f"Password generated: {password}, Security: {security}")

        # Return the password and its security level
        return jsonify({"password": password, "security_level": security})

    except ValueError as e:
        # Handle ValueError (e.g., invalid length)
        logging.error(f"Error generating password: {e}")
        return jsonify({"error": str(e)}), 400

@api.route('/check-security', methods=['POST'])
def check_security_route():
    data = request.json
    password = data.get('password')
    security = check_password_security(password)
    logging.info(f"Checked password: {password}, Security: {security}")
    return jsonify({"password": password, "security_level": security})

@api.route('/passwords', methods=['GET'])
def get_passwords_route():
    passwords = read_passwords()
    return jsonify(passwords)

@api.route('/password/<int:id>', methods=['DELETE'])
def delete_password_route(id):
    if delete_password(id):
        logging.info(f"Password with ID {id} deleted.")
        return '', 204
    else:
        logging.warning(f"Failed to delete password with ID {id}.")
        return jsonify({"error": "Password not found"}), 404
