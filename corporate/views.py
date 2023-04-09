from rest_framework.views import APIView

from users.models import *
from .models import *
from rest_framework.response import Response
class VerifyIdentity(APIView):
    """
    Verify the identity of the user that wants to identify themselves using this
    digital identity system, in order to access the corporate agency's services.
    """
    def post(self, request):
        pass

def get_all_fields(model):
    return [field.name for field in model._meta.get_fields()]
class PersonaldetailsFields(APIView):
    def get(self, request):
        return Response(get_all_fields(UserDetails))