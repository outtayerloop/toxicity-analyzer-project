describe(`Max input length then clicking submit button`, () => {
    it(`Returns 200 OK response`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitMaxLengthInput()
        cy.wait('@submission').should(({ request, response }) => {
            const actualStatusCode = response.statusCode
            expect(actualStatusCode).to.equal(200)
        })
    })
    it(`Returns expected response object structure`, () => {
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitMaxLengthInput()
        cy.wait('@submission').should(({ request, response }) => {
            const actualResponseBody = response.body
            expect(actualResponseBody).to.have.property(`message`)
            expect(actualResponseBody).to.have.property(`content`)
            const actualResponseContent = actualResponseBody.content
            expect(actualResponseContent).to.have.property(`identity_attack`)
            expect(actualResponseContent).to.have.property(`insult`)
            expect(actualResponseContent).to.have.property(`obscene`)
            expect(actualResponseContent).to.have.property(`severe_toxicity`)
            expect(actualResponseContent).to.have.property(`threat`)
            expect(actualResponseContent).to.have.property(`toxicity`)
        })
    })
    it(`Returns the expected headers`, () => {
        const apiEndpoint = `http://localhost:3000`
        cy.intercept(`POST`, `**/analyzer`).as(`submission`)
        cy.submitMaxLengthInput()
        cy.wait('@submission').should(({ request, response }) => {
            const actualHeaders = response.headers
            expect(actualHeaders).to.have.property(`content-type`)
            expect(actualHeaders[`content-type`]).to.equal(`application/json`)
            expect(actualHeaders).to.have.property(`access-control-allow-headers`)
            expect(actualHeaders[`access-control-allow-headers`]).to.equal(`Content-Type`)
            expect(actualHeaders).to.have.property(`access-control-allow-methods`)
            expect(actualHeaders[`access-control-allow-methods`]).to.equal(`GET,POST`)
            expect(actualHeaders).to.have.property(`access-control-allow-origin`)
            expect(actualHeaders[`access-control-allow-origin`]).to.equal(apiEndpoint)
        })
    })
})