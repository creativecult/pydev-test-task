
def settings(request):
    from django.conf import settings
    return settings.__dict__['_wrapped'].__dict__
