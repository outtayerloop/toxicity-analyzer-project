const THRESHOLD = 0.5

describe(`Basic threat input without punctuation then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I will kill you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I will kill you!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I will KILL you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with booster word then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I will kill you, slaughter you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with booster word and capitalization emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I will KILL you, SLAUGHTER you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Threatening without punctuation then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`i'mma kill u`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Threatening slang with punctuation emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`i'mma kill u!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Threatening slang with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I'MMA kill U!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with time notion without punctuation then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have always wanted to kill you, now I will`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with time notion with punctuation emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have always wanted to kill you, now I will!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic threat input with time notion with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I have ALWAYS WANTED to kill you, NOW I WILL!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified threat input without punctuation then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I kind of want to kill you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified threat input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I kind of want to kill you!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified threat input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I KIND OF want to kill you`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Threatening mixed negation input then clicking submit button`, () => {
    it(`Returns threat percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I want to hug you but I want to kill you at the same time`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Nice input then clicking submit button`, () => {
    it(`Returns threat percentage strictly lower than threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love everyone`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualThreatRate = parseFloat(response.body.content.threat)
            expect(actualThreatRate).to.be.lessThan(THRESHOLD)
        })
    })
})