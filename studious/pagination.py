from rest_framework import pagination

class PersonPagination(pagination.PageNumberPagination):       
       page_size = 6000

class OrgPagination(pagination.PageNumberPagination):       
       page_size = 600