from django.urls import path
from server.views.face_identity_views import FaceIdentityViewSet

urlpatterns=[
    path("", FaceIdentityViewSet.as_view({
        "get": "getAllFaceIdentities"
    })),
    path("encoded", FaceIdentityViewSet.as_view({
        "get": "getAllEncodedFaceIdentities"
    })),
    path("get/<str:primaryKey>", FaceIdentityViewSet.as_view({
        "get": "getFaceIdentity"
    })),
    path("create", FaceIdentityViewSet.as_view({
        "post": "createNewFaceIdentity"
    })),
    path("update/<str:primaryKey>", FaceIdentityViewSet.as_view({
        "put": "updateFaceIdentity"
    })),
    path("delete/<str:primaryKey>", FaceIdentityViewSet.as_view({
        "delete": "deleteFaceIdentity"
    }))
]
