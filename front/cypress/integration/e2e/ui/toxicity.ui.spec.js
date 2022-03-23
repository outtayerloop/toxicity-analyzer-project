// Threshold is here considered to be equal to 50 %

describe(`Basic toxic input without punctuation then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I hate everything`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I hate everything!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I HATE everything`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with booster word then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I really hate you, despise you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with booster word and capitalization emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I REALLY hate you, DESPISE you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Toxic slang without punctuation then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`u mad`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Toxic slang with punctuation emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`u mad!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Toxic slang with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`U MAD!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with time notion without punctuation then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have always hated you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with time notion with punctuation emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have always hated you!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Basic toxic input with time notion with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have ALWAYS HATED YOU!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified toxic input without punctuation then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I kind of hate you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified toxic input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I kind of hate you!`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Qualified toxic input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I KIND OF hate you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Toxic mixed negation input then clicking submit button`, () => {
    it(`Returns toxicity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love chocolate a lot, but it sucks being here with you`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s(([5-9][0-9][.][0-9][0-9])|(100.00))\s[%]/)
        })
    })
})

describe(`Nice input then clicking submit button`, () => {
    it(`Returns toxicity percentage strictly lower than threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love everyone`)
        cy.wait(`@submission`).should(({ request, response }) => {
            cy.get(`li:nth-child(6)`)
                .invoke(`text`)
                .should(`match`, /Toxicity\s[:]\s[1-4]?[0-9][.][0-9][0-9]\s[%]/)
        })
    })
})