from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0007_salesorder_salesorderdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('customer', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('paid','Paid'),('pending','Pending'),('overdue','Overdue')], default='pending', max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('receipt_type', models.CharField(choices=[('purchase','Purchase'),('payment-received','Payment Received'),('refund','Refund')], default='purchase', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_method', models.CharField(default='Cash', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]