import pandas as pd  
import numpy as np     
import matplotlib.pyplot as plt 
data = pd.read_csv('data_classification.csv', header=None)
print(data.values)
true_x = []
true_y = []
false_x = []
false_y = []
for item in data.values:
    if item[2] == 1:
        true_x.append(item[0])   
        true_y.append(item[1])
    else :
        false_x.append(item[0])
        false_y.append(item[1])
plt.scatter(true_x, true_y, marker='o', c='b') # type: ignore
plt.scatter(false_x, false_y, marker='s', c='g') # type: ignore
#plt.show()

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))

def phan_chia(p):
    if p >= 0.5 :
        return 1
    
    else :
        return 0
    
def predict(features, weights ):
    z = np.dot(features, weights)
    return sigmoid(z)

def cost_function(features, labels, weights):
    """_summary_

    Args:
        features (_type_): _description_
        labels (_type_): _description_
        weights (_type_): _description_
    """
    n = len(labels)
    predictions = predict(features,weights)
    
    """
    predictions
    [0.6 b, 0.7, 0.4, 0.6]
    ma tran chuyển vị
    ma trận cột
    [[]0],
    [1],
    [0]]
    muoón nhân với ma trận hàng ta phải chuyển thành ma trận hàng mới có thể nhân với ma trận hảng
    """
    
    cost_class1 = -labels*np.log(predictions)
    cost_class2 = -(1 - labels)*np.log(1-predictions) 
    cost = cost_class1 + cost_class2
    return cost.sum()/n

def update_weight(features, labels, weights, learning_rate):
    """
    Args:
        features (_type_): (100*3)
        labels (_type_): (100*1)
        weights (_type_): (3*1)
        learning_rate (_type_): float
        return : new weight : float
    """
    n = len(labels)
    # giá trị dự đoán của các điểm 
    predictions = predict(features, weights)
    # giá trị độ dốc  
    gd = np.dot(features.T , (predict - labels) )
    # tính trung bình
    gd = gd/n
    gd = gd*learning_rate
    # update weight 
    weights = weights - gd 
    return weights
    
def train (features, labels, weights, learning_rate, iter):
    cost_hs = []
    for i in range(iter):
        weights = update_weight(features, labels, weights, learning_rate)
        cost = cost_function(features, labels, weights)
        cost_hs.append(cost)
    return weights, cost_hs
        