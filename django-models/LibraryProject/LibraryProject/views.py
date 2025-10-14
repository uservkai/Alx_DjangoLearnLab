from django.shortcuts import redirect

def root_redirect(request):
    return redirect('index') #index in name of bookshelf home view