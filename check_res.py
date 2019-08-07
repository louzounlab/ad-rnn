

from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn import mixture
import random
from params import Date_format

class anomaly_detection:
    def __init__(self,data,proj,data_format,anom_type):
        self.proj=proj
        self.data=data
        self.len= len(data)
        self.data_format=data_format
        self.anom_type=anom_type
        self.set_anom()

    def set_anom(self):
        data=self.data_format
        ground_t=data.get_grond_truth()
        self.num_anom=len(ground_t)
        self.anom=data.get_anom_indx()

    def isolation_forest(self):
        clf = IsolationForest( max_samples=self.len,bootstrap=True,n_estimators=200)
        clf.fit(self.data)
        y=clf.decision_function(self.data)

        return y


    def local_outlier_factor(self):
        l = LocalOutlierFactor()
        l.fit(self.data)
        y=l._decision_function(self.data)

        return y


    def SVM(self):
        l = OneClassSVM(kernel="rbf",gamma=0.2
                           ,nu=0.168)
        l.fit(self.data)
        y = l.decision_function(self.data)

        return y

    def choose_best(self,y):
        t = []
        for i in range(len(y)):
            t.append([y[i], i])
        s = sorted(t)
        x = list(range(len(y)))

        anoms = []
        for i in range(self.num_anom*2):
            if y[i] < self.delta:
                anoms.append(i)
        return anoms


    def calculate_anom(self):
        if self.anom_type =="Isolation Forest":
            scores=self.isolation_forest()
        elif self.anom_type =="SVM":
            scores = self.SVM()
        elif self.anom_type == "local_outlier_factor":
            scores = self.local_outlier_factor()
        else:
            print( "WORNG ALGO TYPE")
            return

        anom=self.choose_best(scores)

        res=self.calculate_res(anom)
        return res

    def calculate_res(self,anom):
        sum=0
        for i in anom:
            if i in self.data_format.indx:
                sum+=1
        return sum


