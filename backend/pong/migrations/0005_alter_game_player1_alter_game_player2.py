# Generated by Django 5.1.2 on 2024-11-18 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0004_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to='pong.player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to='pong.player'),
        ),
    ]
