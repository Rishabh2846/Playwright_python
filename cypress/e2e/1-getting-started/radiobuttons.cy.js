Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check radio button', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/radio-buttons')
  })
  it('To check color radio button', () => {
    cy.get("input[id='blue']").check().should('be.checked')
   cy.get("input[id='red']").check().should('be.checked')
   cy.get("input[id='yellow']").check().should('be.checked')
   cy.get("input[id='black']").check().should('be.checked')
    cy.get("input[id='green']").should('be.visible')

  })

})