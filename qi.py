import pyqiwi

wallet = pyqiwi.Wallet(token='11', number='111')

print(wallet.balance())

