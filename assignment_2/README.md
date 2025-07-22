### Assignment 2 - simple flask app.
<br>A web application with an HTML interface and REST API, built using a web framework (e.g., Flask) and ORM (e.g., SQLAlchemy), supporting CRUD operations on a relational database with a single table (ID, continuous features as floats, one categorical feature as int), with full data validation and proper error handling (400/404).
Supported routes:
- / – home page displaying all records in a table with delete buttons,
- /add – form to add a new record (POST with validation),
- /delete/<record_id> – deletes a record by ID (POST, 404 if not found),
- GET /api/data – returns all records as JSON,
- POST /api/data – adds a new record from JSON input (400 on validation error),
- DELETE /api/data/<record_id> – deletes a record by ID (404 if not found).
Validation ensures correct data types and formats. On failure, appropriate HTTP responses with error messages are returned. Basic navigation and optional custom styling are supported.
