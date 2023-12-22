
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0004_alter_tododetails_due_date_alter_tododetails_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododetails',
            name='tag',
            field=models.ManyToManyField(blank=True, to='app_todo.tag'),
        ),
    ]
