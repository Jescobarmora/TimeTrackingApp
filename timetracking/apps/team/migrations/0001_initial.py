# Generated by Django 4.0.5 on 2022-06-10 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('max_projects_per_team', models.IntegerField(default=0)),
                ('max_members_per_team', models.IntegerField(default=0)),
                ('max_tasks_per_project', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=10)),
                ('plan_end_date', models.DateTimeField(blank=True, null=True)),
                ('plan_status', models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled')], default='active', max_length=20)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_teams', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.plan')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('invited', 'Invited'), ('accepted', 'Accepted')], default='invited', max_length=20)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='team.team')),
            ],
        ),
    ]