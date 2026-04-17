from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0008 invoice receipt expense'),
    ]

    operations = [
        # Make Product.size and Product.color nullable
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='apparel.size'
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='apparel.color'
            ),
        ),
        # Make PurchaseOrder.employee nullable
        migrations.AlterField(
            model_name='purchaseorder',
            name='employee',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='apparel.employee'
            ),
        ),
        # Make SalesOrder.employee nullable
        migrations.AlterField(
            model_name='salesorder',
            name='employee',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='apparel.employee'
            ),
        ),
        # Add sales_order FK to Invoice
        migrations.AddField(
            model_name='invoice',
            name='sales_order',
            field=models.OneToOneField(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='invoice',
                to='apparel.salesorder'
            ),
        ),
        # Add purchase_order FK to Receipt
        migrations.AddField(
            model_name='receipt',
            name='purchase_order',
            field=models.OneToOneField(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='receipt',
                to='apparel.purchaseorder'
            ),
        ),
        # Create ShippingDetails model
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('shipping_id', models.AutoField(primary_key=True, serialize=False)),
                ('recipient_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_address', models.TextField()),
                ('shipping_method', models.CharField(default='LBC', max_length=50)),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('shipping_status', models.CharField(
                    choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')],
                    default='Pending', max_length=20
                )),
                ('sales_order', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='shipping',
                    to='apparel.salesorder'
                )),
            ],
        ),
    ]