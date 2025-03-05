"""
Fakemail - Python library for generating fake email addresses.
"""

__version__ = "0.1.0"


class InvalidDomainError(Exception):
    """Raised if the domain is invalid."""
    pass


import random

def get_random_emails(domain=None):
    """
    Return a list of random email addresses.

    :param domain: Optional "domain" for the emails.
    :type domain: str or None
    :raise fakemail.InvalidDomainError: If the domain is invalid.
    :return: The email addresses list.
    :rtype: list[str]
    """
    if domain and not isinstance(domain, str):
        raise InvalidDomainError("The domain must be a string.")

    fake_names = ["alice", "bob", "charlie", "dave", "eve"]
    if domain is None:
        domain = "example.com"
    
    emails = [f"{name}{random.randint(1, 100)}@{domain}" for name in fake_names]
    
    return emails
