# Client Tracker

A console application for storing and searching for clients.

## Features
- Stores client information (first name, last name, status, and additional data).
- Allows searching for clients based on any criteria, provided as a function passed to the search method.
- Supports limiting the number of search results (via the `limit` parameter).
- Updates data for all clients matching a condition, with new values passed as named arguments (`update` method).

## How to run
```
python3 client_tracker.py
```