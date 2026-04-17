from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100, blank=True, null=True)),
                ('phone', models.CharField(max_length=50, blank=True, null=True)),
                ('email', models.EmailField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]