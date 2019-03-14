ONLINE RETAIL DATASET


####  Run 'main.py' ####

clean.py  = used for loading and cleaning of the data
pre.py    = used for preprocessing along with train and test split.Also used to know more about data and Apply association rules
main.py   = used for training and testing of the split data



**The dataset available is very huge and not available in csv but excel format.
  So I would recommend using the provided crop.xlsx file for data input.
DATASET LINK  : https://archive.ics.uci.edu/ml/machine-learning-databases/00352/

**WARNING: The training and prediction using the actual data takes a huge toll on the 
           device memory resulting a serious performance hit with SUDDEN SHUTDOWNS due to performance tool.
           So I would recommend using the provided crop.xlsx file for data input.


** Features of data : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country 
     (8 in TOTAL)



** In the project,Apriori function is used to extract frequent itemsets for association rule mining.
   This gave us some rules on customer behaviours.

####RULES(example)### The Interpretation of the RULES is given Below:

   antecedents	                     consequents      antecedent support   consequent support     support      confidence     lift	    leverage	 conviction	
1.LOVE BUILDING BLOCK WORD    HOME BUILDING BLOCK WORD	   0.093023256	    0.093023256        0.093023256	   1	     10.75	   0.08436993	   inf
2.JAM MAKING SET PRINTED      JAM MAKING SET WITH JARS	   0.209302326	    0.139534884        0.093023256    0.444444444   3.185185185	   0.06381828	 1.548837209
3.JAM MAKING SET WITH JARS    JAM MAKING SET PRINTED	   0.139534884	    0.209302326        0.093023256    0.666666667   3.185185185	   0.06381828	 2.372093023
4.PACK OF 72 RETROSPOT CAKE   PACK OF 60 PINK PAISLEY CAKE   0.139534884    0.11627907	       0.093023256    0.666666667   5.733333333	   0.076798269   2.651162791


1.This indicates that there is almost full certainty that the customer who purchases 1st item will also purchase the 2nd item.(confidence)

2.This indicates that there is almost 44 percent certainty that the customer who purchases 1st item will also purchase the 2nd item.(confidence)
...
