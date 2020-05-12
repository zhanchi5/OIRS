### Нейронная сеть распознает на изображении Кота или Собаку

Осознать, что происходит под катом, помогли статьи: 
* [Статья1](https://www.reg.ru/blog/keras/)
* [Статья2](https://medium.com/datathings/dense-layers-explained-in-a-simple-way-62fe1db0ed75)

### Что было использовано?
OpenCV

Keras

Для обучения был использован набор изображений с сайта [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data)

#
### Изображения для распознавания находятся в ImagesToPredict

### Как это использовать?

```bash
	python3 Predict.py ImagesToPredict/<imageName>
```

### Что использовалось в модели из изученных функций?
* Conv2D
* MaxPooling2D

### Что использовалось нового?
* Flatten
* Dense
* EarlyStopping - используется для чтобы избежать переобучения, при обучении итеративным методом

В качестве функции активации используется так называемая [ReLU "выпрямитель"](http://datareview.info/article/eto-nuzhno-znat-klyuchevyie-rekomendatsii-po-glubokomu-obucheniyu-chast-2/)

### Как выглядит модель
	Conv2D
	   | 
	   v
	MaxPooling2D
	   |
	   v
	Conv2D
	   |
	   v
	Flatten
	   |
	   v
	Dense
	   |
	   v
	Dense