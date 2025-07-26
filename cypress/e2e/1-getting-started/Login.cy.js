describe ( 'To check login functionality', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/login')
  })
  it('To check valid login', () => {
    cy.get('#username').type('practice')
    cy.get('#password').type('SuperSecretPassword!')
    cy.get("button[type='submit']").click()
    cy.contains('You logged into a secure area!')
  })

    it('To check Invalid password', () => {
 
    cy.get('#username').type('admin')
    cy.get('#password').type('admin')
    cy.get("button[type='submit']").click()
    cy.contains('Your password is invalid!')
    
  })

})
