from create_emb import Create_emb
from rnn_algo import rnn_algo_class
from check_res import anomaly_detection
import pickle
from params import Date_format
import numpy as np
# Project name can be: Enron400,Enron800,Twitter,RealityMining
project_name="Enron400"
graph_path="enron400_graph.pkl"


# Create the emb
# The function input is graph_path,proj_name,type of emb,rd,moment
# Currently the type of emb is hope. Moment is 2 or 3
emb=Create_emb(graph_path,proj_name=project_name)
emb.emb()

# RNN
file_name=emb.get_name_file()
train=30
try:
    open("res_"+str(file_name)+".p","r")
except:
    rnn=rnn_algo_class(project_name,"emb_"+str(file_name)+".pkl",str(file_name),train=train)
    rnn.rnn_algo()

s=Date_format(project_name)

data= pickle.load(open("res_"+str(file_name)+".p","rb"))
data=np.asarray(data)
data=np.reshape(data,(data.shape[0],data.shape[2]))
times=emb.get_dates()
times=times[train:len(times)]
s.create_anim_indx(times)
anom=anomaly_detection(data,project_name,s,"Isolation Forest")
anom.calculate_anom()