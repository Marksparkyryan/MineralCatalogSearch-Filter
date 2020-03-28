import io
import os
from django.http import HttpResponse


def challenge(request):
    """Endpoint for ssl/tls chalenge"""
    content = os.environ.get('SSL_CHALLENGE')
    return HttpResponse(content, content_type='text/plain')
    