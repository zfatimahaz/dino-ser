import glob
import os
import pickle

import librosa
import numpy as np
import soundfile
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV


def extract_feature(file_name, mfcc=True, chroma=True, mel=True):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
            result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))
    return result


emotions = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}

observed_emotions = ['neutral', 'happy', 'sad', 'angry']


def load_data(test_size=0.2):
    x, y = [], []
    for file in glob.glob("ravdess data\Actor_*\*.wav"):
        file_name = os.path.basename(file)
        emotion = emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature = extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)


# this function used to find the best parameter for the model
# try to optimize the model and increase the accuracy
# this function need 20-30 minutes to run
# however, this function only need to run once
def findBestModel(clf, x, y):
    param_grid = [
        {
            'activation': ['identity', 'logistic', 'tanh', 'relu'],
            'learning_rate': ['constant', 'invscaling', 'adaptive'],
            'max_iter': [850, 875, 900],
            'hidden_layer_sizes': [400, 500, 600],
            'alpha': [0.001, 0.005, 0.01]
        }
    ]
    clf = GridSearchCV(clf, param_grid, cv=3, scoring='accuracy')
    clf.fit(x, y)
    print("Best parameters set found on development set:")
    print(clf.best_params_)


x_train, x_test, y_train, y_test = load_data(test_size=0.25)

model = MLPClassifier(alpha=0.001,
                      activation='tanh',
                      batch_size=256,
                      epsilon=1e-08,
                      hidden_layer_sizes=(500,),
                      learning_rate='adaptive',
                      max_iter=875)

# findBestModel(model, x_train, y_train)

# result of findTheBest function
# {'activation': 'tanh', 'hidden_layer_sizes': 400, 'learning_rate':
# 'adaptive', 'max_iter': 875} --> mean(78.57%, 78.57%, 76.79%, 77.38%, 77.38%) = 77.738‬%
# {'activation': 'tanh', 'alpha': 0.005, 'hidden_layer_sizes': 500,
# 'learning_rate': 'constant', 'max_iter': 875} --> mean(79.17 %, 76.19%, 76.79%, 77.38%, 75.60%) = 77.03%
# {'activation': 'tanh', 'alpha': 0.001, 'hidden_layer_sizes': 500, 'learning_rate': 'adaptive', 'max_iter': 875}
#       --> mean(78.57%, 76.19%, 76.19%, 80.95%, 79.17%) = 78.214%


model.fit(x_train, y_train)  # train data
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))
if accuracy > 0.8:
    pickle.dump(model, open("Speech_emotion_recognition.model", "wb"))
