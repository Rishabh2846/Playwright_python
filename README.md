# Web Automation Testing Framework with Playwright

This project is a comprehensive web automation testing framework that uses Playwright with TypeScript. The framework is designed to test various web functionalities including form inputs, API interactions, and complex UI behaviors.

## Features

- **Testing Framework**:
  - Playwright for modern web testing
  - TypeScript for type-safe test scripts
  - Support for multiple browsers (Chromium, Firefox, WebKit)
  - Parallel test execution

- **Test Scenarios**:
  - Form Input Validation
  - API Testing through UI
  - Drag and Drop Operations
  - Hover Interactions
  - Login/Authentication
  - Web Input Testing

## Project Structure

```
└── Playwright_python/
    ├── tests/               # Playwright TypeScript tests
    │   ├── API_testing.spec.ts
    │   ├── Drag_&_Drop.spec.ts
    │   ├── Hover.spec.ts
    │   ├── Login_page.spec.ts
    │   └── Web_inputs.spec.ts
    ├── playwright-report/   # Test execution reports
    ├── .github/workflows/   # CI/CD configuration
    ├── playwright.config.ts # Playwright configuration
    ├── package.json        # Node.js dependencies
    └── node_modules/       # Installed dependencies

```

## Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Install Playwright browsers:
```bash
npx playwright install
```

3. Install Playwright system dependencies:
```bash
npx playwright install-deps
```

## Running Tests

### Running Tests
```bash
npx playwright test
```

### Running a Specific Test File
```bash
npx playwright test tests/filename.spec.ts
```

## Test Categories

1. **API Testing**
   - Health check endpoints
   - User registration
   - Authentication
   - Response validation

2. **UI Testing**
   - Form input validation
   - Drag and drop functionality
   - Hover interactions
   - Alert handling
   - Radio button interactions

3. **Authentication Testing**
   - Login functionality
   - Secure area access
   - Logout verification

4. **Input Validation**
   - Text inputs
   - Number inputs
   - Date inputs
   - Password fields

## CI/CD Integration

The project includes GitHub Actions workflows for continuous integration:
- Automated test execution on push and pull requests
- Browser installation and setup
- Test report generation and artifact storage
- Multi-browser testing support

## Test Reports

- Playwright HTML reports are generated after test execution
- Reports include:
  - Test execution status
  - Screenshots for failed tests
  - Trace viewer for debugging
  - Performance metrics

## Dependencies

### Node.js Dependencies
- @playwright/test
- @types/node

## Browser Support

- Chromium
- Firefox
- WebKit
- Mobile browsers (configured but disabled by default)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the ISC License.