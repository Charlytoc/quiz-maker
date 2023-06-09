# Generated by Django 4.2 on 2023-04-30 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aitools', '0002_alter_templateai_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletionJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ERROR', 'Error'), ('SUCCESS', 'Success')], default='PENDING', max_length=9)),
                ('status_text', models.TextField(blank=True, default=None, null=True)),
                ('inputs', models.JSONField(blank=True, help_text='User value for template variables', null=True)),
                ('prompt', models.TextField(blank=True, default=None, null=True)),
                ('answer', models.TextField(blank=True, default=None, null=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aitools.templateai')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
