import numpy as np

def load_data():
    data = np.loadtxt("/home/amitk/my_web/Machine-Learning-Andrew-Ng/source/source_files/Supervised_Machine_Learning_Regression_and_Classification/week2/C1W2A1/data/ex1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("/home/amitk/my_web/Machine-Learning-Andrew-Ng/source/source_files/Supervised_Machine_Learning_Regression_and_Classification/week2/C1W2A1/data/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
