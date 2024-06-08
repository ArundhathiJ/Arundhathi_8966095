def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]