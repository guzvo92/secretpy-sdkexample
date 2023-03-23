from secret_sdk.client.lcd import LCDClient
from secret_sdk.key.mnemonic import MnemonicKey
from secret_sdk.core.bank import MsgSend
from secret_sdk.core.tx import StdFee


#Aleatory 24words produce an secretaddress 
MNEMONIC1="hope issue elevator spin grace marine future world able crash arctic theme mean various roof wage bomb ridge hunt dwarf elephant suspect fiber nasty"
MNEMONIC2="hope issue elevator spin grace marine future world able crash arctic theme mean various roof wage bomb ridge hunt dwarf elephant suspect fiber new"


'''Mainnet conection'''
#https://docs.scrt.network/secret-network-documentation/development/connecting-to-the-network/mainnet-secret-4#binaries
#secret_mainnet = LCDClient(chain_id="secret-4", url="https://lcd.secret.express")

'''Docker Localsecret conection'''
#In the docs says that the LCD docker localsecret has is the port1317
# https://docs.scrt.network/secret-network-documentation/development/tools-and-libraries/local-secret
secret_localdocker = LCDClient(chain_id="secretdev-1", url="http://localhost:1317")
print(secret_localdocker.tendermint.block_info()['block']['header']['height'])


#Create a wallet 
wallet1 = secret_localdocker.wallet(MnemonicKey(mnemonic=MNEMONIC1))
wallet2 = secret_localdocker.wallet(MnemonicKey(mnemonic=MNEMONIC2))
print("W1 ",wallet1.key.acc_address)
print("W2 ",wallet2.key.acc_address)

#Print individual balances
print("W1 ",wallet1.lcd.bank.balance(wallet1.key.acc_address))
print("W2 ",wallet2.lcd.bank.balance(wallet2.key.acc_address))

#------------------------------------------------------------------------------------
'''[1] SEND COINS '''
def custom_sendcoins(fromwallet,destinationwallet,amount):
    print("[Making TX]-------------------")
    send_msg = MsgSend(
                fromwallet.key.acc_address,
                destinationwallet.key.acc_address,
                amount)    # send 1 scrt
            
    tx = fromwallet.create_and_broadcast_tx(
        [send_msg],
        memo="My first transaction!",
        gas = fromwallet.lcd.custom_fees["send"].gas_limit)
    
custom_sendcoins(wallet1,wallet2,"5000000uscrt")

'''[2] SEND COINS '''
#Compressed method to send coins: 
#tx = wallet1.send_tokens(recipient_addr=wallet2.key.acc_address, transfer_amount="1000000uscrt")

#Re-check balances
print("W1 ",wallet1.lcd.bank.balance(wallet1.key.acc_address))
print("W2 ",wallet2.lcd.bank.balance(wallet2.key.acc_address))



















