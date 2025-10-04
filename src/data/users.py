"""
users.py

This module provides functions for managing user accounts in the database.
It handles creating, retrieving, and deleting user records, including
password hashing for security. 

"""
from .db import execute_query, execute_update
from .utils.security import hash_password


def create_user(username, email, password, settings):
    """
    Creates a new user in the database with a hashed password.

    Args:
        username (str): The user's chosen username.
        email (str): The user's email address.
        password (str): The user's plaintext password.
        settings (JSONB): json file for additional settings

    Returns:
        int: The id that is created for the user
    """

def get_user_by_username(id):
    """
    Retrieves a user's data by their username.

    Args:
        id (int): To search for the user.

    Returns:
        dict: A dictionary of the user's data, or None if not found.
    """


def get_user_with_password_hash(id):
    """
    Retrieves a user's data including the password hash.
    This should only be used for authentication checks.

    Args:
        id (int): To search for the user.

    Returns:
        dict: A dictionary of the user's data, or None if not found.
    """

def delete_user(id):
    """
    Deletes a user from the database by their username.

    Args:
        id (int): To search for the user.

    Returns:
        int: The number of rows affected.
    """
