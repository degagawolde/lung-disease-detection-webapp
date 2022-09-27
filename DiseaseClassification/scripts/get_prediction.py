import tensorflow as tf
from tensorflow.keras.layers import Input,Dense
from tensorflow.keras.layers import GlobalAveragePooling2D

class GetPrediction:
    def __init__(self) -> None:
        pass
    
    def build_model(self,input_shape):
        inputs = Input(shape=input_shape, name="input_image")
        mobilenetv2 = tf.keras.applications.MobileNetV2(
            input_tensor = inputs, 
            weights="imagenet", include_top=False, alpha=0.35)
        
        x = mobilenetv2.get_layer('out_relu').output
        x = GlobalAveragePooling2D(name='gap')(x)
        output = Dense(3,activation='softmax')(x)
        return tf.keras.Model(inputs,output)
    
    def load_model(self,weight_path):
        model = self.build_model(input_shape=(256,256,3))
        model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate=0.001),
                                loss='binary_crossentropy',
                                metrics=['accuracy'])
        model.load_weights(weight_path)
        return  model
