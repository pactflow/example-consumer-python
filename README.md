# Example Consumer

[![Build Status](https://travis-ci.com/pactflow/example-consumer-python.svg?branch=master)](https://travis-ci.com/pactflow/example-consumer-python)

[![Pact Status](https://test.pactflow.io/pacts/provider/pactflow-example-provider-python/consumer/pactflow-example-consumer-python/latest/badge.svg?label=provider)](https://test.pactflow.io/pacts/provider/pactflow-example-provider-python/consumer/pactflow-example-consumer-python/latest) (latest pact)

[![Pact Status](https://test.pactflow.io/matrix/provider/pactflow-example-provider-python/latest/prod/consumer/pactflow-example-consumer-python/latest/prod/badge.svg?label=provider)](https://test.pactflow.io/pacts/provider/pactflow-example-provider-python/consumer/pactflow-example-consumer-python/latest/prod) (prod/prod pact)

This is an example of a Python consumer using Pact to create a consumer driven contract, and sharing it via [Pactflow](https://pactflow.io).

It is using a public tenant on Pactflow, which you can access [here](https://test.pactflow.io) using the credentials `dXfltyFMgNOFZAxr8io9wJ37iUpY42M`/`O5AIZWxelWbLvqMd8PkAVycBJh2Psyg1`. The latest version of the Example Consumer/Example Provider pact is published [here](https://test.pactflow.io/pacts/provider/pactflow-example-provider-python/consumer/pactflow-example-consumer-python/latest).

The project uses a Makefile to simulate a very simple build pipeline with two stages - test and deploy.

* Test
  * Run tests (including the pact tests that generate the contract)
  * Publish pacts, tagging the consumer version with the name of the current branch
  * Check if we are safe to deploy to prod (ie. has the pact content been successfully verified)
* Deploy (only from master)
  * Deploy app (just pretend for the purposes of this example!)
  * Tag the deployed consumer version as 'prod'

## Usage

See the [Pactflow CI/CD Workshop](https://github.com/pactflow/ci-cd-workshop).

To run the tests locally, run:

```
make test
```

To run the "fake ci" task:
```
export PACT_BROKER_BASE_URL=https://test.pactflow.io
export PACT_BROKER_USERNAME=dXfltyFMgNOFZAxr8io9wJ37iUpY42M
export PACT_BROKER_PASSWORD=O5AIZWxelWbLvqMd8PkAVycBJh2Psyg1
make fake_ci
```