import sys
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def main():
    
    first_line = sys.stdin.readline().strip().split(' ')
    
    F, N = [int(i) for i in first_line]
    
    train = []
    test = []
     
    for i in range(N):
        line = sys.stdin.readline()
        dts = line.strip().split(' ')
        train.append([float(f) for f in dts])
        
    T = input()
    
    for i in range(int(T)):
        line = sys.stdin.readline()
        dts = line.strip().split(' ')
        test.append([float(f) for f in dts])
        
        
    train = np.mat(train)
    predict = np.mat(test)
    X = train[:,:F]
    y = train[:,F]

    
    poly = PolynomialFeatures(degree=9)
    X_ = poly.fit_transform(X)
    predict_ = poly.fit_transform(predict)
    lr = LinearRegression()

    lr.fit(X_,y)
    
    
    y_pred = lr.predict(predict_)
    for i in y_pred:
        print(i[0])

        
if __name__ == '__main__':
    main()
