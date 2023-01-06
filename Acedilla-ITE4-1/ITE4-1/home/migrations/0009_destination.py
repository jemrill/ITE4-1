

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contact_file1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
