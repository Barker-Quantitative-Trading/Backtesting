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
        int: The number of rows affected (1 if successful, 0 on failure/conflict).
    """

def get_user_by_username(username):
    """
    Retrieves a user's data by their username.

    Args:
        username (str): The username to search for.

    Returns:
        dict: A dictionary of the user's data, or None if not found.
    """


def get_user_with_password_hash(username):
    """
    Retrieves a user's data including the password hash.
    This should only be used for authentication checks.

    Args:
        username (str): The username to search for.

    Returns:
        dict: A dictionary of the user's data, or None if not found.
    """

def delete_user(username):
    """
    Deletes a user from the database by their username.

    Args:
        username (str): The username of the user to delete.

    Returns:
        int: The number of rows affected.
    """