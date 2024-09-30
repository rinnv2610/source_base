from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from collections import OrderedDict


class CustomPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        try:
            return super().paginate_queryset(queryset, request, view=view)
        except NotFound:
            return []

    def get_paginated_response(self, data):
        if hasattr(self, 'page') and self.page is not None:
            return super().get_paginated_response(data)
        else:
            return Response(OrderedDict([
                ('count', None),
                ('next', None),
                ('previous', None),
                ('results', data)
            ]))
