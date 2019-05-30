# Generated by Django 2.2.1 on 2019-05-18 14:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userType', models.CharField(
                    choices=[('SL', 'SLKF'), ('AS', 'association'), ('DI', 'district'), ('PR', 'province'),
                             ('AD', 'admin')], default='AD', max_length=2)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.SmallIntegerField(primary_key=True, serialize=False,
                                                     validators=[django.core.validators.MinValueValidator(1)],
                                                     verbose_name='Event Number')),
                ('eventName', models.CharField(max_length=100, verbose_name='Event Name')),
                ('kumite', models.BooleanField(choices=[(True, 'Kumite'), (False, 'Kata')], default=True,
                                               verbose_name='Event Category')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateID', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('isOpen', models.BooleanField(default=True, help_text='Designates whether registrations is open',
                                               verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('associationName', models.CharField(max_length=100, verbose_name='Association Name')),
                ('address', models.CharField(max_length=1000)),
                ('telephone', models.CharField(max_length=12)),
                ('chiefInstructorName', models.CharField(max_length=100, verbose_name='Chief Instructor Name')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('districtSecretaryName', models.CharField(max_length=100, verbose_name='District Secretary Name')),
                ('telephone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('provinceSecretaryName', models.CharField(max_length=100, verbose_name='Province Secretary Name')),
                ('telephone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Slkf',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(max_length=50, verbose_name='Position at SLKF')),
                ('telephone', models.CharField(max_length=12)),
            ],
        ),

        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=100, verbose_name='Player Name')),
                ('telephone', models.CharField(max_length=12, verbose_name='Telephone')),
                ('event',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManagementSystem.Event')),
                ('association',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManagementSystem.Association',
                                   verbose_name='Association Name')),
                ('district',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManagementSystem.District')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManagementSystem.Province'),
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('coachID', models.CharField(max_length=10, primary_key=True, serialize=False,
                                             verbose_name='Registration Number')),
                ('coachName', models.CharField(max_length=100, verbose_name='Name of the Coach')),
                ('telephone', models.CharField(max_length=12)),
                ('association',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManagementSystem.Association',
                                   verbose_name='Association Name')),
            ],
        ),
    ]