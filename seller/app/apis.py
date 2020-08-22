from .models import Seller, Order
from rest_framework import viewsets, permissions
from .serializers import SellerSerializer, OrderSerializer
from datetime import datetime
from calendar import monthrange

class SellerViewSet(viewsets.ModelViewSet):
    """
    API of Seller
    \n@since 2020-08-22
    \n@author eliasssv
    """
    queryset = Seller.objects.all().order_by('fullname')
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned list containing the name of the Seller 
        \n@param: cpf (string)
        \n@since: 2020-08-22
        \n@author: eliasssv
        """
        cpf = self.request.query_params.get('cpf', None)
        if cpf is not None:
            self.queryset = self.queryset.filter(cpf__icontains=cpf)
        return self.queryset

class OrderViewSet(viewsets.ModelViewSet):
    """
    API of Order
    \n@since 2020-08-22
    \n@author eliasssv
    """
    queryset = Order.objects.all().order_by('code')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]    

    def get_queryset(self):
        """
        Optionally restricts the returned list containing the name, publication_year, edition, 
        author_name, author_id
        \n@param: initial_date (date dd/mm/yyyy)
        \n@param: final_date (date dd/mm/yyyy)
        \n@param: month (date mm/yyyy)
        \n@param: seller_cpf (string)
        \n@since: 2020-08-22
        \n@author: eliasssv
        """
        initial_date = self.request.query_params.get('initial_date', None)
        final_date = self.request.query_params.get('final_date', None)
        month = self.request.query_params.get('month', None)
        seller_cpf = self.request.query_params.get('seller_cpf', None)

        if month is not None:
            initial_date = datetime.strptime(f'01/{month}', '%d/%m/%Y')
            spl_month = month.split(sep='/')
            last_day_of_month = monthrange(spl_month[1],spl_month[0])[1]
            final_date = datetime.strptime(f'{last_day_of_month}/{month}')

        if initial_date is not None:
            self.queryset = self.queryset.filter(date__gte=initial_date)

        if final_date is not None:
            self.queryset = self.queryset.filter(date__lte=final_date)
        
        if seller_cpf is not None:
            self.queryset = self.queryset.filter(seller__cpf=seller_cpf)
        
        return self.queryset