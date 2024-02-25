from rest_framework.exceptions import ValidationError
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status


class ValidationError(ValidationError):
    def __init__(self, message):
        super().__init__(None, None)
        self.default_detail = message


class Result:
    @staticmethod
    def data(data=None, message='', status=status.HTTP_200_OK):
        return Response({'message': message, 'data': data}, status=status)

    @staticmethod
    def error(message='Not Found', status=None):
        return Response({'message': message}, status=status)

    @staticmethod
    def list(data_list, total_data, page_number, total_page, message=''):
        return Response({'message': message,
                         'data': {'list': data_list, 'total': total_data, 'page_number': page_number,
                                  'pages': total_page}}, status=status.HTTP_200_OK)

    @staticmethod
    def to_pagination(query_result, count, page=1, ):
        paginator = Paginator(query_result, count)
        page_obj = paginator.get_page(page)

        return page_obj.object_list, paginator.count, page, paginator.num_pages
