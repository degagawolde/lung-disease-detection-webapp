import cv2
import numpy as np

import tensorflow as tf

class Explanation:
    def __init__(self) -> None:
        pass
    
    def get_img_array(self,img_path, size):
        # `img` is a PIL image of size 299x299
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=size)
        # `array` is a float32 Numpy array of shape (299, 299, 3)
        array = tf.keras.preprocessing.image.img_to_array(img)
        # We add a dimension to transform our array into a "batch"
        # of size (1, 299, 299, 3)
        array = np.expand_dims(array, axis=0)
        return array

    def explanation(self,imagepath):
        im = cv2.imread(imagepath)
        im = cv2.resize(im, (256,256), interpolation = cv2.INTER_AREA)
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.reshape(img,(1,256,256,3))
    
        heatmap_cam = make_cam_heatmap(img, model, 'out_relu')
        heatmap_gradcam = make_grad_cam_pp_heatmap(img, model, 'out_relu')
        save_and_display_gradcam(im, heatmap_gradcam,2*count-1,title='gradcam')