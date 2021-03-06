from keras.utils import np_utils

from config import *
from utility.cv_utils import *

from extractor import Extractor



def load_data(categories):
    if len(categories) in (0, 1):
        raise ValueError("Cannot classify %d class" % len(categories))
    data = []
    labels = []
    for label, category in enumerate(categories):
        files = glob.glob(os.path.join(category, '*'))
        print("%3d. Category %-50s  %-7d files" % (label, category, len(files)))
        for file in files:
            image = imread(file)
            image = cv2.resize(image, SIZE)
            if CHANNELS == 1:
                image = im2gray(image).reshape(*image.shape[:-1], 1)
            data.append(image)
            labels.append(label)
    X = np.array(data)
    y = np.array(labels)
    y = np_utils.to_categorical(y, len(categories))
    
    print('X.shape:', X.shape)
    print('y.shape:', y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_TRAIN_SPLIT)
    return X_train, X_test, y_train, y_test 
