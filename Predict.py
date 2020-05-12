import keras
import cv2
import numpy as np

class Predict:

    def __init__(self, path, file):

        self.path = path
        self.file = file

    def load_model(self):
        '''
        Загрузка модели
        '''
        self.loaded_model = keras.models.load_model(self.path)
        return self.loaded_model

    def makepredictions(self):
        '''
        Обработка файлов и предсказания
        '''

        img = cv2.imread(self.file)
        img = cv2.resize(img, (64, 64))
        img = np.reshape(img, [1, 64, 64, 3])
        print("File loaded and reshaped. The new shape is ", img.shape)
        print("Start predicting...")
        predictions = self.loaded_model.predict_classes(img)

        # Переработка вывода в удобный для человека вид

        if predictions == 0:
            predictions = 'Cat'
        elif predictions == 1:
            predictions = 'Dog'

        print("Prediction completed: this is a", predictions)

# `PATH` путь до модели `DogCat.h5`
# `FILE` Изображение для распознавания

pred = Predict(
    path='/home/zhanchi/Documents/Лекции/ОИРС/sems/sem4/dz/DogCat.h5',
    file='/home/zhanchi/Documents/Лекции/ОИРС/sems/sem4/dz/ImageToPredict/cat_to_guess.jpeg')

pred.load_model()
pred.makepredictions()
