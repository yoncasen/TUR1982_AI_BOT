from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def detect_bird(model_path, labels_path, image_path):
  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model(model_path, compile=False)

  # Load the labels
  class_names = open(labels_path, "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(image_path).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  #print(prediction)
  index = np.argmax(prediction)
  #print(index)
  class_name = class_names[index]
  #print(class_name)
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  return class_name[2:], confidence_score

#print(detect_bird("converted_keras/keras_model.h5","converted_keras/labels.txt","img/images.jpeg"))