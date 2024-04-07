# Generated by Django 5.0.3 on 2024-04-07 14:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statustcc',
            name='tcc',
        ),
        migrations.AlterModelOptions(
            name='professorexterno',
            options={},
        ),
        migrations.RenameField(
            model_name='semestre',
            old_name='settings',
            new_name='configuracoes',
        ),
        migrations.RemoveField(
            model_name='professorexterno',
            name='statusCadastro',
        ),
        migrations.AddField(
            model_name='sessao',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='ficha_avaliacao',
            field=models.FileField(blank=True, null=True, upload_to='avaliacoes/fichas'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='grau_academico',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='titulos',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professorexterno',
            name='diploma',
            field=models.FileField(blank=True, null=True, upload_to='professoresExterno/diploma'),
        ),
        migrations.AlterField(
            model_name='professorexterno',
            name='identidade',
            field=models.FileField(blank=True, null=True, upload_to='professoresExterno/identidade'),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='dataAberturaSemestre',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='dataFechamentoSemestre',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='autorizacaoPublicacao',
            field=models.FileField(blank=True, null=True, upload_to='tcc/autorizacaoPublicacao'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='documentoTCC',
            field=models.FileField(blank=True, null=True, upload_to='tcc/documento'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='prazoEntregaFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='prazoEntregaPrevia',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.CreateModel(
            name='TccStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PROPOSTA_ANALISE_PROFESSOR', 'Proposta Analise Professor'), ('PROPOSTA_RECUSADA_PROFESSOR', 'Proposta Recusada Professor'), ('PROPOSTA_ANALISE_COORDENADOR', 'Proposta Analise Coordenador'), ('PROPOSTA_RECUSADA_COORDENADOR', 'Proposta Recusada Coordenador'), ('DESENVOLVIMENTO', 'Desenvolvimento'), ('PREVIA', 'Previa'), ('REPROVADO_PREVIA', 'Reprovado Previa'), ('FINAL', 'Final'), ('REPROVADO_FINAL', 'Reprovado Final'), ('AJUSTE', 'Ajuste'), ('APROVADO', 'Aprovado')], max_length=255)),
                ('justificativa', models.TextField(blank=True, null=True)),
                ('dataStatus', models.DateTimeField(auto_now=True)),
                ('tcc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tcc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Convite',
        ),
        migrations.DeleteModel(
            name='StatusTCC',
        ),
    ]
