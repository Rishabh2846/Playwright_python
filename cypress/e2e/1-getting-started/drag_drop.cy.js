/* To use drag and drop functionality we need to install cypress-drag-drop plugin */
import 'cypress-drag-drop';

Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test due to any uncaught exception
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
  return false;
});

describe( 'To check drag and drop functionality', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/drag-and-drop')
  })
    it('To check drag and drop functionality', () => {
    cy.get('#column-a').drag("#column-b")
    })
})