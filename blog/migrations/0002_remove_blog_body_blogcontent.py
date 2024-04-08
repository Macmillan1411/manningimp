# Generated by Django 5.0.4 on 2024-04-08 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('element_type', models.CharField(choices=[('heading', 'Heading'), ('paragraph', 'Paragraph'), ('list', 'List'), ('image', 'Image')], max_length=10)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='blog_images/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='blog.blog')),
            ],
        ),
    ]