import nap as nap
import requests
from django.contrib.auth import authenticate, logout
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from config.settings import config
from member.forms import UserForm, UserSignupForm
from member.models import MyUser


class Login(APIView):
    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            if user:
                token = Token.objects.get_or_create(user=user)[0]
                ret = {"token": token.key}
                return Response(ret, status=status.HTTP_200_OK)

            else:
                return Response({"error": "이메일 혹은 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class SignUp(APIView):
    def post(self, request, *args, **kwargs):
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            try:
                MyUser.objects.create_user(
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"],
                )
            except IntegrityError as e:
                if "email" in str(e):
                    return Response({"error": "이미 존재하는 email 입니다."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"success": "회원가입이 완료되었습니다."}, status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        logout(request)
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class FacebookLogin1(APIView):
    def post(self, request, *args, **kwargs):
        access_token = request.POST.get("access_token")
        url_debug_token = 'https://graph.facebook.com/debug_token?' \
                          'input_token={it}&' \
                          'access_token={at}'.format(
            it=access_token,
            at=settings.FB_APP_ACCESS_TOKEN
        )
        r = requests.get(url_debug_token)
        debug_token = r.json()
        if debug_token['data']['is_valid']:
            user_id = debug_token['data']['user_id']
            try:
                facebook_user = MyUser.objects.get(facebook_id=user_id)
            except MyUser.DoesNotExist:
                user_info = self.get_user_info(user_id, access_token)
                facebook_user = MyUser.objects.create_facebook_user(facebook_id=user_id,
                                                                    email=user_info['email'])
            token = Token.objects.get_or_create(user=facebook_user)[0]
            ret = {"token": token.key}
            return Response(ret, status=status.HTTP_200_OK)
        else:
            return Response({'error': debug_token['data']['error']['message']})

    def get_user_info(self, user_id, access_token):
        url_request_user_info = 'https://graph.facebook.com/' \
                                '{user_id}?' \
                                'fields=email&' \
                                'access_token={access_token}'.format(
            user_id=user_id,
            access_token=access_token
        )
        r = requests.get(url_request_user_info)
        user_info = r.json()
        return user_info


def home(request):
    context = RequestContext(
        request, {
            'request': request,
            'user': request.user
        }
    )
    return render_to_response('member/home.html', context=context)