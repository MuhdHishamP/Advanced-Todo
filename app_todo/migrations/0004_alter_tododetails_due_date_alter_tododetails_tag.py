from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0003_rename_todo_details_tododetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododetails',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tododetails',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='app_todo.tag'),
        ),
    ]
