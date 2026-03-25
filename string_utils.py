import re


def format_slug(text):
    """
    Converts a string into a URL-friendly slug.
    - Trims whitespace, replaces spaces with hyphens, removes special chars.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text.strip()) == 0:
        raise ValueError("Input cannot be empty")

    text = text.lower().replace(" ", "-")
    text = re.sub(r'[^a-z0-9-]', '', text)
    return re.sub(r'-+', '-', text).strip("-")


def reverse_and_clean(text):
    """
    Reverses a string and removes any digits.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Remove all digits using regex
    cleaned = re.sub(r'\d', '', text)
    # Reverse the string
    return cleaned[::-1]


def get_initials(full_name):
    """
    Extracts uppercase initials from a full name.
    Example: "John Quincy Doe" -> "JQD"
    """
    if not isinstance(full_name, str):
        raise TypeError("Input must be a string")

    parts = full_name.strip().split()
    if not parts:
        raise ValueError("Name cannot be empty")

    return "".join([name[0].upper() for name in parts])