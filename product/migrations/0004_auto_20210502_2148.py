# Generated by Django 3.2 on 2021-05-02 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('super-market', 'Supermarket'), ('health-beauty', 'Health & Beauty'), ('home-office', 'Home and Office'), ('phones-tablet', 'Phones & Tablet'), ('computing', 'Computing'), ('electronics', 'Electronics'), ('fashion', 'Fashion'), ('foot-wear', 'Foot Wear'), ('baby-products', 'Baby Products'), ('sporting-goods', 'Sporting goods'), ('automobile', 'Automobile')], max_length=40),
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='product.CartItem')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
