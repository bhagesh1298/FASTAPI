# FastAPI Full Stack Project - Technical Documentation

## Table of Contents
1. [Project Architecture](#project-architecture)
2. [Dependencies & Libraries](#dependencies--libraries)
3. [File Structure Breakdown](#file-structure-breakdown)
4. [Core Components](#core-components)
5. [Database Layer](#database-layer)
6. [API Layer](#api-layer)
7. [Authentication System](#authentication-system)
8. [Frontend Integration](#frontend-integration)
9. [Configuration Management](#configuration-management)
10. [Development Workflow](#development-workflow)

---

## Project Architecture

This FastAPI project follows a **layered architecture** pattern:

```
┌─────────────────────────────────────┐
│              Frontend               │
│         (HTML/CSS/JS)              │
├─────────────────────────────────────┤
│              API Layer              │
│        (FastAPI Routes)            │
├─────────────────────────────────────┤
│           Service Layer             │
│        (Business Logic)            │
├─────────────────────────────────────┤
│            Data Layer               │
│    (SQLAlchemy Models & ORM)       │
├─────────────────────────────────────┤
│             Database                │
│       (SQLite/PostgreSQL)          │
└─────────────────────────────────────┘
```

**Benefits of this architecture:**
- **Separation of Concerns**: Each layer has a specific responsibility
- **Maintainability**: Easy to modify individual components
- **Testability**: Each layer can be tested independently
- **Scalability**: Easy to extend and add new features

---

## Dependencies & Libraries

### Core Framework
- **FastAPI (0.104.1)**
  - Modern, fast web framework for building APIs
  - Automatic API documentation (Swagger UI/ReDoc)
  - Built-in data validation with Pydantic
  - Async support out of the box

### Server & ASGI
- **Uvicorn (0.24.0)**
  - Lightning-fast ASGI server
  - Hot reload during development
  - Production-ready performance

### Database & ORM
- **SQLAlchemy (2.0.23)**
  - Python SQL toolkit and ORM
  - Database abstraction layer
  - Support for multiple database backends
  
- **Alembic (1.12.1)**
  - Database migration tool
  - Version control for database schema
  - Auto-generates migration scripts

### Authentication & Security
- **python-jose[cryptography] (3.3.0)**
  - JSON Web Token (JWT) implementation
  - Cryptographic signing and verification
  
- **passlib[bcrypt] (1.7.4)**
  - Password hashing library
  - Bcrypt algorithm for secure password storage

### Data Validation & Serialization
- **Pydantic (2.5.0)**
  - Data validation using Python type annotations
  - JSON serialization/deserialization
  - Integration with FastAPI for request/response models

- **Pydantic-Settings (2.1.0)**
  - Settings management using Pydantic
  - Environment variable loading
  - Configuration validation

### Template Engine & Static Files
- **Jinja2 (3.1.2)**
  - Modern templating engine
  - Template inheritance and macros
  - Auto-escaping for security

- **python-multipart (0.0.6)**
  - Handles multipart form data
  - File uploads support
  - Form data parsing

### Configuration & Environment
- **python-dotenv (1.0.0)**
  - Loads environment variables from .env files
  - Development/production configuration separation
  - Secure secrets management

### Database Driver
- **psycopg2-binary (2.9.9)**
  - PostgreSQL adapter for Python
  - Efficient database connections
  - Production-ready performance

### Testing Framework
- **pytest (7.4.3)**
  - Testing framework
  - Fixtures and parametrized tests
  - Plugin ecosystem

- **pytest-asyncio (0.21.1)**
  - Async testing support
  - Test async functions and coroutines

- **httpx (0.25.2)**
  - HTTP client for testing APIs
  - Async/sync support
  - Drop-in replacement for requests

---

## File Structure Breakdown

### `/app` - Main Application Directory

#### `/app/core` - Core Configuration
- **`config.py`**: Application settings and configuration
- **`security.py`**: Authentication utilities (JWT, password hashing)
- **`deps.py`**: Dependency injection for FastAPI routes

#### `/app/models` - Database Models
- **`user.py`**: User SQLAlchemy model
- **`item.py`**: Item SQLAlchemy model
- Purpose: Define database table structure and relationships

#### `/app/schemas` - Pydantic Schemas
- **`user.py`**: User request/response schemas
- **`item.py`**: Item request/response schemas  
- **`auth.py`**: Authentication schemas
- Purpose: Data validation and API documentation

#### `/app/services` - Business Logic
- **`user_service.py`**: User-related business operations
- **`item_service.py`**: Item-related business operations
- Purpose: Encapsulate business logic, database operations

#### `/app/api/v1` - API Routes
- **`auth.py`**: Authentication endpoints
- **`users.py`**: User CRUD endpoints
- **`items.py`**: Item CRUD endpoints
- Purpose: HTTP endpoint definitions and routing

#### `/app/database` - Database Configuration
- **`database.py`**: SQLAlchemy engine, session management
- Purpose: Database connection and session handling

### Frontend Files
- **`/static`**: CSS, JavaScript, images
- **`/templates`**: HTML templates (Jinja2)
- **`main.py`**: FastAPI application entry point

### Configuration Files
- **`requirements.txt`**: Python dependencies
- **`.env.example`**: Environment variables template
- **`.gitignore`**: Git ignore patterns
- **`README.md`**: Project documentation

---

## Core Components

### 1. FastAPI Application (`main.py`)
```python
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="A FastAPI full-stack project",
    docs_url="/docs",
    redoc_url="/redoc"
)
```

**Key Features:**
- Automatic API documentation
- CORS middleware for cross-origin requests
- Static file serving
- Router inclusion for modular routes

### 2. Configuration Management (`app/core/config.py`)
```python
class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Full Stack Project"
    SECRET_KEY: str = "your-secret-key"
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        env_file = ".env"
```

**Benefits:**
- Type-safe configuration
- Environment-specific settings
- Validation of configuration values

### 3. Database Models (`app/models/`)
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    # ... more fields
```

**Features:**
- SQLAlchemy ORM models
- Relationships between tables
- Automatic timestamp fields
- Indexing for performance

---

## Database Layer

### SQLAlchemy Configuration
```python
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### Database Session Management
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Benefits:**
- Automatic session cleanup
- Connection pooling
- Transaction management

### Model Relationships
```python
# User model
items = relationship("Item", back_populates="owner")

# Item model  
owner = relationship("User", back_populates="items")
```

---

## API Layer

### Route Organization
```
/api/v1/auth/     - Authentication endpoints
/api/v1/users/    - User management
/api/v1/items/    - Item management
```

### Dependency Injection
```python
@router.get("/me")
def read_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

### Response Models
```python
@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Implementation
```

---

## Authentication System

### JWT Implementation
1. **Login Process:**
   - User provides username/password
   - Server validates credentials
   - Returns JWT access token

2. **Protected Routes:**
   - Client sends token in Authorization header
   - Server validates token
   - Extracts user information

### Security Features
- **Password Hashing**: Bcrypt algorithm
- **Token Expiration**: Configurable token lifetime
- **Secure Headers**: Bearer token authentication

---

## Frontend Integration

### Static Files Structure
```
/static/
├── css/
│   └── style.css     # Responsive CSS
└── js/
    └── main.js       # API interaction
```

### Template System
- **Jinja2 Templates**: Server-side rendering
- **Responsive Design**: Mobile-friendly interface
- **API Integration**: JavaScript functions for API calls

---

## Configuration Management

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost/db

# Security
SECRET_KEY=your-secure-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
PROJECT_NAME=FastAPI Project
```

### Settings Validation
- **Type Checking**: Pydantic validates types
- **Required Fields**: Fails if missing required config
- **Default Values**: Sensible defaults for development

---

## Development Workflow

### 1. Local Development Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env

# Start development server
python main.py
```

### 2. Database Migrations
```bash
# Generate migration
alembic revision --autogenerate -m "Add new table"

# Apply migration
alembic upgrade head
```

### 3. Testing
```bash
# Run tests
pytest

# With coverage
pytest --cov=app tests/
```

### 4. Production Deployment
```bash
# Install production dependencies
pip install -r requirements.txt

# Set production environment
export DATABASE_URL=postgresql://...
export SECRET_KEY=production-secret

# Run with production server
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## API Endpoints Reference

### Authentication
- `POST /api/v1/auth/login` - User login

### User Management
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/me` - Get current user
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Item Management
- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/` - Get user's items
- `GET /api/v1/items/{id}` - Get item by ID
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

---

## Security Considerations

1. **Password Security**: Bcrypt hashing with salt
2. **JWT Security**: Secure secret key, token expiration
3. **Input Validation**: Pydantic schema validation
4. **SQL Injection**: SQLAlchemy ORM protection
5. **CORS**: Configurable cross-origin policies

---

## Performance Optimizations

1. **Database Indexing**: Key columns indexed
2. **Connection Pooling**: SQLAlchemy connection management
3. **Async Support**: FastAPI async capabilities
4. **Response Caching**: Static file caching
5. **Query Optimization**: Efficient database queries

---

This documentation provides a comprehensive overview of the FastAPI project structure, components, and implementation details. Each component is designed to work together to create a robust, scalable, and maintainable web application.
