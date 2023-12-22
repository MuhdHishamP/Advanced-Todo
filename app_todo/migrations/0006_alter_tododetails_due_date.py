
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0005_alter_tododetails_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododetails',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
