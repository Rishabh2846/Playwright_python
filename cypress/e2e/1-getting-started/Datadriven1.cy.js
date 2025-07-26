describe ( 'To check login functionality using fixture file', () => {
 
    beforeEach(() => {
     cy.visit('https://practice.expandtesting.com/login')
    })

  it('To check valid login using fixture file(valid scenario)', () => {

     cy.fixture('testdata1').then((data) => {

        data.forEach((userdata) => {
        if(userdata.name === 'practice' && userdata.password === 'SuperSecretPassword!') {
        cy.get('#username').type(userdata.name)
        cy.get('#password').type(userdata.password)
        cy.get("button[type='submit']").click()
        cy.contains(userdata.expected)
        
        }
        
        });

        })

    })

    it('To check invalid login using fixture file(invalid scenario)', () => {
    
         cy.fixture('testdata1').then((data) => {
    
            data.forEach((userdata) => {
            if(userdata.name != 'practice' && userdata.password != 'SuperSecretPassword') {
            cy.get('#username').type(userdata.name)
            cy.get('#password').type(userdata.password)
            cy.get("button[type='submit']").click()
            cy.contains(userdata.expected)
            
            }
            
            });
    
            })
    
        })

})
