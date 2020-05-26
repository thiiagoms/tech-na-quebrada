# Generated by Django 3.0.6 on 2020-05-25 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_address', models.CharField(max_length=100)),
                ('community_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=50)),
                ('community_image', models.ImageField(upload_to='img_community')),
                ('community_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.CommunityAddress')),
            ],
        ),
    ]