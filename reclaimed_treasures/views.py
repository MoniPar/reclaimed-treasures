from django.shortcuts import render


def error404(request, exception):
    """
    Handles 404 http error - Page Not Found
    """
    return render(request, '404.html', status=404)


def error403(request, exception):
    """
    Handles 403 http error - Forbidden
    """
    return render(request, '403.html', status=403)


def error500(request):
    """
    Handles 500 http error - Server Error
    """
    return render(request, '500.html', status=500)
