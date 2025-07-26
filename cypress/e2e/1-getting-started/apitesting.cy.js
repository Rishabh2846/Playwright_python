Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false prevents Cypress from failing the test
  if (err.message.includes('adsbygoogle.push() error')) {
    return false;
  }
});
describe( 'API testing', () => {

  it('To check GET method', () => {
       cy.request("GET",
           "practice.expandtesting.com/notes/api/health-check")
    .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property("message", "Notes API is Running");
    });
        })
    })

    it('To check POST method for user registration', () => {
  cy.request({
    method: "POST",
    url: "https://practice.expandtesting.com/notes/api/users/register",
    body: {
      name: "testiuyghgkjbbb",
      email: "testnkjnkjhg@tyh.com",
      password: "Password12335345435",
    },
    failOnStatusCode: false // Prevent Cypress from failing the test on non-2xx status
  }).then((response) => {
    if (response.status === 409) {
      expect(response.body).to.have.property("message", "An account already exists with the same email address");
    } else if (response.status === 201) {
      expect(response.body).to.have.property("message", "User account created successfully");
    } else {
      throw new Error("Unexpected status code: " + response.status);
    }
  });

  
})