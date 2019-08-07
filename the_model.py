from keras.layers.core import Dense, Activation, Dropout ,Flatten
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras import regularizers,optimizers
import time #helper libraries



def model(x,act,loss):
    print(x.shape[2] * 1.2)
    model = Sequential()
    print(round(x.shape[2] * 0.005))
    model.add(LSTM(
        #input_shape=(x.shape[-1],10),
        input_dim=x.shape[-1],
        #output_dim=round(x.shape[2] * 1.5),
        output_dim=round(x.shape[2] * 1.2),

        #output_dim=round(x.shape[2]*3),
        return_sequences= True))

    model.add(Dense(x.shape[2]))
    #model.add(Dropout(0.01 ))
    ###model.add(Dropout(0.3))

    ##### RM
    #model.add(Dropout(0.4))
    model.add(Activation(act))

    start = time.time()



    sgd = optimizers.SGD(lr=0.2, momentum=0.1)



    #sgd = optimizers.SGD(lr=0.1,  momentum=0.001)
    #ad=optimizers.Adam(lr=0.001, beta_1=0.99, beta_2=0.99, epsilon=None, decay=0.0, amsgrad=True)

    model.compile(loss=loss,optimizer=sgd)

    print('compilation time : {}'.format(time.time() - start))

    # model.fit(
    #     x,
    #     y,00001
    #     # batch_size=3028,
    #     nb_epoch=200,
    #     validation_split=0.1)

    return model