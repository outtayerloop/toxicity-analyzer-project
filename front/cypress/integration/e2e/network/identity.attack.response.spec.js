const THRESHOLD = 0.5

describe(`Basic identity attack input without punctuation then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews suck!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You ARABIC JEWS suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with booster word then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`All of you arabic jews suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with booster word and capitalization emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`ALL OF YOU arabic jews suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Identity attack slang without punctuation then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`Y'all arabic jews suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Identity attack slang with punctuation emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`Y'all arabic jews suck!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Identity attack slang with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`Y'ALL arabic jews suck!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with time notion without punctuation then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews have always sucked`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with time notion with punctuation emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews have always sucked!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic identity attack input with time notion with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews HAVE ALWAYS sucked!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified identity attack input without punctuation then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews kind of suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified identity attack input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews kind of suck!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified identity attack input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`You arabic jews KIND OF suck!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Identity attack mixed negation input then clicking submit button`, () => {
    it(`Returns identity attack percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I'm not a discriminator but all of you arabic jews suck`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Nice input then clicking submit button`, () => {
    it(`Returns identity attack percentage strictly lower than threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love everyone`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualIdentityAttackRate = parseFloat(response.body.content.identity_attack)
            expect(actualIdentityAttackRate).to.be.lessThan(THRESHOLD)
        })
    })
})