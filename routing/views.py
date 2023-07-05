from django.shortcuts import render
# connect models and templates.


def routing_page(request):
    return render(request, 'routing/routing_page.html', {})