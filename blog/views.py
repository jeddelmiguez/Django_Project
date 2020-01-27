from django.shortcuts import render

# Dummy data to be used in displaying into the home.html file with a database yet
# See 'context' under def home (request): section below
# See home.html <body> code for the for loop to display this data
posts = [
    {
        'author': 'JedRD',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 27, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 28, 2020'
    }    
]

# Create your views here.
# Functions

def home(request):
    context = {
        'posts': posts #Passing the data into the home.html file
    }
    return render(request, 'blog/home.html', context) # 'context' added as third argument

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
