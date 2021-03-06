from keras.utils import np_utils

from config3d import *
from utility.cv_utils import *


def load_data(categories):
    if len(categories) in (0, 1):
        raise ValueError("Cannot classify %d class" % len(categories))
    data = []
    labels = []
    for label, category in enumerate(categories):
        files = glob.glob(os.path.join(category, '*'))
        print("%3d. Category %-50s  %-7d files" % (label, category, len(files)))
        for file in files:
            video = Video(file)
            frame_array = []
            for frame in video:
                if CHANNELS == 1:
                    frame = im2gray(frame).reshape(frame.shape[:-1], 1)
                frame_array.append(frame)
            frame_array = np.array(frame_array)
            data.append(frame_array)
            labels.append(label)
    if not EXTRACT:
    	X = np.array(data).transpose((0, 2, 3, 4, 1))
    	X = X.reshape((X.shape[0], *SIZE3D, DEPTH, CHANNELS))
    else:
        extractor=Extractor()	
	X=[]
        for frame_array in data:
     	    frame_array=extractor.extract(frame_array)
            X.append(frame_array)
        X=np.array(X)

    y = np.array(labels)
    y = np_utils.to_categorical(y, len(categories))

    if EXTRACT:
        
        
    print('X.shape:', X.shape)
    print('y.shape:', y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_TRAIN_SPLIT)
    return X_train, X_test, y_train, y_test 
