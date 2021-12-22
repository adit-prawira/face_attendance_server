import numpy as np
from rest_framework import status, viewsets
from rest_framework.response import Response
from server.models import FaceIdentity
from server.serializer import FaceIdentitySerializer
from server.errors.error_message import ErrorMessage
import urllib.request
import face_recognition
import cv2
import re


class FaceIdentityViewSet(viewsets.ViewSet):
    @classmethod
    def _openImageUrl(cls, imageUrl, readFlag=cv2.IMREAD_COLOR):
        res = (urllib.request.urlopen(imageUrl)).read()
        image = np.asarray(bytearray(res), dtype="uint8")
        return cv2.imdecode(image, readFlag)

    def getAllFaceIdentities(self, request):
        try:
            faceIdentities = FaceIdentity.objects.all()
            serializedFaceIdentities = FaceIdentitySerializer(faceIdentities, many=True).data
            for fi in serializedFaceIdentities:
                del fi["encodedFace"]
            return Response(serializedFaceIdentities, status=status.HTTP_200_OK)
        except:
            errorCode = status.HTTP_500_INTERNAL_SERVER_ERROR # this is an integer
            errorMessage = ErrorMessage("Unable to connect to database", errorCode).getMessageBody()
            return Response(errorMessage, status=errorCode)

    def getAllEncodedFaceIdentities(self, request):
        try:
            faceIdentities = FaceIdentity.objects.all()
            serializedFaceIdentities = FaceIdentitySerializer(faceIdentities, many=True).data

            dataToSend = []

            for fi in serializedFaceIdentities:

                dataToSend.append({
                    "id": fi["id"],
                    "name": fi["name"],
                    "encodedFace": eval(fi["encodedFace"])
                })
            return Response(dataToSend, status=status.HTTP_200_OK)
        except:
            errorCode = status.HTTP_500_INTERNAL_SERVER_ERROR
            errorMessage = ErrorMessage("ERROR: Unable to connect to database", errorCode).getMessageBody()
            return Response(errorMessage, status=errorCode)

    def getFaceIdentity(self, request, primaryKey = None):
        pass

    def createNewFaceIdentity(self, request):
        try:
            body = request.data
            postedImage = self._openImageUrl(body["imageUrl"])
            encodedData = re.sub("\s+", ",", str(face_recognition.face_encodings(postedImage)[0]).strip())
            newFaceIdentity = FaceIdentity.objects.create(
                name=body["name"],
                imageUrl=body["imageUrl"],
                encodedFace=encodedData
            )
            serializedFaceIdentity = FaceIdentitySerializer(newFaceIdentity, many=False).data
            serializedFaceIdentity["encodedFace"] = eval(serializedFaceIdentity["encodedFace"])
            return Response(serializedFaceIdentity, status=status.HTTP_201_CREATED)
        except:
            errorCode = status.HTTP_500_INTERNAL_SERVER_ERROR
            errorMessage = ErrorMessage("ERROR: Unable to connect to database", errorCode).getMessageBody()
            return Response(errorMessage, status=errorCode)

    def deleteFaceIdentity(self, request, primaryKey = None):
        try:
            targetIdentity = FaceIdentity.objects.get(id=primaryKey)
            targetIdentity.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except:
            errorCode = status.HTTP_404_NOT_FOUND
            errorMessage = ErrorMessage("ERROR: Identity not found", errorCode).getMessageBody()
            return Response(errorMessage, status=errorCode)

    def updateFaceIdentity(self, request, primaryKey=None):
        pass