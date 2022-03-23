// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

const MAX_INPUT_LENGTH = 500

Cypress.Commands.add(`submitMaxLengthInput`, () => {
    cy.visit(`http://localhost:3000`)
    cy.get('#sentence').type(`x`.repeat(MAX_INPUT_LENGTH))
    cy.get(`#submit-btn`).click()
})

Cypress.Commands.add(`submitInput`, input => {
    cy.visit(`http://localhost:3000`)
    cy.get('#sentence').type(input)
    cy.get(`#submit-btn`).click()
})