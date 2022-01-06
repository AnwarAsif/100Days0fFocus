## Import dependencies
from solcx import compile_standard, install_solc
import json
from web3 import Web3

install_solc("0.6.0")

## Load Solidiy code / contract
with open('simple_storage.sol', 'r') as file:
    simple_storage = file.read()
    # print(simple_storage)

compile_sol = compile_standard(
    {
        'language': "Solidity",
        'sources': {'simple_storage.sol': {'content': simple_storage}},
        'settings': {
            'outputSelection': {
                '*': {
                    "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                }
            }
        },
    },
    solc_version="0.6.0"
)

## Save compiler file to JSON
with open('compiled_file.json', 'w') as file:
    json.dump(compile_sol, file)

## Load Bytecode
bytecode = compile_sol['contracts']['simple_storage.sol']['SimpleStorage']['evm']['bytecode']['object']
print(bytecode)
## Load ABI
abi = compile_sol['contracts']['simple_storage.sol']['SimpleStorage']['abi']

##
