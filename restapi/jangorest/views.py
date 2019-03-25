
from .serializers import EmployeesSerializers
from .models import Employee
from rest_framework.response import Response

from rest_framework.views import APIView


class EmployeeList(APIView):


    def get(self,request, format=None):

        employees=Employee.objects.all()
        serializer=EmployeesSerializers(employees,many=True)
        return Response(serializer.data)

    def post(selfself,request):

