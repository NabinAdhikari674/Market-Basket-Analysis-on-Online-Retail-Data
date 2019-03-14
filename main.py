#The default dataset used is Offline because
#the dataset is very huge and it is available in excel format and not csv
#due to which the entire dataset needs to be downloaded which takes like forever if you have slow internet connection

#To change this go to 'clean.py'

from pre import x_train,x_test,y_train,y_test,np,pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
#from sklearn.metrics import accuracy_score

   


print("\n##Running main.py\n")

print("\n\tTraining Data Using DecisionTreeClassifier...\n")
pred=DecisionTreeClassifier(criterion='entropy',max_depth=6,random_state=0)
pred.fit(x_train,y_train)
print("\t\tThe Training is DONE")
predictions=pred.predict(x_test)
print(predictions)
print("\nThe Misclassified Samples per Descriptions are : \n",np.sum(np.not_equal(y_test, predictions)))
#accuracy=accuracy_score(predictions,y_test)
pp,zz=np.shape(predictions)
aa,yy=np.shape(y_test)
print("PRED Shape ",np.shape(predictions))
print("ACTUAL SHAPE ",np.shape(y_test))
q=np.random.randint(0,(pp-1))
print(q)
print("\n\nMoving on to Graphical Representation with a RANDOM sample...")

print(predictions[q:q+1,:])
y_test=y_test.values.tolist()
y_test=np.asarray(y_test)
print((y_test[q:q+1,:]))

plt.xlabel('Probability That Item can be Purchased')
plt.ylabel('PROBABILITIES')
plt.plot((predictions[q:q+1 ,:]),c='b',label="GoldTest")
plt.plot(y_test[q:q+1,:],c='r',label="Predicted")
#plt.legend(loc='upper left')
plt.show()



print("\n\tDONE\n\tExiting main.py\n")


