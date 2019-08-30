"""
The Application Services and/or Command Handlers contain the logic to unfold a use case,
a business process.

Typically, their role is to:
- use a repository to find one or several entities;
- tell those entities to do some domain logic;
- and use the repository to persist the entities again, effectively saving the data changes.
"""
