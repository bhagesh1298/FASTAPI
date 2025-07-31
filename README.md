# FastAPI Full Stack Project

A complete full-stack web application built with FastAPI, featuring authentication, CRUD operations, and a responsive frontend.

## Features

- 🔐 **JWT Authentication** - Secure user authentication with JSON Web Tokens
- 👥 **User Management** - Complete CRUD operations for user accounts
- 📦 **Item Management** - Create, read, update, and delete items with ownership
- 🗄️ **Database Integration** - SQLAlchemy ORM with PostgreSQL/SQLite support
- 📱 **Responsive Frontend** - Modern HTML/CSS/JavaScript interface
- 📚 **Auto-generated API Docs** - Interactive Swagger UI and ReDoc documentation
- 🧪 **Test Ready** - Structured for easy testing implementation

## Project Structure

```
fastapi-project/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py          # Authentication endpoints
│   │       ├── users.py         # User CRUD endpoints
│   │       └── items.py         # Item CRUD endpoints
│   ├── core/
│   │   ├── config.py           # Application configuration
│   │   ├── security.py         # Security utilities
│   │   └── deps.py             # Dependencies
│   ├── models/
│   │   ├── user.py             # User database model
│   │   └── item.py             # Item database model
│   ├── schemas/
│   │   ├── user.py             # User Pydantic schemas
│   │   ├── item.py             # Item Pydantic schemas
│   │   └── auth.py             # Authentication schemas
│   ├── services/
│   │   ├── user_service.py     # User business logic
│   │   └── item_service.py     # Item business logic
│   └── database/
│       └── database.py         # Database configuration
├── static/
│   ├── css/
│   │   └── style.css           # Stylesheets
│   └── js/
│       └── main.js             # JavaScript functionality
├── templates/
│   └── index.html              # HTML templates
├── tests/                      # Test directory
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # Project documentation
```

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to your project directory
cd D:\RND\FASTAPI

# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy environment template
copy .env.example .env

# Edit .env file with your configuration
# - Set your SECRET_KEY
# - DATABASE_URL is already configured for PostgreSQL
# - Update other settings as needed
```

### 3. Run the Application

```bash
# Start the development server using the batch file (Windows)
start .\start.bat

# Or activate virtual environment and use uvicorn directly
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Access the Application

- **Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - Login and get access token

### Users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - Get all users (requires authentication)
- `GET /api/v1/users/me` - Get current user profile
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Items
- `POST /api/v1/items/` - Create a new item
- `GET /api/v1/items/` - Get user's items
- `GET /api/v1/items/{id}` - Get item by ID
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

## Usage Examples

### 1. Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "username": "testuser",
       "full_name": "Test User",
       "password": "secretpassword"
     }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=secretpassword"
```

### 3. Create an Item

```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{
       "title": "My First Item",
       "description": "This is a test item",
       "price": 29.99
     }'
```

## Database Configuration

### SQLite (Default)
The application uses SQLite by default for development. No additional setup required.

### PostgreSQL (Production)
1. Install PostgreSQL
2. Create a database
3. Update `.env` file:
   ```
   DATABASE_URL=postgresql://username:password@localhost/your_database_name
   ```

## Development

### Adding New Features
1. **Models**: Add new database models in `app/models/`
2. **Schemas**: Define Pydantic schemas in `app/schemas/`
3. **Services**: Implement business logic in `app/services/`
4. **APIs**: Create endpoints in `app/api/v1/`
5. **Tests**: Add tests in `tests/`

### Code Structure Guidelines
- **Models**: Database table definitions using SQLAlchemy
- **Schemas**: Data validation and serialization with Pydantic
- **Services**: Business logic layer
- **APIs**: HTTP endpoint definitions
- **Core**: Configuration, security, and dependencies

## Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt password hashing
- **CORS Protection**: Configurable CORS middleware
- **Input Validation**: Pydantic model validation
- **SQL Injection Prevention**: SQLAlchemy ORM protection

## Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## Deployment

### Docker (Recommended)
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
- `SECRET_KEY`: JWT secret key (required)
- `DATABASE_URL`: Database connection string
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: CORS allowed origins

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
