from rest_framework import serializers
from datetime import datetime
from django.contrib.postgres.fields import JSONField
from django.utils.functional import empty


class MonthField(serializers.Field):
    def to_representation(self, value):
        # Convert datetime object to "YYYYMM" string format
        return value.strftime('%Y%m')

    def to_internal_value(self, data):
        # Convert "YYYYMM" string to datetime object for the first day of the month
        year = int(data[:4])
        month = int(data[4:])
        return datetime(year, month, 1)


class OrderByField(serializers.Field):
    """
    Custom serializer field for handling orderBy parameter.
    """

    def to_internal_value(self, data):
        # Assuming the data is a string representing the field name and sorting order
        # Example: "field_name_asc" or "field_name_desc"
        parts = data.split('_')
        if len(parts) != 2:
            raise serializers.ValidationError('Invalid format for orderBy parameter.')

        field_name, sort_order = parts
        if sort_order not in ['asc', 'desc']:
            raise serializers.ValidationError('Invalid sort order. Must be "asc" or "desc".')

        return field_name, sort_order

    def to_representation(self, value):
        # This method is called when serializing the data to represent it
        field_name, sort_order = value
        return f"{field_name}_{sort_order}"


class CustomDateField(serializers.Field):
    def to_representation(self, value):
        # Convert datetime object to "yyyyMMdd" string format
        return value.strftime('%Y%m%d')

    def to_internal_value(self, data):
        # Convert "yyyyMMdd" string to datetime object
        return datetime.strptime(data, '%Y%m%d')


class EmptyListDefaultJSONBField(JSONField):
    def get_default(self):
        default = super().get_default()
        if default is empty:
            # Return an empty list as the default value
            return []
        return default
