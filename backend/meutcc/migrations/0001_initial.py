# Generated by Django 5.0.3 on 2024-03-23 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorExterno',
            fields=[
                ('professor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.professor')),
                ('identidade', models.FileField(upload_to='professoresExterno/identidade')),
                ('diploma', models.FileField(upload_to='professoresExterno/diploma')),
                ('statusCadastro', models.BooleanField()),
                ('dataStatus', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('app.professor',),
        ),
        migrations.CreateModel(
            name='StatusCadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprovacao', models.BooleanField()),
                ('justificativa', models.CharField(blank=True, max_length=255, null=True)),
                ('dataStatus', models.DateTimeField(auto_now_add=True)),
                ('professorExterno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meutcc.professorexterno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=500)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
