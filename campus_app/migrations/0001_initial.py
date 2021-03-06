# Generated by Django 2.2.2 on 2019-07-06 00:03

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
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('palavras_chave', models.CharField(max_length=200, null=True)),
                ('resumo', models.CharField(max_length=300, null=True)),
                ('texto', models.CharField(max_length=600)),
                ('prioridade', models.IntegerField(default=0)),
                ('link_externo', models.CharField(max_length=300, null=True)),
                ('link_foto', models.CharField(max_length=300, null=True)),
                ('link_audio', models.CharField(max_length=300, null=True)),
                ('link_video', models.CharField(max_length=300, null=True)),
                ('link_georreferenciamento', models.CharField(max_length=300, null=True)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('cod_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_noticia', to='campus_app.Usuario')),
            ],
        ),
    ]
