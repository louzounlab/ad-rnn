from keras.layers.core import Dense, Activation, Dropout ,Flatten
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import time #helper libraries
import numpy as np
from keras.models import model_from_json
import sys
from sklearn import preprocessing
from scipy.spatial import distance
import pickle
from the_model import model
import scipy


class rnn_algo_class:
    def __init__(self,name_proj,dataset,name_file,activation_f="sigmoid",loss="mean_squared_error",train=10,
               ep=8000,ep_train=1500):
        self.data_n=np.asarray(pickle.load(open(""+dataset+"","rb")))
        self.activation_f=activation_f
        self.loss=loss
        self.train=train
        self.ep=ep
        self.ep_train=ep_train
        self.name_proj=name_proj
        self.name_file=name_file

    def rnn_algo(self):
        res = []
        f = []
        X = np.asarray(self.data_n[0:self.train])
        y_train = self.data_n[0:self.train]
        X = np.reshape(X, (X.shape[0], 1, X.shape[1]))
        y_train = np.reshape(y_train, (y_train.shape[0], 1, y_train.shape[1]))
        loaded_model = model(X, self.activation_f, self.loss)
        h = loaded_model.fit(X, y_train, nb_epoch=self.ep)
        for i in range(self.train, self.data_n.shape[0]):
            next = self.data_n[i:i + 1]
            next_s = next

            next_s = np.reshape(next_s, (next_s.shape[0], 1, next_s.shape[1]))

            s = loaded_model.predict(next_s)
            s = np.reshape(s, (s.shape[0], s.shape[2]))

            next = np.reshape(next, (next.shape[0], 1, next.shape[1]))
            res.append(s)
            h = loaded_model.fit(next_s, next, nb_epoch=self.ep_train)
            t = h.history
            f.append((t["loss"][-1]))

        pickle.dump(f, open(str(self.name_file) + "loss" + ".p", "wb"))

        pickle.dump(res, open("res_" + str(self.name_file) + ".p", "wb"))



# rnn=rnn_algo_class("try","/home/polina/PycharmProjects/rnn_emb/emb_try.pkl")
# rnn.rnn_algo()

