import numpy as np 
import pandas as pd 
from sklearn.impute import SimpleImputer 

'''data = pd.read_csv('dt.csv', header = None)
print(data)
X = data.values
imp = SimpleImputer(missing_values=np.nan , strategy='most_frequent')
imp.fit(X)
result = imp.transform(X)
print(result)

'''
'''
df = pd.DataFrame(
    [(1, 2, 1),
     (0, 3, 0),
     (2, 0, 4),
     (1, 1, 1),], columns=['dog', 'cat', 'bear']
)
cd = df.cov() # sự tương quan giữa các thuộc tính 
print(cd)

'''

