Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});

describe( 'To check Javascript alerts', () => {
  beforeEach(() => {
    cy.visit('https://practice.expandtesting.com/js-dialogs')
  })

  it('To check alert dailog box', () => {
    cy.get("button[id='js-alert']").click();
    cy.on('window:alert', (alertText) => {
  expect(alertText).to.equal('I am a Js Alert');
  return true;
  });
  cy.get("p[id='dialog-response']").should('contain', 'OK');
  })

  it('To check confirm dailog box - click OK', () => {
     cy.get("button[id='js-confirm']").click();
    cy.on('window:confirm', (confirmText) => {
  expect(confirmText).to.equal('I am a Js Confirm');
  return true; 
   });
    cy.get("p[id='dialog-response']").should('contain', 'Ok');
  })

  it('To check confirm dailog box - click Cancel', () => {
      cy.get("button[id='js-confirm']").click();
   cy.on('window:confirm', (confirmText) => {
  expect(confirmText).to.equal('I am a Js Confirm');
  return false; 
    });
     cy.get("p[id='dialog-response']").should('contain', 'Cancel');
  })

it('should handle a prompt dialog', () => {
    cy.window().then((win) => {
    cy.stub(win, 'prompt').returns('testing');
    return true; // Ensure the stub is set up
  });
    
    cy.get("button[id='js-prompt']").click();
 
  cy.get("p[id='dialog-response']").should('contain', 'testing');
});

})