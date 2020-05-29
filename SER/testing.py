import joblib
import numpy as np
from SER import extract_feature
from collections import Counter

model = joblib.load('Speech_emotion_recognition.model')


def most_frequent(List):
    result = Counter(List)
    return list(result.keys())[0]


def prediction(filename):
    feature = extract_feature(filename)
    y = [1] * 192
    y = np.reshape(y, (-1, 1))
    testFile = feature * y
    predict = model.predict(testFile)
    return most_frequent(predict)


print(prediction('testfile.wav'))
print(prediction('testfile2.wav'))