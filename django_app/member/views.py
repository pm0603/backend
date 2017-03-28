from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
                return Response("이메일 혹은 비밀번호가 올바르지 않습니다.", status=status.HTTP_400_BAD_REQUEST)


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
                    return Response("이미 존재하는 email 입니다.", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("회원가입이 완료되었습니다.", status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.user.auth:
            request.user.auth_token.delete()
            return Response("정상적으로 로그아웃 되었습니다.", status=status.HTTP_200_OK)
        else:
            return Response("이미 로그아웃 되었습니다.", status=status.HTTP_400_BAD_REQUEST)
