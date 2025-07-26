describe ( 'To check login functionality using fixture file', () => {
 
    let username, password,expectedText ;
    before(() => {
  cy.fixture('testdata').then((data) => {
    username = data.name;
    password = data.password;
    expectedText = data.expected;
    });
  })

  

  it('To check valid login using fixture file', () => {
     cy.visit('https://practice.expandtesting.com/login')
    cy.get('#username').type(username)
    cy.get('#password').type(password)
    cy.get("button[type='submit']").click()
    cy.contains(expectedText)
  })

   /* it('To check Invalid password', () => {
 
    cy.get('#username').type('admin')
    cy.get('#password').type('admin')
    cy.get("button[type='submit']").click()
    cy.contains('Your password is invalid!')
    
  })*/

})
