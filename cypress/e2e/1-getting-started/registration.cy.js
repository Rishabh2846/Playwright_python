Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check input validation', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/login')
  })
  it('To check valid registration', () => {
    cy.get("a[href='/register']").click()
    cy.get("input[name='username']").type('admin')
    cy.get("input[name='password']").type('admin')
    cy.get("input[name='confirmPassword']").type('admin')
    cy.get("button[class='btn btn-bg btn-primary d-block w-100']").click()

  })

})