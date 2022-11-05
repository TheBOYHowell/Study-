#Asian currency to USD and some Crypto!

CN=int(input('What do you have left in yuan? '))
JP=int(input('What do you have left in yen? '))
KR=int(input('What do you have left in won? '))

#CONVERSION 
USD_sold= (CN * 0.14)+ (JP * 0.0068) +(KR * 0.00071)
BT_sold=(USD_sold * 0.000049)
ETH_sold=(USD_sold * 0.00063)
BNB_sold=(USD_sold * 0.0031)
XRP_sold=(USD_sold * 2.17)
DG_sold=(USD_sold * 6.56)
print('your sold in USD')
print(USD_sold)
#CRYPTO SIDE 
print("--------------- Value of the market 1 064 827 637 635,00 USD   IN 01/11/2022 ---------------")
print('your sold in Bitcoin')
print(BT_sold)
print('your sold in Ethereum')
print(ETH_sold)
print('your sold in BNB')
print(BNB_sold)
print('your sold in XRP')
print(XRP_sold)
print('your sold in Dogecoin')
print(DG_sold)

#end