"""
user_secrets.py

Manages the storage and retrieval of encrypted user-specific secrets (e.g., API keys).
Secrets are encrypted before being stored in the database and decrypted upon retrieval.
"""

def store_user_secret(user_id: str, key_name: str, secret_value: str) -> int:
    """
    Encrypts and stores a user's secret in the database.
    If a secret with the same user_id and key_name already exists, it will be updated.

    Args:
        user_id (str): The UUID of the user.
        key_name (str): A descriptive name for the secret (e.g., 'tiingo_api_key').
        secret_value (str): The plaintext secret value to be stored.

    Returns:
        int: The number of rows affected (1 on insert/update, 0 on failure).
    """

def get_user_secret(user_id: str, key_name: str) -> str | None:
    """
    Retrieves and decrypts a user's secret from the database.

    Args:
        user_id (str): The UUID of the user.
        key_name (str): The name of the secret to retrieve.

    Returns:
        str: The decrypted plaintext secret value, or None if not found.
    """


def delete_user_secret(user_id: str, key_name: str) -> int:
    """
    Deletes a specific user secret from the database.

    Args:
        user_id (str): The UUID of the user.
        key_name (str): The name of the secret to delete.

    Returns:
        int: The number of rows affected (1 on deletion, 0 if not found).
    """