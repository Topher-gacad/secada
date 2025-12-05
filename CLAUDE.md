# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Secada is a Flask web application with MySQL database integration and user authentication system. The application uses Flask-SQLAlchemy ORM with a separation of authentication and user profile data.

## Architecture

### Database Models Structure

The project uses a **multi-model architecture** separating authentication from user profiles:

- **UserAuth** (`models/user_auth.py`): Handles authentication credentials
  - Table: `user_auth`
  - Contains: username, email, password_hash, login tracking
  - Uses Flask-Login's `UserMixin` for session management
  - Password hashing via `werkzeug.security`
  - One-to-one relationship with UserProfile (cascade delete)

- **UserProfile** (`models/user_profile.py`): Stores user information
  - Table: `user_profile`
  - Contains: fname, lname, theme_mode preferences
  - Foreign key to `user_auth.id` (one-to-one)
  - Foreign key to `departments.id` (many-to-one, nullable)

- **Department** (`models/department.py`): Organization structure
  - Table: `departments`
  - Contains: name, code (both unique)
  - One-to-many relationship with UserProfile (lazy='dynamic')

### Relationship Pattern

The models use SQLAlchemy's `back_populates` for bidirectional relationships:
- `UserAuth.user_profile` ↔ `UserProfile.user` (one-to-one)
- `Department.user_profiles` ↔ `UserProfile.department` (one-to-many)

**Important**: `back_populates` refers to the **attribute name** on the related model, NOT the table name or class name.

### Application Entry Point

- `app.py`: Main Flask application
  - Routes: `/` (home), `/login` (auth page)
  - Configuration loaded from `Config` class
  - SQLAlchemy initialization is NOT yet integrated into app.py
  - No database initialization or migrations setup yet

### Configuration System

- `config.py`: Centralized configuration using environment variables
  - Database URI: `mysql+mysqlconnector://` format for Flask-SQLAlchemy
  - SECRET_KEY with development fallback
  - SQLALCHEMY_TRACK_MODIFICATIONS disabled

### Templates

- `templates/auth/login.html`: Login page
- `templates/home/index.html`: Home page
- `templates/dashboard/dash.html`: Dashboard (not yet connected to routes)

## Environment Configuration

Copy `.env.example` to `.env` and configure:

**Required:**
- `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`: MySQL connection
- `SECRET_KEY`: Flask secret key (change in production)
- `PORT`: Development server port

**Optional:**
- `SQLALCHEMY_ECHO`: Enable SQL query logging (True/False)
- Session and security settings (see `.env.example`)

## Development Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Edit .env with your database credentials
```

### Running the Application
```bash
# Run development server
python app.py
```

Server runs on `http://localhost:{PORT}` with debug mode enabled.

### Database Operations

**Note:** Database initialization is not yet implemented in the application. You'll need to:
1. Initialize SQLAlchemy in `app.py` (import and bind `db` instance)
2. Create tables using `db.create_all()` or set up Flask-Migrate for migrations

## Key Dependencies

- Flask 3.1.2: Web framework
- Flask-Login 0.6.3: User session management (UserMixin integration)
- mysql-connector-python 9.5.0: MySQL database driver
- python-dotenv 1.2.1: Environment variable management
- Werkzeug 3.1.4: Password hashing utilities

**Note:** Flask-SQLAlchemy is referenced in code but not in requirements.txt - need to add it.

## Current State & Next Steps

### Completed
- ✅ Database models with relationships defined
- ✅ Configuration system with environment variables
- ✅ Basic Flask routing structure
- ✅ Password hashing utilities in UserAuth model

### Not Yet Implemented
- ❌ SQLAlchemy initialization in `app.py` (db instance not bound to app)
- ❌ Database migrations (Flask-Migrate not installed)
- ❌ Authentication logic (login/logout routes, Flask-Login setup)
- ❌ Route protection/authorization
- ❌ Dashboard functionality
- ❌ Flask-SQLAlchemy in requirements.txt

### Known Issues
- UserProfile model has relationship mismatch: references `'User'` class but should reference `'UserAuth'`
- Department model uses `user_profile` (singular) for relationship name but should be `user_profiles` (plural) to match back_populates
