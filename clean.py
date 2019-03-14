print("Running clean.py\n\t\tImporting Packages...",end="# ")
import pandas as pd
pd.set_option('max_colwidth',80)
#pd.set_option('max_columns',10)
import numpy as np
print(" Packages Imported")

print("\n\t\tImporting and Reading Data...",end="# ")
names=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']

#DataSet is very huge.Recommended using crop.xlsx
#data=pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx',names=names)
data=pd.read_excel('crop.xlsx',names=names)

print(" READ and IMPORT DONE\n")
#data.to_excel('crop.xlsx')

print("CLEANING DATA...")
print("\tCurrent Shape of Data : ",np.shape(data))
print("\n\tStriping Spaces from Descriptions...")#
data['Description'] = data['Description'].str.strip()
print("Current Shape :",np.shape(data))
print("\tRemoving Rows that dont have Invoice No or CustomerID...")#
data.dropna(axis=0, subset=['CustomerID'], inplace=True)
data.dropna(axis=0, subset=['Description'], inplace=True)
data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
print("Current Shape :",np.shape(data))
print("\tRemoving Rows that have Cancelled Transactions...")#
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('C')]  #C=Cancelled Transactions
data = data[~data['InvoiceNo'].str.contains('D')]  #D=Discount Transactions
print("\tRemoving WASTE Transactions...")
waste = ["WRONG","LOST", "CRUSHED", "SMASHED", "DAMAGED", "FOUND", "THROWN", "MISSING", "AWAY", "\\?",
              "CHECK", "POSTAGE", "MANUAL", "CHARGES", "DAMAGES", "FEE", "FAULT", "SALES", "ADJUST", "COUNTED",
              "LABEL","INCORRECT", "SOLD", "BROKEN", "BARCODE", "CRACKED", "RETURNED", "MAILOUT", "DELIVERY",
              "MIX UP", "MOULDY", "PUT ASIDE", "ERROR", "DESTROYED", "RUSTY"]
waste = '|'.join(waste)
data= data[-data['Description'].str.contains(waste)]
print("Current Shape :",np.shape(data))




print("  ##Cleaning DONE##")
print("Final Shape of Data : ",np.shape(data))
print("\n\t\tExiting clean.py\n")


