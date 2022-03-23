describe(`Max input length then clicking submit button`, () => {
    it(`Hides the bad input error message`, () => {
        cy.submitMaxLengthInput()
        cy.get(`#error-message`).should(`be.hidden`)
    })
    it(`Disables the submission button`, () => {
        cy.submitMaxLengthInput()
        cy.get(`#submit-btn`).should(`be.disabled`)
    })
    it(`Hides the submission button text`, () => {
        cy.submitMaxLengthInput()
        cy.get(`#submit-btn-text`).should(`be.hidden`)
    })
    it(`Shows the submission progress spinner`, () => {
        cy.submitMaxLengthInput()
        cy.get(`#progress`).should(`be.visible`)
    })
    it(`Appends the results in the results area after request completion`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitMaxLengthInput()
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`#result`).should(`have.descendants`, `ul`)
            cy.get(`li`).should(`have.length`, 6)
            cy.get(`li:nth-child(1)`).should(`include.text`, `Identity attack : `)
            cy.get(`li:nth-child(2)`).should(`include.text`, `Insult : `)
            cy.get(`li:nth-child(3)`).should(`include.text`, `Obscenity : `)
            cy.get(`li:nth-child(4)`).should(`include.text`, `Severe toxicity : `)
            cy.get(`li:nth-child(5)`).should(`include.text`, `Threat : `)
            cy.get(`li:nth-child(6)`).should(`include.text`, `Toxicity : `)
            cy.get(`li`).invoke(`text`).should(`match`, /[a-zA-Z]+\s[a-zA-Z]+\s[:]\s(([1-9]?[0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
    it(`Resets submission button after request completion`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitMaxLengthInput()
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`#submit-btn`).should(`be.enabled`)
            cy.get(`#submit-btn-text`).should(`be.visible`)
            cy.get(`#progress`).should(`be.hidden`)
        })
    })
})