from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

def predict_price(request):
    if request.method == "POST":
        # Get input data from POST request
        # Use your machine learning model for predictions
        predicted_price = 350000  # Placeholder
        return JsonResponse({"predicted_price": predicted_price})
    return render(request, "predict.html")
