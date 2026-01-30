# Vendor React Automation

A Python-based automation framework for testing and managing vendor-related React applications.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Vendor React Automation is a comprehensive testing and automation framework designed to streamline vendor management operations in React applications. This project provides automated testing capabilities, workflow automation, and continuous integration support to ensure reliable vendor-related functionalities.

## ✨ Features

- **Automated Testing Suite**: Comprehensive test coverage for vendor management operations
- **Python-Based Framework**: Leverages Python's robust testing ecosystem
- **CI/CD Integration**: Automated workflows using GitHub Actions
- **Modular Architecture**: Clean separation of concerns with organized source and test directories
- **Environment Configuration**: Flexible configuration management using environment variables
- **Test Reporting**: Detailed test execution reports with pytest

## 📁 Project Structure

```
Vendor-React-Automation/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD workflows
├── src/                    # Source code directory
│   ├── __init__.py
│   ├── automation/         # Automation scripts and modules
│   ├── config/             # Configuration management
│   └── utils/              # Utility functions and helpers
├── tests/                  # Test suite directory
│   ├── __init__.py
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── conftest.py         # Pytest configuration and fixtures
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore rules
├── pyproject.toml          # Python project configuration
├── pytest.ini              # Pytest configuration
└── README.md               # Project documentation
```

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- **Git**: Version control system
- **Virtual Environment**: Recommended for dependency isolation

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bhavyabansal-hub/Vendor-React-Automation.git
cd Vendor-React-Automation
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install project dependencies
pip install -e .

# Or install development dependencies
pip install -e ".[dev]"
```

## ⚙️ Configuration

### Environment Variables

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Configure the following variables in `.env`:

```env
# Application Settings
APP_ENV=development
DEBUG=True

# Test Configuration
TEST_BROWSER=chrome
TEST_TIMEOUT=30

# Vendor API Settings
VENDOR_API_URL=http://localhost:3000
VENDOR_API_KEY=your_api_key_here

# Database Configuration (if applicable)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=vendor_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### Project Configuration

The `pyproject.toml` file contains project metadata and dependency specifications. Key sections include:

- **Project Metadata**: Name, version, description, and author information
- **Dependencies**: Required packages for the project
- **Build System**: Build backend configuration
- **Tool Configuration**: Settings for linters, formatters, and test runners

## 💻 Usage

### Running the Automation

```bash
# Run the main automation script
python -m src.automation.main

# Run specific automation module
python -m src.automation.vendor_operations

# Run with custom configuration
python -m src.automation.main --config custom_config.yaml
```

### Common Operations

#### Vendor Management Automation

```python
from src.automation.vendor_operations import VendorAutomation

# Initialize automation
vendor_auto = VendorAutomation()

# Perform vendor operations
vendor_auto.create_vendor(vendor_data)
vendor_auto.update_vendor(vendor_id, updated_data)
vendor_auto.delete_vendor(vendor_id)
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_vendor_operations.py

# Run tests with verbose output
pytest -v

# Run tests matching a pattern
pytest -k "test_vendor"
```

### Test Categories

#### Unit Tests
Tests individual components in isolation:
```bash
pytest tests/unit/
```

#### Integration Tests
Tests component interactions:
```bash
pytest tests/integration/
```

#### End-to-End Tests
Tests complete workflows:
```bash
pytest tests/e2e/
```

### Test Coverage Report

After running tests with coverage, view the HTML report:

```bash
# Generate coverage report
pytest --cov=src --cov-report=html

# Open report in browser
# On Windows:
start htmlcov/index.html
# On macOS:
open htmlcov/index.html
# On Linux:
xdg-open htmlcov/index.html
```

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

The project includes automated CI/CD workflows in `.github/workflows/`:

#### Continuous Integration

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Setup Python
      - Install dependencies
      - Run linters
      - Run tests
      - Upload coverage reports
```

#### Workflow Features

- **Automated Testing**: Runs on every push and pull request
- **Code Quality Checks**: Linting and formatting validation
- **Coverage Reports**: Automatic coverage analysis
- **Multi-Python Support**: Tests across multiple Python versions
- **Dependency Caching**: Faster workflow execution

### Manual Workflow Triggers

```bash
# Trigger workflow manually from GitHub UI
# Navigate to Actions → Select Workflow → Run workflow
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code Quality Tools

#### Linting

```bash
# Run flake8
flake8 src/ tests/

# Run pylint
pylint src/ tests/

# Run black (formatter)
black src/ tests/
```

#### Type Checking

```bash
# Run mypy for type checking
mypy src/
```

### Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

3. **Run tests** to ensure everything works:
   ```bash
   pytest
   ```

4. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub

### Commit Message Convention

Follow conventional commit format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `style:` Code style changes
- `chore:` Maintenance tasks

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create your feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add: amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Write clear, concise commit messages
- Add tests for new features
- Update documentation as needed
- Follow the existing code style
- Ensure all tests pass before submitting PR
- Keep PRs focused on a single feature or fix

### Code Review Process

1. Automated tests must pass
2. Code review by at least one maintainer
3. All comments must be addressed
4. Final approval and merge by project maintainer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Bhavya Bansal** - *Initial work* - [@bhavyabansal-hub](https://github.com/bhavyabansal-hub)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by best practices in test automation and CI/CD
- Built with modern Python testing frameworks

## 📞 Support

For support, please:

- Open an issue on GitHub
- Check existing documentation
- Review closed issues for similar problems

## 🗺️ Roadmap

- [ ] Enhanced test coverage
- [ ] API documentation with Swagger
- [ ] Performance optimization
- [ ] Docker containerization
- [ ] Cloud deployment guides
- [ ] Additional browser support
- [ ] Parallel test execution

## 📊 Project Status

This project is actively maintained and open for contributions.

---

**Note**: This is an automation framework for vendor management in React applications. Ensure you have proper authorization before running automated tests against production systems.
