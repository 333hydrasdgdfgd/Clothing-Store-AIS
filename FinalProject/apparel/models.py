from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Category
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# Supplier
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.supplier_name

# Brand linked to Category and Supplier
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.brand_name

# Size linked to Category
class Size(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size_name = models.CharField(max_length=50)

    def __str__(self):
        return self.size_name

# Color linked to Category
class Color(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

# Material linked to Category
class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=50)

    def __str__(self):
        return self.material_name

# Main Product model
class Product(models.Model):
    product_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

# Customer model
class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


# Employee model
class Employee(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Sales Manager'),
        ('Purchasing', 'Purchasing Staff'),
        ('Inventory', 'Inventory Clerk'),
        ('Sales', 'Sales / Cashier'),
        ('Accounting Manager', 'Accounting Manager'),
        ('Staff Accountant', 'Staff Accountant')
    ]

    full_name = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Sales')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True, default='')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    username = models.CharField(max_length=50, unique=True, default='')
    password = models.CharField(max_length=128, blank=True, null=True, default='')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.full_name} ({self.role})"

# Purchase Order
class PurchaseOrder(models.Model):

    purchase_order_id = models.AutoField(primary_key=True)

    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE
    )

    employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    order_date = models.DateField(auto_now_add=True)

    expected_delivery_date = models.DateField()

    received_date = models.DateTimeField(null=True, blank=True)

    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    po_discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Received', 'Received'),
        ('Cancelled', 'Cancelled')
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"PO-{self.purchase_order_id}"

class PurchaseOrderDetails(models.Model):

    po_detail_id = models.AutoField(primary_key=True)

    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name="details"
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )

    quantity_ordered = models.IntegerField()

    unit_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"POD-{self.po_detail_id}"

# Sales Order
class SalesOrder(models.Model):

    sales_id = models.AutoField(primary_key=True)

    SALE_TYPE_CHOICES = [
        ('Walk-in', 'Walk-in'),
        ('Online', 'Online'),
    ]

    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('E-wallet', 'E-wallet'),
    ]

    sales_date = models.DateField(auto_now_add=True)
    type_of_sale = models.CharField(max_length=20, choices=SALE_TYPE_CHOICES, default='Walk-in')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    freight_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # NEW: manual freight cost
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"SO-{self.sales_id}"


# Sales Order Details
class SalesOrderDetails(models.Model):

    sales_detail_id = models.AutoField(primary_key=True)

    sales_order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name='details'
    )

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    quantity_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sd_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"SOD-{self.sales_detail_id}"


# Shipping Details — auto-created for Online sales orders
class ShippingDetails(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    sales_order = models.OneToOneField(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name='shipping'
    )
    recipient_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.TextField()
    shipping_method = models.CharField(max_length=50, default='LBC')
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    shipping_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"SHIP-{self.shipping_id} — {self.recipient_name}"


# Accounting — Invoice (auto-generated from SalesOrder)
class Invoice(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue'),
    ]
    ref = models.CharField(max_length=50)
    date = models.DateField()
    customer = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)
    sales_order = models.OneToOneField(
        SalesOrder, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoice'
    )

    def __str__(self):
        return f"{self.ref} — {self.customer}"


# Accounting — Receipt (auto-generated from PurchaseOrder)
class Receipt(models.Model):
    RECEIPT_TYPE_CHOICES = [
        ('purchase', 'Purchase'),
        ('payment-received', 'Payment Received'),
        ('refund', 'Refund'),
    ]
    ref = models.CharField(max_length=50)
    date = models.DateField()
    source = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    receipt_type = models.CharField(max_length=30, choices=RECEIPT_TYPE_CHOICES, default='purchase')
    created_at = models.DateField(auto_now_add=True)
    purchase_order = models.OneToOneField(
        PurchaseOrder, on_delete=models.SET_NULL, null=True, blank=True, related_name='receipt'
    )

    def __str__(self):
        return f"{self.ref} — {self.source}"


# Accounting — Expense
class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=30, default='Cash')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} — {self.category} ₱{self.amount}"

class InventoryTransaction(models.Model):
    """Track all inventory movements"""
    TRANSACTION_TYPE_CHOICES = [
        ('PURCHASE', 'Purchase Receipt'),
        ('SALE', 'Sale'),
        ('ADJUSTMENT', 'Inventory Adjustment'),
        ('RETURN', 'Return'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES, db_index=True)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reference_type = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    balance_after = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['product', 'created_at']),
            models.Index(fields=['transaction_type', 'created_at']),
        ]

    def __str__(self):
        sign = '+' if self.quantity > 0 else ''
        return f"{self.product.product_code} — {self.transaction_type} ({sign}{self.quantity})"

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('LOGIN',    'Login'),
        ('LOGOUT',   'Logout'),
        ('CREATE',   'Create'),
        ('EDIT',     'Edit'),
        ('DELETE',   'Delete'),
        ('RECEIVE',  'Receive'),
        ('STATUS',   'Status Change'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )
    employee_name = models.CharField(max_length=100, blank=True, null=True)  # snapshot in case employee is deleted
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f"[{self.datetime:%Y-%m-%d %H:%M}] {self.employee_name} — {self.action}: {self.description[:60]}"