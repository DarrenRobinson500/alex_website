# Generated by Django 4.2.8 on 2023-12-27 21:28

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking_alter_quote_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]