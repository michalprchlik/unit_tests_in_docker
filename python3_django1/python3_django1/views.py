from rest_framework.views import APIView
from rest_framework.response import Response
import json

class ApiView(APIView):
    def get(self, request):
        response = Response('Hello world')
        return response

    def post(self, request):
        expression = request.data.get('data')
        text = request.data
        try:
            result = eval(expression)
        except (SyntaxError, ValueError, TypeError):
            result = 'invalid input'
        except ZeroDivisionError as err:
            result = 'division by 0'
        response =  Response(data=result)
        return response
         