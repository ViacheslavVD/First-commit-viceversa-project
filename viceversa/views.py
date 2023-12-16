from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	splite_words = user_text.split()
	num_words = len(splite_words)

	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'numwords':num_words})
