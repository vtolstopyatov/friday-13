import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import CustomUser as User
from .serializers import CustomUserSerializer, UserpicSerializer


class CustomUserViewSet(UserViewSet):
    """Кастомный вьюсет для работы с пользователем."""

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("^email", "^username", "^first_name", "^last_name")

    @action(
        methods=["patch"],
        detail=True,
        permission_classes=(IsAuthenticated,),
        url_path="update-user-pic",
    )
    def update_user_pic(self, request, **kwargs):
        user = request.user
        serializer = UserpicSerializer(
            user,
            partial=True,
            data=self.request.data,
            context={"request": request},
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class ActivateUserView(GenericAPIView):
    """Подтверждение мейла."""

    permission_classes = [AllowAny]

    def get(self, request, uid, token, format=None):
        """Отправка POST вместо GET."""
        payload = {"uid": uid, "token": token}
        actiavtion_url = settings.ACTIVATION_URL
        response = requests.post(actiavtion_url, data=payload)
        if response.status_code == 204:
            return HttpResponseRedirect(redirect_to=settings.LOGIN_URL_)
        return Response(response.json())