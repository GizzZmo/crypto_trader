# Contributing to AI-Powered Binance Grid Trading Bot

First off, thank you for considering contributing to this project! It's people like you that make this bot better for everyone.

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**
- **Description**: Clear and concise description of the bug
- **Steps to Reproduce**: Detailed steps to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Screenshots**: If applicable
- **Environment**:
  - OS: [e.g., Windows 11, Ubuntu 22.04]
  - Python Version: [e.g., 3.10.5]
  - Bot Version: [e.g., 0.1.0]
- **Additional Context**: Any other relevant information

### Suggesting Features

Feature suggestions are welcome! Please:

1. Check if the feature is already in the [ROADMAP.md](ROADMAP.md)
2. Search existing issues to avoid duplicates
3. Provide a clear use case and benefits
4. Consider the impact on existing functionality

**Feature Request Template:**
- **Feature Description**: What you want to achieve
- **Use Case**: Why this feature is needed
- **Proposed Solution**: How you think it should work
- **Alternatives**: Alternative solutions you've considered
- **Additional Context**: Screenshots, mockups, examples

### Pull Requests

We actively welcome your pull requests!

1. Fork the repo and create your branch from `main`
2. Make your changes following our code standards
3. Test your changes thoroughly
4. Update documentation if needed
5. Ensure your code passes all checks
6. Submit the pull request

## 🔧 Development Setup

### Prerequisites

- Python 3.9+
- Git
- pip or conda

### Setting Up Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/crypto_trader.git
   cd crypto_trader
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line Length**: Maximum 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Grouped and sorted
  - Standard library imports
  - Third-party imports
  - Local application imports
- **Naming Conventions**:
  - Functions and variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Private methods/variables: `_leading_underscore`

### Code Quality Tools

We use the following tools (run before committing):

```bash
# Code formatting
black bot.py

# Import sorting
isort bot.py

# Linting
pylint bot.py
flake8 bot.py

# Type checking
mypy bot.py
```

### Comments and Documentation

- Write clear, concise comments for complex logic
- Use docstrings for all public functions and classes
- Keep comments up-to-date with code changes
- Explain "why" not "what" in comments

**Docstring Format (Google Style):**
```python
def calculate_grid_levels(lower_bound, upper_bound, num_grids):
    """Calculate price levels for grid trading.
    
    Args:
        lower_bound (float): Minimum price boundary
        upper_bound (float): Maximum price boundary
        num_grids (int): Number of grid levels
        
    Returns:
        list: List of price levels for grid placement
        
    Raises:
        ValueError: If parameters are invalid
    """
    pass
```

## 🧪 Testing

### Writing Tests

- Write unit tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Use meaningful test names

**Test Structure:**
```python
import unittest

class TestGridCalculation(unittest.TestCase):
    def test_calculate_grid_levels_basic(self):
        """Test basic grid level calculation."""
        result = calculate_grid_levels(100, 200, 5)
        self.assertEqual(len(result), 5)
        
    def test_calculate_grid_levels_invalid_input(self):
        """Test that invalid input raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_grid_levels(200, 100, 5)
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_grid.py

# Run with coverage
python -m pytest --cov=. --cov-report=html
```

## 📚 Documentation

### Code Documentation

- Update docstrings for modified functions
- Add inline comments for complex logic
- Keep README.md up-to-date

### User Documentation

When adding features, update:
- README.md - For user-facing features
- ROADMAP.md - For future plans
- docs/ - For detailed guides

## 🔒 Security

### Security Best Practices

- **Never commit API keys or secrets**
- Use environment variables for sensitive data
- Validate all user inputs
- Handle exceptions properly
- Follow the principle of least privilege
- Use secure communication (HTTPS, WSS)

### Reporting Security Vulnerabilities

**DO NOT** open public issues for security vulnerabilities.

Instead:
1. Email the maintainers directly
2. Provide detailed information about the vulnerability
3. Allow time for a fix before public disclosure

See [SECURITY.md](SECURITY.md) for details.

## 🎨 UI/UX Guidelines

### GUI Design Principles

- Maintain consistency with existing UI
- Use CustomTkinter components
- Follow the established color scheme
- Ensure responsive layouts
- Test on different screen sizes
- Consider accessibility (contrast, font size)

### User Experience

- Provide clear error messages
- Show loading states for async operations
- Validate inputs before submission
- Give feedback for user actions
- Keep the interface intuitive

## 🌍 Internationalization

When adding user-facing strings:
- Use i18n placeholders (future feature)
- Avoid hard-coded strings in UI
- Consider cultural differences
- Use clear, simple language

## 📋 Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

**Examples:**
```
feat(ai): add support for multiple AI models

fix(gui): resolve crash on invalid API key

docs(readme): update installation instructions

refactor(trading): simplify grid calculation logic
```

## 🔄 Pull Request Process

1. **Update Documentation**: Ensure README and other docs are updated
2. **Add Tests**: Include tests for new features
3. **Follow Code Style**: Run linters and formatters
4. **Clean Commit History**: Squash commits if necessary
5. **Descriptive PR Title**: Follow commit message format
6. **Complete PR Template**: Fill in all sections
7. **Link Issues**: Reference related issues
8. **Request Review**: Tag relevant reviewers
9. **Address Feedback**: Respond to review comments
10. **Merge**: Maintainers will merge once approved

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation
- Added to the README (significant contributions)

## 📞 Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Create a GitHub Issue
- **Chat**: Join our community (if available)
- **Documentation**: Check the docs/ folder

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unethical or unprofessional conduct

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report violations to the project maintainers.

## 📄 License

By contributing, you agree that your contributions will be licensed under the GNU General Public License v3.0.

---

## 🙏 Thank You!

Your contributions make this project better for everyone. Whether it's code, documentation, bug reports, or feature ideas - every contribution matters!

Happy coding! 🚀
