import librosa
import pandas as pd
import os
from keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.models import load_model
import numpy as np

model = load_model('weights1109_4.best.basic_cnn.hdf5')

featuresdf = pd.read_pickle("featuresdf.pkl")


from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical


def coughdetect(coughfile):
# Convert features and corresponding classification labels into numpy arrays
    X = np.array(featuresdf.feature.tolist())
    y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
    le = LabelEncoder()
    yy = to_categorical(le.fit_transform(y)) 


    max_pad_len = 1000
    num_rows = 40
    num_columns = 1000
    num_channels = 1

    def extract_features(file_name):
        try:
            audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
            mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            pad_width = max_pad_len - mfccs.shape[1]
            mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        except Exception as e:
            print("Error encountered while parsing file: ", file_name)
            return None
        return mfccs


    def print_prediction(file_name):
        prediction_feature = extract_features(file_name)
        prediction_feature = prediction_feature.reshape(1, num_rows, num_columns, num_channels)
    
        predicted_vector = model.predict_classes(prediction_feature)
        predicted_class = le.inverse_transform(predicted_vector)
#        print("The predicted class is:", predicted_class[0], '---','\n')
#        return predicted_class[0]
#        print(predicted_class[0])

        if (predicted_class[0]=="cough") :
            return 1
        else:
            return 0
#        return predicted_class[0]=="cough"
    
#        predicted_proba_vector = model.predict_proba(prediction_feature)
#        predicted_proba = predicted_proba_vector[0]
#        for i in range(len(predicted_proba)):
#            category = le.inverse_transform(np.array([i]))
#            print(category[0], "\t\t : ", format(predicted_proba[i], '.32f') )

    return print_prediction(coughfile)==1
