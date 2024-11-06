from rest_framework.views import APIView, status
from rest_framework.exceptions import NotFound, PermissionDenied

from rest_framework.response import Response
from libs.response import ResponseDict


class ExceptionAPIView(APIView):
      def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response(ResponseDict(success=False, message="Not Found", errors=exc.detail),
                status=status.HTTP_404_NOT_FOUND
            )
        elif isinstance(exc, PermissionDenied):
            return Response(
               ResponseDict(success=False, message="Forbidden Error", errors=exc.detail),
                status=status.HTTP_403_FORBIDDEN
            )
        return super().handle_exception(exc)
