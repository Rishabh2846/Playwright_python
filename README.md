
# Selenium Python BDD Testing Project

This project contains end-to-end (E2E) tests written using Selenium WebDriver with Python, following the BDD (Behavior-Driven Development) approach using Behave.

## Project Structure

- `features/` — Contains all BDD feature files and step definitions
- `features/steps/` — Step implementation files for Behave
- `test_*.py` — Standalone Selenium Python scripts (if any)

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Installation
1. Clone this repository or download the project files.
2. (Recommended) Create a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running BDD Tests
To run all Behave BDD tests:
```sh
behave
```

To run a specific feature file:
```sh
behave features/your_feature_file.feature
```

## Writing Tests
- Add new feature files in the `features/` directory.
- Implement step definitions in `features/steps/`.
- Use Selenium WebDriver for browser automation in your steps.

## Resources
- [Behave Documentation](https://behave.readthedocs.io/en/stable/)
- [Selenium with Python Docs](https://selenium-python.readthedocs.io/)

---

# CI/CD Pipeline
- CI/CD pipeline created using GitHub Actions
- Whenever there is a push action performed on this repository, the pipeline will be triggered

---

Feel free to contribute or modify the tests as needed for your application!
