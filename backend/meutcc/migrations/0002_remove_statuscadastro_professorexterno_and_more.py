# Generated by Django 5.0.3 on 2024-03-23 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meutcc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuscadastro',
            name='professorExterno',
        ),
        migrations.RemoveField(
            model_name='tema',
            name='professor',
        ),
        migrations.DeleteModel(
            name='ProfessorExterno',
        ),
        migrations.DeleteModel(
            name='StatusCadastro',
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
    ]
