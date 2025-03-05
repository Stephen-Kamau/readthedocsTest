```rst
Fakemail - Python Library for Generating Fake Email Addresses
=============================================================

Fakemail is a Python library for generating random, fake email addresses, perfect for testing and development purposes.

Project Documentation
----------------------

The documentation for this project is hosted on `Read the Docs <https://fakemail.readthedocs.io/en/stable/>`.

Tutorial
--------

Read the full tutorial to set up this project on Read the Docs: 

`Read the Docs tutorial <https://docs.readthedocs.io/en/stable/tutorial/>`


Usage
-----

Here’s an example of how to use the Fakemail library to generate fake email addresses:

```python
from fakemail import get_random_emails

# Generate a list of random emails with a specific domain
emails = get_random_emails("test.com")

# Print the generated emails
print(emails)
```

Example output:

```
['alice34@test.com', 'bob21@test.com', 'charlie56@test.com', 'dave11@test.com', 'eve99@test.com']
```

API Reference
-------------

### get_random_emails(domain=None)

Return a list of random email addresses.

**Parameters:**

- `domain`: Optional string to specify the email domain. Defaults to "example.com".
  
**Raises:**

- `fakemail.InvalidDomainError`: If the domain is invalid.

**Returns:**

- A list of randomly generated email addresses with the specified domain.

**Example:**

```python
emails = get_random_emails("fakemail.com")
```