import pyqiwi

wallet = pyqiwi.Wallet(token='9404b0ca0ccf756829d3d972f5b0bb5c', number='79237481901')

print(wallet.balance())

