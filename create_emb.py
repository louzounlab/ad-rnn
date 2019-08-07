import pickle
from gem.embedding.hope     import HOPE
import networkx as nx
import numpy as np
import time
from params import Date_format

class Create_emb:
    def __init__(self,graph_path,proj_name,type_emb="hope",r_d=20,moment=2):


        self.type_emb=type_emb
        self.r_d=r_d
        self.graph=pickle.load(open(graph_path,"rb"))
        self.proj_name=proj_name
        self.moment=moment
        self.create_format()
        self.create_keys()
        self.create_name()

    def create_format(self):
        form=Date_format(self.proj_name)
        self.format=form.get_data_form()

    def create_keys(self):
        keys = list(self.graph.keys())
        keys.sort(key=lambda x: time.mktime(time.strptime(x, self.format)))
        self.keys=keys

    def get_dates(self):
        return self.keys

    def create_name(self):
        self.name=str(self.proj_name)+"_"+str(self.type_emb)+"_"+\
                  str(self.r_d)+"_"+str(self.moment)

    def get_name_file(self):
        return self.name

    def emb(self):
        try:
            open("emb_"+self.name+".pkl")
            return


        except:
            res=[]

            for key in self.keys:
                g = self.graph[key]

                s = nx.from_dict_of_dicts(g._adj)
                if self.type_emb=="hope":
                    embedding = HOPE(d=self.r_d, beta=0.01)
                else:
                    print("Wrong type!!!")
                    return
                Y, t = embedding.learn_embedding(graph=s, edge_f=None, is_weighted=True, no_python=True)
                Y = np.asmatrix(Y)
                x = Y.T
                f = x * Y
                x=f
                if self.moment==3:
                    x = f*f

                x = np.asarray(x)
                x = x.reshape(x.size, 1)
                res.append(x)
            pickle.dump(res, open("emb_"+str(self.name)+".pkl", "wb"))



# emb=Create_emb("/home/polina/PycharmProjects/Multi_graphs/enron400_graph.pkl","try")
# emb.emb()