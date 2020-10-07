[![PyPI version](https://badge.fury.io/py/demisto-py.svg)](https://badge.fury.io/py/demisto-py)
[![CircleCI](https://circleci.com/gh/demisto/demisto-py/tree/master.svg?style=svg)](https://circleci.com/gh/demisto/demisto-py/tree/master)
# Demisto Client for Python

A Python library for the Demisto API.

Version 2.x is compatible with Demisto server version 4.5 and later.

**Note:** You are viewing the demisto-py 2.x development branch. demisto-py 1.x is officially deprecated (maintenance-mode only) and can be obtained at: https://github.com/demisto/demisto-py/releases.

## Demisto for Python Usage
This section covers the steps you need to take to get the client configured.

### 1. Get a Demisto API Key
Follow these instructions to generate your Demisto API Key.
1. In Demisto, navigate to **Settings > API Keys**.
2. Click the **Generate Your Key** button.

To avoid hard coding configurations in your code, it is possible to specify configruation params
as the following environment variables (env variables will be used if parameters are not specified):

 * DEMISTO_BASE_URL
 * DEMISTO_API_KEY
 * DEMISTO_USERNAME
 * DEMISTO_PASSWORD
 * DEMISTO_VERIFY_SSL (true/false. Default: true)
 * SSL_CERT_FILE (specify an alternate certificate bundle)

### 2. Create a Demisto client instance with the api-key and server-url:
```python
import demisto_client

# Also possible to set env variables: DEMISTO_API_KEY and DEMISTO_BASE_URL
api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key)

```

**Alternatively, you can login with username and password:**

```python
import demisto_client

# Also possible to set env variables: DEMISTO_USERNAME DEMISTO_PASSWORD and DEMISTO_BASE_URL
host = 'https://YOUR_DEMISTO_HOST'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

api_instance = demisto_client.configure(base_url=host, username=username, password=password)
```

### 3. Create incidents

```python
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException


api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()

create_incident_request.name = 'Sample Simulation Incident'
create_incident_request.type = 'Simulation'
create_incident_request.owner = 'Admin'

try:
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident: %s\n" % e)

```

Additional examples available in the [docs](docs/README.md) and under the [examples folder](examples/).

## API Documentation
API Documentation based upon the Demisto Server Swagger API is available [here](docs/README.md)

## Troubleshooting

### API Key
If when using an API key you encounter a response similar to the following:
```json
{"id":"forbidden","status":403,"title":"Forbidden","detail":"Issue with CSRF code","error":"http: named cookie not present","encrypted":false,"multires":null}
```
It means your API key is invalid. Make sure you are using a valid API key. You can check your API key by using curl with the following request:
```bash
  curl -i -k -H 'Authorization: YOUR_API_KEY'  https://your-demisto.server.url/about
```
For a valid API key you will receive a response similar to the following:
```
HTTP/1.1 200 OK
Strict-Transport-Security: max-age=10886400000000000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1; mode=block
Date: Thu, 04 Jun 2020 09:27:53 GMT
Content-Length: 189
Content-Type: text/plain; charset=utf-8

{"demistoVersion":"5.5.0", ...}
```

## Contributing
Contributions are welcome and appreciated. To contribute follow the instructions below and submit a PR. 

Before merging any PRs, we need all contributors to sign a contributor license agreement. By signing a contributor license agreement, we ensure that the community is free to use your contributions.

When you open a new pull request, a bot will evaluate whether you have signed the CLA. If required, the bot will comment on the pull request, including a link to accept the agreement. The CLA document is also available for review as a [PDF](https://github.com/demisto/content/blob/master/docs/cla.pdf).

If the `license/cla` status check remains on *Pending*, even though all contributors have accepted the CLA, you can recheck the CLA status by visiting the following link (replace **[PRID]** with the ID of your PR): https://cla-assistant.io/check/demisto/dockerfiles?pullRequest=[PRID] .


## Dev Environment Setup
We build for both python 2 and 3. We recommend installing both development environments. You can use pyenv to manage multiple python versions (see: https://github.com/pyenv/pyenv). We use [tox](https://github.com/tox-dev/tox) for managing environments and running unit tests.

Install `tox`:
```
pip install tox
```
List configured environments:
```
tox -l
```
Then setup dev virtual envs for both python 2 and 3 (will also install all necessary requirements):
```
tox --devenv venv2 --devenv py27
tox --devenv venv3 --devenv py37
```
Activate python 2 env by running:
```
. venv2/bin/activate
```
Switch to python 3 env by running:
```
. venv3/bin/activate
```

## Running Unit Tests
We use pytest to run unit tests. Inside a virtual env you can run unit test using:
```
python -m pytest -v
```
Additionally, our build uses tox to run on multiple envs. To use tox to run on all supported environments (py27, py36, py37), run:
```
tox -q  
```
To run on a specific environment, you can use:
```
tox -q -e py27
```

## Code Generation
Library code was generated using the Demisto Server 4.5.0 Swagger definition with modifications to support later Server versions.

**Important:** All code under [demisto_client/demisto_api](demisto_client/demisto_api) is generated using the swagger code generation tool. Do not modify this code directly.

We use a script to run the generate tool and then modify as needed. 
If you would like to contribute **DO NOT** modify the generated code directly, modify the script: [gen-code.sh](gen-code.sh) and then re-generate the code.

To generate the code run (requires bash, sed and docker):
```
./gen-code.sh
```

## License
Apache 2.0 - See [LICENSE](LICENSE) for more information.
