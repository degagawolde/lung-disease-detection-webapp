class Explanation:
    def __init__(self) -> None:
        pass
    
    def explanation(self,imagepath):
        im = cv2.imread(imagepath)
        im = cv2.resize(im, (256,256), interpolation = cv2.INTER_AREA)
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.reshape(img,(1,256,256,3))
    
        heatmap_cam = make_cam_heatmap(img, model, 'out_relu')
        heatmap_gradcam = make_grad_cam_pp_heatmap(img, model, 'out_relu')
        save_and_display_gradcam(im, heatmap_gradcam,2*count-1,title='gradcam')