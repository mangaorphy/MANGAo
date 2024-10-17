import os
from django.conf import settings
from django.shortcuts import render
from .forms import ImageUploadForm
import tensorflow as tf  # or torch for PyTorch
from PIL import Image
import numpy as np

# Load the trained model once when the app starts
model = tf.keras.models.load_model('path_to_your_model.h5')  # Update with your model's path

# Helper function to make prediction
def make_prediction(image_path):
    # Preprocess the uploaded image
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize to match model input size
    img_array = np.array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction using the AI model
    prediction = model.predict(img_array)
    return prediction_to_label(prediction)  # Convert model output to a readable label

# Convert prediction result into a human-readable label
def prediction_to_label(prediction):
    # Example: convert model output into a readable label (you should modify this)
    return "Predicted Disease or Pest"

# The view to handle image upload and return prediction
def diagnose_plant(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image
            image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT, image.name)

            # Save the uploaded image to the media directory
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Make a prediction using the AI model
            prediction = make_prediction(image_path)

            # Pass the result to the template
            context = {'form': form, 'prediction': prediction}
            return render(request, 'diagnose.html', context)

    else:
        form = ImageUploadForm()

    return render(request, 'diagnose.html', {'form': form})
