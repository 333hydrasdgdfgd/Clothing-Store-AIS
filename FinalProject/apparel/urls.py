from django.urls import path
from . import views

urlpatterns = [
    path('', views.coverpage, name='coverpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/edit/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('get-products-by-supplier/<int:supplier_id>/', views.get_products_by_supplier, name='get_products_by_supplier'),
    # NEW: products filtered by category (used in create sales order)
    path('get-products-by-category/<int:category_id>/', views.get_products_by_category, name='get_products_by_category'),

    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.supplier_create, name='supplier_create'),
    path('suppliers/edit/<int:pk>/', views.supplier_update, name='supplier_update'),
    path('suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_create, name='customer_create'),
    path('customers/edit/<int:pk>/', views.customer_update, name='customer_update'),
    path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('employees/edit/<int:pk>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    path('get-attributes/<int:category_id>/', views.get_attributes, name='get_attributes'),

    path('purchase-orders/', views.purchase_orders, name='purchase_orders'),
    path('purchase-orders/create/', views.create_purchase_order, name='create_purchase_order'),
    path('purchase-orders/<int:pk>/', views.purchase_order_details, name='purchase_order_details'),
    path('purchase-orders/<int:pk>/receive/', views.receive_order, name='receive_order'),

    path('sales-orders/', views.sales_orders, name='sales_orders'),
    path('sales-orders/create/', views.create_sales_order, name='create_sales_order'),
    path('sales-orders/<int:pk>/', views.sales_order_details, name='sales_order_details'),

    path('accounting/', views.accounting, name='accounting'),
    path('api/invoices/', views.api_invoices, name='api_invoices'),
    path('api/invoices/<int:pk>/', views.api_invoice_detail, name='api_invoice_detail'),
    path('api/receipts/', views.api_receipts, name='api_receipts'),
    path('api/receipts/<int:pk>/', views.api_receipt_detail, name='api_receipt_detail'),
    path('api/expenses/', views.api_expenses, name='api_expenses'),
    path('api/expenses/<int:pk>/', views.api_expense_detail, name='api_expense_detail'),
    path('api/sales-orders-accounting/', views.api_sales_orders_accounting, name='api_sales_orders_accounting'),
    path('api/purchase-orders-accounting/', views.api_purchase_orders_accounting, name='api_purchase_orders_accounting'),

    # NEW: Excel export endpoints for accounting section
    path('export/invoices/', views.export_invoices_excel, name='export_invoices_excel'),
    path('export/receipts/', views.export_receipts_excel, name='export_receipts_excel'),
    path('export/expenses/', views.export_expenses_excel, name='export_expenses_excel'),
    path('export/sales-orders/', views.export_sales_orders_excel, name='export_sales_orders_excel'),
    path('export/purchase-orders/', views.export_purchase_orders_excel, name='export_purchase_orders_excel'),

    path('shipping/', views.shipping_list, name='shipping_list'),
    path('shipping/status/<int:pk>/', views.update_shipping_status, name='update_shipping_status'),
    path('sales-orders/<int:pk>/shipping-status/', views.update_shipping_from_so, name='update_shipping_from_so'),

    path('transactions/', views.transactions_page, name='transactions'),

    path('audit-log/', views.audit_log_view, name='audit_log'),
    path('transactions/product-detail/<int:product_id>/', views.product_transaction_detail, name='product_transaction_detail'),
]