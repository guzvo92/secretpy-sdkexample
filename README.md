# Secretpy SDK Example

## Background

Hoping to help some python developers to build on Secret Network there are an easy use of the secretpy SDK for cover some points that help to test a LCD connection (Light Client Daemon). In order to easily identify how to work with the network (use the "secretcli" for verify*) there are some code examples.

## This example covers the next points:
- ✅ How to connect through Secret Mainnet endpoints
- ✅ How to connect through Localsecret docker instance
- ✅ Create wallets
- ✅ Sending Coins through secret wallets

## Requirements:

-[0] try to start the project in a virtual environment:
```bash
pip install virtualenv
python3 -m venv aenv
aenv/bin/activate
```

-[1] https://github.com/secretanalytics/secret-sdk-python
```bash
pip install secret-sdk
```
At this time i am working with secret-sdk==1.7.1

-[2] For testing this code u should have a docker with localsecret instance running on your machine (if u are working on windows use Docker Desktop and the WSL2)
https://docs.docker.com/desktop/windows/wsl/#:~:text=Start%20Docker%20Desktop%20from%20the,option%20is%20enabled%20by%20default.

There are the docs of localsecret:
#https://docs.scrt.network/secret-network-documentation/development/tools-and-libraries/local-secret

```bash
docker run -it -p 9091:9091 -p 26657:26657 -p 1317:1317 -p 5000:5000 \
  --name localsecret ghcr.io/scrtlabs/localsecret
```

-[3] Install secretcli for testing purposes
https://docs.scrt.network/secret-network-documentation/development/tools-and-libraries/secret-cli/install

//config secretcli in bash to link to localsecret docker instance
```bash
secretcli config node http://localhost:26657
secretcli config chain-id secretdev-1
secretcli config keyring-backend test
secretcli config output json
```

//For check the node URL
```bash
secretcli status --node "$URL"
```

//quering founds
```bash
secretcli query bank balances "secret16rx0tlptqvyw4zvngpwxr4rquj3597jpsdjrzq"
```

## Ussage:
-Configure ur MNEMONICs to generate ur secretaddress
-First u should have coins in ur wallet 1 for transfer
(Localsecret has a faucet integrated on port 5000 where u target an secret address)
Run in bash the next url for claim coins:
```bash
curl http://localhost:5000/faucet?address=secret16rx0tlptqvyw4zvngpwxr4rquj3597jpsdjrzq 
```
#(where the secret address is builded from MNEMONIC1 on my example)


## Reporting Issues
Please use this repo to report any issues for the Secretpy SDK Example.
- [Guzvo92] (https://github.com/guzvo92)

## Features and improvements: (pull requests welcome):
- [ ] Loading...
