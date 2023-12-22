
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_alter_todo_details_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_details',
            new_name='TodoDetails',
        ),
    ]
