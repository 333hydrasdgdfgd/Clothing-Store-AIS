from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0005_alter_brand_supplier_purchaseorder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('sales_date', models.DateField(auto_now_add=True)),
                ('type_of_sale', models.CharField(choices=[('Walk-in', 'Walk-in'), ('Online', 'Online')], default='Walk-in', max_length=20)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('E-wallet', 'E-wallet')], default='Cash', max_length=20)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apparel.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apparel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderDetails',
            fields=[
                ('sales_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_sold', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sd_discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apparel.product')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='apparel.salesorder')),
            ],
        ),
    ]