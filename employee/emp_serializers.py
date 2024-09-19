from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        fields = [
            'user_id', 'username', 'email', 'phone_number', 'password',
            'date_of_birth', 'position', 'profile_picture', 'address', 'bio'
        ]

    def create(self, validate_data):
        password = validate_data.pop('password')
        employee = Employee(**validate_data)
        employee.set_password(password)
        employee.save()

        return employee
