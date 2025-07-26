Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check input validation', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/inputs')
  })
    it('To check valid input validations', () => {
        cy.get("input[name='input-number']").type('8776554321')
        cy.get('#input-text').type('Cypress Testing')
        cy.get('#input-password').type('Password123')
        cy.get("input[name='input-date']").type('2023-05-05')

        cy.get("button[id='btn-display-inputs']").click()
        cy.get("strong[id='output-number']").should('have.text', '8776554321')
        cy.get("strong[id='output-text']").should('have.text', 'Cypress Testing')
        cy.get("strong[id='output-password']").should('have.text', 'Password123')
        cy.get("strong[id='output-date']").should('have.text', '2023-05-05')

        cy.get("button[class='btn btn-outline-danger ms-2']").click()
    })
})