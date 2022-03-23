// Threshold is here considered to be equal to 50 %

describe(`Basic insult input without punctuation then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You motherf*****`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You motherf*****!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You MOTHERF*****`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with booster word then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You motherf*****, son of a b****`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with booster word and capitalization emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You MOTHERF*****, SON of a B****`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Insult slang without punctuation then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`If you breath, you a thooot`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Insult slang with punctuation emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`If you breath, you a thooot!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Insult slang with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`If you breath, you a THOOOT!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with time notion without punctuation then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You've always been a son of a b****`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with time notion with punctuation emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You've always been a son of a b****!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic insult input with time notion with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You've always been a SON of a B****!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified insult input without punctuation then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You're kind of an a**hole`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified insult input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You're kind of an a**hole!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified insult input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You're KIND OF an a**hole`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Insult mixed negation input then clicking submit button`, () => {
    it(`Returns insult percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love chocolate a lot, but you're the biggest dumb*** i've ever met`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Nice input then clicking submit button`, () => {
    it(`Returns insult percentage strictly lower than threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love everyone`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(2)`)
                .invoke(`text`)
                .should(`match`, /Insult\s[:]\s[1-4]?[0-9][.][0-9][0-9]\s[%]/)
        })
    })
})