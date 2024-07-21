from django.urls import path
from .views import *

# from . import test
# from .views import *

urlpatterns = [
    # path('demo/',test),
    # path('title/',demo),
    # path('title2/',demo2)
    path('',index),
    path('addproducts/',post_product),
    path('updateproducts/<int:product_id>',update_product),
    path('deleteproducts/<int:product_id>',delete_product),
    path('addcategory/',post_category),
    path('categories/',show_category),
    path('updatecategory/<int:category_id>',update_category),
    path('deletecategory/<int:category_id>',delete_category)

    
    




]