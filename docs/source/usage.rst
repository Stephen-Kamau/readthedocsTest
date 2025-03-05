Usage
=====

.. _installation:

Installation
------------

To use Fakemail, first install it using pip:

.. code-block:: console

   (.venv) $ pip install fakemail

Creating Fake Emails
--------------------

To retrieve a list of random email addresses, you can use the ``fakemail.get_random_emails(domain="test.com")`` function:

.. autofunction:: fakemail.get_random_emails

The ``domain`` parameter is an optional string. If not provided, it will default to ``"example.com"``. You can specify a custom domain like ``"p33.com"`` for your generated emails.

For example:

>>> from fakemail import get_random_emails
>>> get_random_emails("test.com")
['alice34@test.com', 'bob21@test.com', 'charlie56@test.com', 'dave11@test.com', 'eve99@test.com']

Handling Invalid Domains
-------------------------

If you provide an invalid domain, the function will raise an exception.

.. autoexception:: fakemail.InvalidDomainError

For example:

>>> from fakemail import get_random_emails
>>> get_random_emails(123)
Traceback (most recent call last):
    ...
fakemail.InvalidDomainError: The domain must be a string.
