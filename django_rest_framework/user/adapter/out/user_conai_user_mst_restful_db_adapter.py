from rest_framework.response import Response
from rest_framework import status
from django.db import models
from datetime import datetime
from injector import inject

import app.utils.common_utils as common_utils
from ...serializers.conai_user_mst_restful_serializer import ConaiUserMstGetSerializer, ConaiUserMstPostSerializer, \
    ConaiUserMstPutSerializer, ConaiUserMstDeleteSerializer
from ...domain.CONAI_USER_MST import ConaiUserMst


class UserConaiUserMstRestfulDbAdapter:
    """
    # CLASS : UserConaiUserMstRestfulDbAdapter
    # AUTHOR : conai
    # TIME : 2024. 8. 20. 오후 3:51
    # DESCRIPTION
        - conai_user_mst Restful API DB Adapter
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 8. 20.          conai          최초 생성
    """

    @inject
    def __init__(self,
                #  db_object: ConaiUserMst,
                #  get_serializer: ConaiUserMstGetSerializer,
                #  post_serializer: ConaiUserMstPostSerializer,
                #  put_serializer: ConaiUserMstPutSerializer,
                #  delete_serializer: ConaiUserMstDeleteSerializer,
                 ):
        # self.db_object = db_object
        # self.get_serializer = get_serializer
        # self.post_serializer = post_serializer
        # self.put_serializer = put_serializer
        # self.delete_serializer = delete_serializer
        pass

    def user_conai_user_mst_restful_db(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"user_conai_user_mst_restful_db self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"user_conai_user_mst_restful_db args ==> {args}")

        db = args[1]
        sql_query = args[2]
        data = args[3]
        target_params = args[4]

        param_list = common_utils.get_target_params_list(data, target_params)
        dbResult = common_utils.execute_raw_sql_query(db, sql_query, param_list)

        for result in dbResult:
            print(f"user_conai_user_mst_restful_db result ==> {result}")

        return dbResult

    def user_conai_user_mst_restful_db_get(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"user_conai_user_mst_restful_db_get self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"user_conai_user_mst_restful_db_get args ==> {args}")
        filter_kwargs = args[3]

        # Convert keys from camel case to snake case
        filter_kwargs_snakecase = {common_utils.camelcase_to_snakecase(key): value for key, value in
                                   filter_kwargs.items()}

        # Handle date range filtering
        range_query_field = filter_kwargs_snakecase.pop('range_query_field', None)
        start_date = filter_kwargs_snakecase.pop('start_date', None)
        end_date = filter_kwargs_snakecase.pop('end_date', None)
        if range_query_field and start_date and end_date:
            # Convert string dates to datetime objects
            start_date = datetime.strptime(start_date, '%Y%m%d')
            end_date = datetime.strptime(end_date, '%Y%m%d')

            # Adjust the end date to include all records on that day
            end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            # Assuming reg_dtm is the field representing the datetime
            filter_kwargs_snakecase[f'{range_query_field}__range'] = [start_date, end_date]

        print(f"event_tba_event_user_pnt_mst_restful_db_get filter_kwargs_snakecase ==> {filter_kwargs_snakecase}")

        # Get orderBy parameter from request.data
        order_by = filter_kwargs.get('orderBy', None)
        if order_by:
            filter_kwargs_snakecase.pop('order_by', None)
            field_name, sort_order = order_by.split('_')
            result_objects = self.db_object.objects.filter(**filter_kwargs_snakecase).order_by(
                common_utils.camelcase_to_snakecase(
                    field_name) if sort_order == 'asc' else f"-{common_utils.camelcase_to_snakecase(field_name)}")
        else:
            result_objects = ConaiUserMst.objects.filter(**filter_kwargs_snakecase)
        print(f"user_conai_user_mst_restful_db_get result_objects ==> {result_objects}")
        result_serializer = ConaiUserMstGetSerializer(result_objects, many=True)

        return result_serializer

    def user_conai_user_mst_restful_db_post(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"user_conai_user_mst_restful_db_post self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"user_conai_user_mst_restful_db_post args ==> {args}")
        result_serializer = ConaiUserMstPostSerializer(data=args[3])

        return result_serializer

    def user_conai_user_mst_restful_db_put(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"user_conai_user_mst_restful_db_put self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"user_conai_user_mst_restful_db_put args ==> {args}")

        filter_kwargs = args[3]

        # Convert keys from camel case to snake case
        filter_kwargs_snakecase = {common_utils.camelcase_to_snakecase(key): value for key, value in
                                   filter_kwargs.items()}
        print(f"user_conai_user_mst_restful_db_put filter_kwargs_snakecase ==> {filter_kwargs_snakecase}")
        unique_together_fields = {}
        unique_together = getattr(ConaiUserMst._meta, 'unique_together', [])
        print(f"user_conai_user_mst_restful_db_put unique_together ==> {unique_together}")
        for unique_constraint in unique_together:
            print(f"user_conai_user_mst_restful_db_put unique_constraint ==> {unique_constraint}")
            for key, value in filter_kwargs_snakecase.items():
                print(f"user_conai_user_mst_restful_db_put key ==> {key}")
                print(f"user_conai_user_mst_restful_db_put value ==> {value}")
                if key in unique_constraint:
                    unique_together_fields[key] = value

        if unique_together:
            print(f"user_conai_user_mst_restful_db_put unique_togather_fields ==> {unique_together_fields}")
            result_objects = ConaiUserMst.objects.get(**unique_together_fields)

        elif filter_kwargs_snakecase.get(ConaiUserMst._meta.pk.name):
            print(f"user_conai_user_mst_restful_db_put filter_kwargs_snakecase[ConaiUserMst._meta.pk.name] ==> {filter_kwargs_snakecase[ConaiUserMst._meta.pk.name]}")
            # Use the primary key field name and its value for the lookup
            pk_field_name = ConaiUserMst._meta.pk.name
            pk_value = filter_kwargs_snakecase[pk_field_name]
            result_objects = ConaiUserMst.objects.get(**{pk_field_name: pk_value})

        else:
            # Unique together and PK fields are not provided, so we will use the filter kwargs to get the object
            # But it does not guarantee that only one object will be returned or no object will be returned
            # result_objects = ConaiUserMst.objects.filter(**filter_kwargs_snakecase)
            # raise ValidationError("Parameter Must Contain PK or Unique Together Fields")
            return Response({"error": "Parameter Must Contain PK or Unique Together Fields"}, status=status.HTTP_400_BAD_REQUEST)

        print(f"user_conai_user_mst_restful_db_put result_objects ==> {result_objects}")

        result_serializer = ConaiUserMstPutSerializer(result_objects, data=args[3], partial=True)

        return result_serializer

    def user_conai_user_mst_restful_db_delete(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"user_conai_user_mst_restful_db_delete self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"user_conai_user_mst_restful_db_delete args ==> {args}")

        filter_kwargs = args[3]

        # Convert keys from camel case to snake case
        filter_kwargs_snakecase = {common_utils.camelcase_to_snakecase(key): value for key, value in
                                   filter_kwargs.items()}
        print(f"user_conai_user_mstt_restful_db_delete filter_kwargs_snakecase ==> {filter_kwargs_snakecase}")
        unique_together_fields = {}
        unique_together = getattr(ConaiUserMst._meta, 'unique_together', [])
        print(f"user_conai_user_mst_restful_db_delete unique_together ==> {unique_together}")
        for unique_constraint in unique_together:
            print(f"user_conai_user_mst_restful_db_delete unique_constraint ==> {unique_constraint}")
            for key, value in filter_kwargs_snakecase.items():
                print(f"user_conai_user_mst_restful_db_delete key ==> {key}")
                print(f"user_conai_user_mst_restful_db_delete value ==> {value}")
                if key in unique_constraint:
                    unique_together_fields[key] = value

        print(f"user_conai_user_mst_restful_db_delete unique_togather_fields ==> {unique_together_fields}")

        if unique_together:
            print(f"user_conai_user_mst_restful_db_delete unique_togather_fields ==> {unique_together_fields}")
            result_objects = ConaiUserMst.objects.get(**unique_together_fields)

        elif filter_kwargs_snakecase.get(ConaiUserMst._meta.pk.name):
            print(f"user_conai_user_mst_restful_db_delete filter_kwargs_snakecase[ConaiUserMst._meta.pk.name] ==> {filter_kwargs_snakecase[ConaiUserMst._meta.pk.name]}")
            # Use the primary key field name and its value for the lookup
            pk_field_name = ConaiUserMst._meta.pk.name
            pk_value = filter_kwargs_snakecase[pk_field_name]
            result_objects = ConaiUserMst.objects.get(**{pk_field_name: pk_value})

        else:
            # Unique together and PK fields are not provided, so we will use the filter kwargs to get the object
            # But it does not guarantee that only one object will be returned or no object will be returned
            # result_objects = ConaiUserMst.objects.filter(**filter_kwargs_snakecase)
            # result_objects = ConaiUserMst.objects.filter(**filter_kwargs_snakecase)
            # raise ValidationError("Parameter Must Contain PK or Unique Together Fields")
            return Response({"error": "Parameter Must Contain PK or Unique Together Fields"}, status=status.HTTP_400_BAD_REQUEST)

        print(f"user_conai_user_mst_restful_db_delete result_objects ==> {result_objects}")

        return result_objects
