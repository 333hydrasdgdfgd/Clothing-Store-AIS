from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0003_customer_employee'),  # last migration applied
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='supplier',
            field=models.ForeignKey(null=True, blank=True, on_delete=models.CASCADE, to='apparel.supplier'),
        ),
    ]