from clean import data,pd,np,names

print("Running pre.py\n")
print("The Data Has 8 Features along with an Index Column(1st Column) : ")
print(names)
row,columns=np.shape(data)
print("\nThe size of each Feature in the Data is : ",row)
d_allc=data.iloc[:,8:9]
d_allc=np.ravel(d_allc)
y=[];c=0;z=[];t=0;tar=0
while(t<row):
    i=d_allc[t]
    if i not in y:
        y.append(i)
        c=c+1
        z.append(1)
    elif i in y:
        index=y.index(i)
        tar=np.int(z[index])
        tar=tar+1
        z[index]=tar        
    t=t+1
print("The number of the countries are ",c)
print("\nThe Countries in the Data Set are : ",y)
print("The number of Country (samples-1) are       : ",z)
print("The number of the countries are ",c)


d_uk =(data[data['Country'] == "United Kingdom"]
          .pivot_table(index="CustomerID",
                       columns="Description",
                       values="Quantity",
                       aggfunc="sum",
                       fill_value=0))

    
print("\nThe shape of UK data is : ",np.shape(d_uk))
print("\n\tEncoding Units in Data...",end="# ")
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
uk_set = d_uk.applymap(encode_units)

try :
    uk_set.drop('POSTAGE', inplace=True, axis='columns')
except:
    print("\n\t\t##Dropped all Waste##")
d_uk= d_uk[(d_uk.T !=0).any()]
#print(d_uk)


def ruler():
    global uk_set;
    choose=str(input("\n\t\tUse Apriori to define RULES(FOR UK only) ?\nEnter [y/n]:   "))
    if choose=='y':
        from mlxtend.frequent_patterns import apriori
        from mlxtend.frequent_patterns import association_rules
        frequent_itemsets = apriori(uk_set, min_support=0.07, use_colnames=True)
        a_rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
        a_rules.to_excel('rules.xlsx')
        a_rules[(a_rules['lift'] >= 0.6) &
                (a_rules['confidence'] >= 0.8) ]
        print("\n\t\tALL The Rules are saved in 'rules.xlsx' file")
        print("\t\tThe Interpretation of the RULES are given in 'README.txt' file")
        rules=pd.DataFrame([a_rules.antecedents,a_rules.consequents,a_rules.support,a_rules.confidence]).transpose()
        print("##### SOME RULES : \n",rules.head(10))
    elif choose=='n':
        print("")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        ruler()
ruler()







## ## ### ##### #### #### #### ### #### # #### ### ## ### ## ## ### #### # ## ## ##
def train_test_split1(data,percent):
    print("\nRunning Train_Test_Split...\n")
    global row;
    test_size= int((percent/100)*row)
    train_size=row-test_size
    print("   The size of Training Data is : ",train_size)
    print("   The size of Test Data is     : ",test_size,)
    print("                          Total : ",(train_size+test_size))
    length=0
    rows_t=[]
    rows_s=[]
    print("\n\tRandomly Choosing Training Data...\n")
    train=pd.DataFrame(rows_t,columns=names)
    while(length<train_size):
        x1=np.random.choice(data['Sn'])
        
        if (((x1==train.Sn).any())==False):
            dict1=(data.iloc[x1-1:x1,:]).to_dict(orient='dict')
            rows_t.append(dict1)########
            length=length+1
            train=pd.DataFrame(rows_t,columns=names)
            #print(np.shape(train))
        else:
            print("",end="")
    length=0
    test=pd.DataFrame(rows_s,columns=names)
    print("\tRandomly Choosing Test Data...\n")
    while(length<test_size):
        x1=np.random.choice(data['Sn'])
        if (((x1==train.Sn).any())==False) and (((x1==test.Sn).any())==False):
             dict2=(data.iloc[x1-1:x1,:]).to_dict(orient='dict')
             rows_s.append(dict2)
             length=length+1
             test=pd.DataFrame(rows_s,columns=names)
    print("\t\tThe Training and Test Data ARE Split")
    return train,test
################################################################################  

inputs=d_uk.index.values.tolist()
inputs=np.asarray(inputs)
inputs=inputs.reshape(-1,1)
#print(type(inputs))
print("\n\t\t *INPUTS READY! SHAPE  : ",np.shape(inputs))
targets=d_uk.reset_index()
targets=targets.drop('CustomerID',axis=1)
print("\t\t*TARGETS READY! SHAPE  : ",np.shape(targets))




def choser():
    global inputs;global targets;
    choose=str(input("\n\t\tUse Built-IN Splitter(NOT READY!!) ?\nEnter [y/n]:   "))
    if choose=='y':
        print("\n##The Module is not Ready yet...")
        print("##Check the code of this module(train_test_split1) in : 'pre.py' \n")
        choser()
        percent=int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        percent=(percent/100)
        train,test=train_test_split1(data,percent)
        print("\nThe Training Data has shape :",np.shape(train))
        print("The Test Data has shape     :",np.shape(test))
        train[names]=train[names].replace({'{':''},regex=True)
        train[names]=train[names].replace({'}':''},regex=True)
        train.to_excel('hello.xlsx')
        #train[names]=train[names].replace({'':''},regex=True)
        x_train = pd.DataFrame([train.InvoiceNo,train.StockCode,train.Quantity]).transpose()
        x_test  = pd.DataFrame([test.InvoiceNo,test.StockCode,test.Quantity]).transpose()
        y_train = pd.DataFrame([train.Country]).transpose()
        y_test  = pd.DataFrame([test.Country]).transpose()
    elif choose=='n':
        percent=int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        from sklearn.model_selection import train_test_split
        print("\n\tRandomly Choosing Training and Test Data...\n")
        x_train,x_test,y_train,y_test=train_test_split(inputs,targets,test_size=percent,random_state=0)
        print("\t\tThe Training and Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        choser()
    return x_train,x_test,y_train,y_test

x_train,x_test,y_train,y_test=choser()


print("\n\t##Data PreProcessing Done.") 
print("\t\tExiting pre.py\n")


'''

target_n=np.ravel(target_n)
target=[]
t=0
print("\nData Organizing...")
while(t<974):
    i=target_n[t]
    if (i=='United Kingdom'):
        target.append(1)
    elif (i=='France'):
        target.append(2)
    elif(i=='Australia'):
        target.append(3)
    elif(i=='Netherlands'):
        target.append(3)
    else:
        target.append(4)
    t=t+1
         


X = data['InvoiceNo','StockCode','Quantity','UnitPrice']
Y = data.iloc[:, 7:8] 
print(Y)
'''
