from rest_framework import viewsets
from .models import Employee
from .emp_serializers import EmployeeSerializer
import logging
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


logger = logging.getLogger('employee')


class RegisterView(generics.CreateAPIView):

    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers =self.get_success_headers(serializer.data)

        return Response({"message":"Employee created successfully",
                         "employee":serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # TODO
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        logger.info(f"Creating a new employee with data: {request.data}")

        try:
            response = super().create(request, *args, **kwargs)
            emp_id = response.data.get('user_id')
            logger.info(f"Employee created with ID: {emp_id}")
            return Response({"message":" Employee created successfully",
                             "data":response.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating employee: {str(e)}")
            raise

    def update(self, request, *args, **kwargs):
        emp_id = kwargs.get('pk')
        logger.info(f"Updating employee with ID: {emp_id}")

        try:
            employee = self.get_object()
        except NotFound:
            logger.error(f"Employee with ID {emp_id} not found.")
            return Response({"message": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)


        try:
            response = super().update(request, *args, **kwargs)
            logger.info(f"Updated employee with ID: {emp_id}")
            return Response({"message": "Employee updated successfully.",
                             "data": response.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Error updating employee: {str(e)}')
            return Response({"message": "Error updating employee."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):

        emp_id = kwargs.get('pk')
        logger.info(f"Attempting to delete employee with ID: {emp_id}")
        employee = get_object_or_404(Employee, pk=emp_id)

        try:
            response = super().destroy(request, *args, **kwargs)
            logger.info(f"Employee deleted with ID: {emp_id}")
            return Response({"message": "Employee deleted successfully."},
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting employee with ID {emp_id}: {str(e)}")
            return Response({"error": "An error occurred while deleting the employee."},
                            status=status.HTTP_400_BAD_REQUEST)