describe(`Visiting home page and then doing nothing`, () => {
    it(`Shows an empty input field`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#sentence`).should(`be.empty`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Error message is hidden`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#error-message`).should(`be.hidden`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Submit button is disabled`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#submit-btn`).should(`be.disabled`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Text on the button is visible`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#submit-btn-text`).should(`be.visible`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Loading progress spinner of submit button is hidden`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#progress`).should(`be.hidden`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Result area is empty`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#result`).should(`be.empty`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`Footer text is visible`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#txt-footer`).should(`be.visible`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`navbar text is visible`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#txt-navbar`).should(`be.visible`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`'Write a sentence' is visible`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#msg`).should(`be.visible`)
    })
})

describe(`Visiting home page and then doing nothing`, () => {
    it(`'the result are:' is visible`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#result-msg`).should(`be.visible`)
    })
})

describe(`Visiting home page and then typing a letter`, () => {
    it(`Submit button is enabled`, () => {
        cy.visit(`http://localhost:3000`)
        cy.get(`#sentence`).type("i");

        cy.get(`#submit-btn`).should(`be.enabled`)
    })
})

describe(`Visiting home page and then typing a letter then erasing it`, () => {
    it(`Error message is visible and submit button is disabled`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#sentence`).type("i")
        cy.get(`#sentence`).type('{selectall}{backspace}')

        cy.get(`#submit-btn`).should(`be.disabled`)
        cy.get(`#error-message`).should(`be.visible`)
    })
})


describe(`Visiting home page, then typing a letter and then clicking on the analyze button`, () => {
    it(`loading progress spinner is visible`, () => {
        cy.visit(`http://localhost:3000`)

        cy.get(`#sentence`).type("i");

        cy.get(`#submit-btn`).click()
        cy.get(`#progress`).should(`be.visible`)
    })
})