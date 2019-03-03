from django.shortcuts import render

def home(request):
    if request.method == 'GET' and 'fulltext' in request.GET:
        text = request.GET['fulltext']
        words = text.split()
        word_dictionary = {}
        for word in words:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1       
        return render(request, 'home.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})
    else:
        return render(request, 'home.html')