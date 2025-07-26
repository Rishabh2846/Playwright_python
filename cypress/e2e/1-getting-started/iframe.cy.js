Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check Iframes', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/iframe')
  })

  it('To check iframe', () => {
    const getIframeDocument = () => {
  return cy
  .get('iframe[id="mce_0_ifr"]')
  // Cypress yields jQuery element, which has the real
  // DOM element under property "0".
  // From the real DOM iframe element we can get
  // the "document" element, it is stored in "contentDocument" property
  // Cypress "its" command can access deep properties using dot notation
  // https://on.cypress.io/its
  .its('0.contentDocument').should('exist')
}

const getIframeBody = () => {
  // get the document
  return getIframeDocument()
  // automatically retries until body is loaded
  .its('body').should('not.be.undefined')
  // wraps "body" DOM element to allow
  // chaining more Cypress commands, like ".find(...)"
  .then(cy.wrap)
}

getIframeBody().find('p').clear();
getIframeBody().find('p').type('This is my new text');
getIframeBody().find('p').should('contain', 'This is my new text');


  })

})