import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K

def make_cam_heatmap(img_array, model, layer_name, cam_path="cam.jpg"):

    #Get the 128 input weights to the softmax.
    class_weights = model.layers[-1].get_weights()[0]

    get_output = K.function(
        [model.input],
        [model.get_layer(layer_name).output, model.output])

    [conv_outputs, predictions] = get_output([img_array])
    conv_outputs = conv_outputs[0, :, :, :]

    #Create the class activation map.
    cam = np.zeros(dtype=np.float32, shape=conv_outputs.shape[0:2])

    for i, w in enumerate(class_weights[:, 0]):
            cam += w * conv_outputs[:, :, i]

    cam = tf.maximum(cam, 0) / tf.math.reduce_max(cam)

    return cam.numpy()

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    # First, we create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

        # This is the gradient of the output neuron (top predicted or chosen)
        # with regard to the output feature map of the last conv layer
        grads = tape.gradient(class_channel, last_conv_layer_output)
        grads = tf.keras.layers.ReLU()(grads)
      
        grads=grads[0,:,:,:]

    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    # then sum all the channels to obtain the heatmap class activation
    last_conv_layer_output = last_conv_layer_output[0]
#     heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.math.multiply(last_conv_layer_output,grads)
    heatmap = tf.reduce_sum(heatmap,axis=-1)
   
    heatmap = tf.squeeze(heatmap)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def make_grad_cam_pp_heatmap(img_array, model, layer_name, pred_index=None):
    
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(layer_name).output, model.output]
    )

    with tf.GradientTape() as tape1:
        with tf.GradientTape() as tape2:
            with tf.GradientTape() as tape3:
                last_conv_layer_output, preds = grad_model(img_array)
                if pred_index is None:
                    pred_index = tf.argmax(preds[0])
                class_channel = preds[:, pred_index]
                
                #derivation of the given layer with respect to the output clas
                grads_1 = tape3.gradient(class_channel, last_conv_layer_output)
            grads_2 = tape2.gradient(grads_1, last_conv_layer_output)
        grads_3 = tape1.gradient(grads_2, last_conv_layer_output)
            

    global_sum = np.sum(last_conv_layer_output, axis=(0, 1, 2))

    alpha_num = grads_2[0]
    alpha_denom = grads_2[0]*2.0 + grads_3[0]*global_sum
    alpha_denom = np.where(alpha_denom != 0.0, alpha_denom, 1e-10)
    
    alphas = alpha_num/alpha_denom
    alpha_normalization_constant = np.sum(alphas, axis=(0,1))
    alphas /= alpha_normalization_constant

    weights = np.maximum(grads_1[0], 0.0)

    deep_linearization_weights = np.sum(weights*alphas, axis=(0,1))
    grad_CAM_map = np.sum(deep_linearization_weights*last_conv_layer_output[0], axis=1)

    heatmap = np.maximum(grad_CAM_map, 0)
    max_heat = np.max(heatmap)
    if max_heat == 0:
        max_heat = 1e-10
    heatmap /= max_heat
    
    last_conv_layer_output = last_conv_layer_output[0]
    
#     heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.math.multiply(last_conv_layer_output,heatmap)
    heatmap = tf.reduce_sum(heatmap,axis=-1)
   
    heatmap = tf.squeeze(heatmap)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()