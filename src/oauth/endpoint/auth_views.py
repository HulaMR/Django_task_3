from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializer
from ..services.google import check_google_auth


def google_login(requests):
    return render(requests, 'google_login.html')


@api_view(['POST'])
def google_auth(requests):
    google_data = serializer.GoogleAuth(data=requests.data)
    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
