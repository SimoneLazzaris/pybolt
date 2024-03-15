# pybolt

Simple modern python library for accessing secrets stored in passbolt

## Rationale

I needed a simple way to access credentials stored in passbolt; I've found only obsolete
packages and decided to write a quick one.

## Usage

You need:
- a working passbolt server (let's say at `https://mypassbolt.domain.example`)
- a set of credentials for that server:
  - an ascii-armored private key (e.g. in file `myprivatekey.asc`)
  - the passphrase for that key (e.g. `mysecretpassphrase`)
- the uuid of a secret you want to know

Then you can just import pybolt and use it like this:

```python
import pybolt

url="https://mypassbolt.domain.example"
passphrase="mysecretpassphrase"
private_key="myprivatekey.asc"
secret_uuid='31d79219-86e8-4cbf-b5ac-0b49f7aefa7b'

b = pybolt.Bolt(url, private_key, passphrase)
b.verify()
b.login()
secret = b.get_secret(secret_uuid)
print(f"PASSWORD: '{secret['password']}'")
```
## Installation

Easy:
```sh
pip install pybolt
```
