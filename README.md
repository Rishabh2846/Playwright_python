# Cypress End-to-End Testing Project

This project contains end-to-end (E2E) tests written using [Cypress](https://www.cypress.io/). It is organized to help you learn, write, and run automated browser tests for web applications.

## Project Structure

- `cypress/e2e/1-getting-started/` — Beginner test examples
- `cypress/fixtures/` — Test data files
- `cypress/support/` — Custom commands and support utilities
- `cypress.config.js` — Cypress configuration file
- `package.json` — Project dependencies and scripts

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v12 or higher recommended)
- [npm](https://www.npmjs.com/)

## To use drag and drop functionality
```sh
npm install --save-dev cypress-drag-drop
```

### Installation
1. Clone this repository or download the project files.
2. Install dependencies:
   ```sh
   npm install
   ```

### Running Tests
To open the Cypress Test Runner:
```sh
npx cypress open
```

To run tests in headless mode:
```sh
npx cypress run
```

To run test for only file in headless mode
```sh
npx cypress run --spec "C:\Users\Rishabh Sinha\Documents\cypress\cypress\e2e\1-getting-started\drag_drop.cy.js" --headless
```
To run test for only file in headed mode
```sh
npx cypress run --spec "C:\Users\Rishabh Sinha\Documents\cypress\cypress\e2e\1-getting-started\drag_drop.cy.js" --headed
```

## Writing Tests
- Add new test files in the `cypress/e2e/` directory.
- Use the existing examples as a reference for writing your own tests.

## Resources
- [Cypress Documentation](https://docs.cypress.io/)
- [Cypress Best Practices](https://docs.cypress.io/guides/references/best-practices)

=======
# CI/CD Pipeline
- CI/CD pipeline created using GITHUB actions 
- Whenever there is a push action performed on this repository
- pipeline will triggered
---


- Feel free to contribute or modify the tests as needed for your application!
