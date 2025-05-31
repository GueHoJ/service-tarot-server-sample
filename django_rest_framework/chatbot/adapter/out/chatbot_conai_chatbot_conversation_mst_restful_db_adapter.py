from rest_framework.response import Response
from rest_framework import status
from django.db import models
from datetime import datetime
import logging

import app.utils.common_utils as common_utils
from ...serializers.conai_chatbot_conversation_mst_restful_serializer import ConaiChatbotConversationMstGetSerializer, ConaiChatbotConversationMstPostSerializer, \
    ConaiChatbotConversationMstPutSerializer, ConaiChatbotConversationMstDeleteSerializer
from ...domain.CONAI_CHATBOT_CONVERSATION_MST import ConaiChatbotConversationMst

logger = logging.getLogger(__name__)


class ChatbotConaiChatbotConversationMstRestfulDbAdapter:
    """
    # CLASS : ChatbotConaiChatbotConversationMstRestfulDbAdapter
    # AUTHOR : conai
    # TIME : 2024. 12. 24. 오후 2:32
    # DESCRIPTION
        - conai_chatbot_conversation_mst Restful API DB Adapter
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 24.          conai          최초 생성
    """

    def __init__(self,
                #  db_object: ConaiChatbotConversationMst,
                #  get_serializer: ConaiChatbotConversationMstGetSerializer,
                #  post_serializer: ConaiChatbotConversationMstPostSerializer,
                #  put_serializer: ConaiChatbotConversationMstPutSerializer,
                #  delete_serializer: ConaiChatbotConversationMstDeleteSerializer,
                 ):
        # self.db_object = db_object
        # self.get_serializer = get_serializer
        # self.post_serializer = post_serializer
        # self.put_serializer = put_serializer
        # self.delete_serializer = delete_serializer
        pass

    def chatbot_conai_chatbot_conversation_mst_restful_db(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"chatbot_conai_chatbot_conversation_mst_restful_db self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"chatbot_conai_chatbot_conversation_mst_restful_db args ==> {args}")

        db = args[1]
        sql_query = args[2]
        data = args[3]
        target_params = args[4]

        param_list = common_utils.get_target_params_list(data, target_params)
        dbResult = common_utils.execute_raw_sql_query(db, sql_query, param_list)

        for result in dbResult:
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db result ==> {result}")

        return dbResult

    def chatbot_conai_chatbot_conversation_mst_restful_db_get(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"chatbot_conai_chatbot_conversation_mst_restful_db_get self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"chatbot_conai_chatbot_conversation_mst_restful_db_get args ==> {args}")
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

        print(f"chatbot_conai_chatbot_conversation_mst_restful_db_get filter_kwargs_snakecase ==> {filter_kwargs_snakecase}")

        # Get orderBy parameter from request.data
        order_by = filter_kwargs.get('orderBy', None)
        if order_by:
            filter_kwargs_snakecase.pop('order_by', None)
            field_name, sort_order = order_by.split('_')
            result_objects = ConaiChatbotConversationMst.objects.filter(**filter_kwargs_snakecase).order_by(
                common_utils.camelcase_to_snakecase(
                    field_name) if sort_order == 'asc' else f"-{common_utils.camelcase_to_snakecase(field_name)}")
        else:
            result_objects = ConaiChatbotConversationMst.objects.filter(**filter_kwargs_snakecase)
        print(f"chatbot_conai_chatbot_conversation_mst_restful_db_get result_objects ==> {result_objects}")
        result_serializer = ConaiChatbotConversationMstGetSerializer(result_objects, many=True)

        return result_serializer

    def chatbot_conai_chatbot_conversation_mst_restful_db_post(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"chatbot_conai_chatbot_conversation_mst_restful_db_post self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"chatbot_conai_chatbot_conversation_mst_restful_db_post args ==> {args}")

        data = args[3]

        if type(data) == list:
            result_serializer = ConaiChatbotConversationMstPostSerializer(data=args[3], many=True)
        else:
            result_serializer = ConaiChatbotConversationMstPostSerializer(data=args[3])

        return result_serializer

    def chatbot_conai_chatbot_conversation_mst_restful_db_put(self, *args, **kwargs):
        idx = 0
        for arg in args:
            print(
                f"chatbot_conai_chatbot_conversation_mst_restful_db_put self arg[{idx}] ==> {arg}")
            idx += 1
        print(
            f"chatbot_conai_chatbot_conversation_mst_restful_db_put args ==> {args}")

        data = args[3]
        print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put data ==> {data}")

        result_object = None

        # Check if data is a list
        if isinstance(data, list):
            # Bulk update
            print("chatbot_conai_chatbot_conversation_mst_restful_db_put Processing bulk update")

            # Extract and convert field names for all items
            filter_kwargs_list = []
            for item in data:
                # Extracting Update Data and Converting Field Names
                filter_kwargs = item
                filter_kwargs_snakecase = {
                    common_utils.camelcase_to_snakecase(key): value
                    for key, value in filter_kwargs.items()
                    if key is not None  # Skip None keys
                }
                filter_kwargs_list.append(filter_kwargs_snakecase)
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put filter_kwargs_list ==> {filter_kwargs_list}")

            # Collect all IDs from data
            ids = []
            for filter_kwargs_snakecase in filter_kwargs_list:
                conai_chatbot_conversation_mst_id = filter_kwargs_snakecase.get('conai_chatbot_conversation_mst_id')
                if conai_chatbot_conversation_mst_id:
                    ids.append(conai_chatbot_conversation_mst_id)
                else:
                    print("chatbot_conai_chatbot_conversation_mst_restful_db_put Error: Each item must contain 'ConaiChatbotConversationMstId' for bulk update")
                    return Response({"error": "Each item must contain 'ConaiChatbotConversationMstId' for bulk update"},
                                    status=status.HTTP_400_BAD_REQUEST)
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put ids ==> {ids}")

            # Fetch existing instances using filter
            instances = ConaiChatbotConversationMst.objects.filter(conai_chatbot_conversation_mst_id__in=ids)
            instances_dict = {str(instance.conai_chatbot_conversation_mst_id): instance for instance in instances}
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put instances_dict ==> {instances_dict}")

            # Ensure all instances are found
            if len(instances) != len(ids):
                missing_ids = set(ids) - set(instances_dict.keys())
                print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put Error: Records not found for IDs: {', '.join(missing_ids)}")
                return Response({"error": f"Records not found for IDs: {', '.join(missing_ids)}"},
                                status=status.HTTP_404_NOT_FOUND)

            # Order instances to match the order of data
            ordered_instances = []
            for filter_kwargs_snakecase in filter_kwargs_list:
                conai_chatbot_conversation_mst_id = filter_kwargs_snakecase.get('conai_chatbot_conversation_mst_id')
                instance = instances_dict.get(str(conai_chatbot_conversation_mst_id))
                ordered_instances.append(instance)
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put ordered_instances ==> {ordered_instances}")



            # Initialize serializer with existing instances and data
            result_serializer = ConaiChatbotConversationMstPutSerializer(
                ordered_instances,
                data=data,
                many=True,
                partial=True
            )
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put result_serializer (bulk) ==> {result_serializer}")

            result_object = {"ordered_instances": ordered_instances, "result_serializer": result_serializer}
            print(f"chatbot_conai_chatbot_conversation_mst result_object  ==> {result_object}")
        else:
            # Single update
            print("chatbot_conai_chatbot_conversation_mst_restful_db_put Processing single update")
            filter_kwargs = data

            # Extracting Update Data and Converting Field Names
            filter_kwargs_snakecase = {
                common_utils.camelcase_to_snakecase(key): value
                for key, value in filter_kwargs.items()
            }
            print(
                f"chatbot_conai_chatbot_conversation_mst_restful_db_put filter_kwargs_snakecase ==> {filter_kwargs_snakecase}")

            # Retrieving Unique Constraints
            conai_chatbot_conversation_mst_id = filter_kwargs_snakecase.get('conai_chatbot_conversation_mst_id')
            if not conai_chatbot_conversation_mst_id:
                print("chatbot_conai_chatbot_conversation_mst_restful_db_put Error: Parameter 'ConaiChatbotConversationMstId' is required for update")
                return Response({"error": "Parameter 'ConaiChatbotConversationMstId' is required for update"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Fetch existing instance
            try:
                result_object = ConaiChatbotConversationMst.objects.get(
                    conai_chatbot_conversation_mst_id=conai_chatbot_conversation_mst_id)
                print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put result_object ==> {result_object}")
            except ConaiChatbotConversationMst.DoesNotExist:
                print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put Error: Record not found for ID {conai_chatbot_conversation_mst_id}")
                return Response({"error": f"Record not found for ID {conai_chatbot_conversation_mst_id}"},
                                status=status.HTTP_404_NOT_FOUND)

            # Initialize serializer
            result_serializer = ConaiChatbotConversationMstPutSerializer(
                result_object,
                data=data,
                partial=True
            )
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put result_serializer (single) ==> {result_serializer}")

            result_object = {"result_serializer": result_serializer}
            print(f"chatbot_conai_chatbot_conversation_mst_restful_db_put result_object  ==> {result_object}")

        return result_object

    def chatbot_conai_chatbot_conversation_mst_restful_db_delete(self, *args, **kwargs):
        # Log incoming arguments
        logger.debug("Delete method called with args: %s, kwargs: %s", args, kwargs)

        # Get the filter kwargs from the last argument
        filter_kwargs = args[-1]
        logger.debug("Filter kwargs: %s", filter_kwargs)

        # Convert camelCase to snake_case
        filter_kwargs_snakecase = {common_utils.camelcase_to_snakecase(key): value
                                 for key, value in filter_kwargs.items()}
        logger.debug("Snake case filter kwargs: %s", filter_kwargs_snakecase)

        # Get primary key field name
        pk_field_name = ConaiChatbotConversationMst._meta.pk.name
        logger.debug("Primary key field name: %s", pk_field_name)

        # Check if primary key is provided
        if pk_value := filter_kwargs_snakecase.get(pk_field_name):
            logger.info("Attempting to delete object with %s=%s", pk_field_name, pk_value)
            try:
                result_objects = ConaiChatbotConversationMst.objects.get(**{pk_field_name: pk_value})
                logger.info("Found object to delete: %s", result_objects)
                return result_objects
            except ConaiChatbotConversationMst.DoesNotExist:
                logger.warning("Object with %s=%s not found", pk_field_name, pk_value)
                return Response(
                    {"error": f"Object with {pk_field_name}={pk_value} does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # If no primary key provided, check unique together fields
        unique_together = getattr(ConaiChatbotConversationMst._meta, 'unique_together', [])
        logger.debug("Checking unique together constraints: %s", unique_together)

        for unique_constraint in unique_together:
            unique_together_fields = {
                field: filter_kwargs_snakecase[field]
                for field in unique_constraint
                if field in filter_kwargs_snakecase
            }
            logger.debug("Checking unique constraint with fields: %s", unique_together_fields)

            if len(unique_together_fields) == len(unique_constraint):
                logger.info("Attempting to delete object with unique constraint: %s", unique_together_fields)
                try:
                    result_objects = ConaiChatbotConversationMst.objects.get(**unique_together_fields)
                    logger.info("Found object to delete: %s", result_objects)
                    return result_objects
                except ConaiChatbotConversationMst.DoesNotExist:
                    logger.debug("No object found with unique constraint: %s", unique_together_fields)
                    continue

        # If we get here, neither PK nor unique together fields were valid
        logger.warning("Invalid request: No valid primary key or unique constraint provided")
        return Response(
            {"error": "Request must contain either primary key or all fields of a unique constraint"},
            status=status.HTTP_400_BAD_REQUEST
        )
