import nltk
from django.http import HttpResponse
from django.shortcuts import render
from textblob import TextBlob

# Ensure nltk data is downloaded to avoid runtime errors
nltk.download('punkt')

def home(request):
    return render(request, 'index.html')

def analyze(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text', '')
        blob = TextBlob(user_text)

        polarity = blob.polarity
        subjectivity = blob.subjectivity

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        return render(request, 'result.html', {
            'text': user_text,
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity
        })
    else:
        return HttpResponse("Invalid request method.")

# Add these views to your Django app's urls.py file:
 urlpatterns = [
     path('', home, name='home'),
     path('analyze/', analyze, name='analyze'),
 ]
