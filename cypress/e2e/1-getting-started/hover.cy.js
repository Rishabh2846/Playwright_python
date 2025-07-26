Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check Hover functionality', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/hovers')
  })

  it('To check hover functionality', () => {
 cy.get("img[data-testid='img-user-1']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user1');

cy.get("img[data-testid='img-user-2']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user2');

cy.get("img[data-testid='img-user-3']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user3');
})

it('To click on link after hover functionality on user 1', () => {
 cy.get("img[data-testid='img-user-1']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user1');
cy.get("a[href='/users/1']").click({force: true });
cy.url().should('include', 'https://practice.expandtesting.com/users/1');
cy.get('h2').should('contain', 'Welcome user1');
cy.go('back');

})

it('To click on link after hover functionality on user 2', () => {
 cy.get("img[data-testid='img-user-2']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user2');
cy.get("a[href='/users/2']").click({force: true });
cy.url().should('include', 'https://practice.expandtesting.com/users/2');
cy.get('h2').should('contain', 'Welcome user2');
cy.go('back');

})

it('To click on link after hover functionality on user 3', () => {
 cy.get("img[data-testid='img-user-3']").trigger('mouseover');
cy.get('h5').should('contain', 'name: user3');
cy.get("a[href='/users/3']").click({force: true });
cy.url().should('include', 'https://practice.expandtesting.com/users/3');
cy.get('h2').should('contain', 'Welcome user3');
cy.go('back');

})

})