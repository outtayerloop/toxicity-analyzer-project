const THRESHOLD = 0.5

describe(`Basic obscene input without punctuation then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`My d*** in your a**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`My d*** in your a**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`My D*** in your A**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with booster word then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`my d*** in your a** sweating hard`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with booster word and capitalization emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`my d*** in your a** SWEATING hard`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Obscene slang without punctuation then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`my d*** in ur a**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Obscene slang with punctuation emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`my d*** in ur a**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Obscene slang with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`my d*** in UR a**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with time notion without punctuation then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's always been a sl**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with time notion with punctuation emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's always been a sl**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Basic obscene input with time notion with punctuation and capitalization emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's ALWAYS BEEN a sl**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified obscene input without punctuation then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's at least kind of a sl**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified obscene input with punctuation emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's at least kind of a sl**!`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Qualified obscene input with capitalization emphasis then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`She's at least KIND OF a sl**`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Obscene mixed negation input then clicking submit button`, () => {
    it(`Returns obscenity percentage equal or above threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love her a lot but, but she's such a sl** omg`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.gte(THRESHOLD)
        })
    })
})

describe(`Nice input then clicking submit button`, () => {
    it(`Returns obscenity percentage strictly lower than threshold`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitInput(`I love everyone`)
        cy.wait('@submission').should(({ request, response }) => {
            const actualObscenity = parseFloat(response.body.content.obscene)
            expect(actualObscenity).to.be.lessThan(THRESHOLD)
        })
    })
})