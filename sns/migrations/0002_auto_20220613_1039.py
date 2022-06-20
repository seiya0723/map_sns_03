# Generated by Django 3.2.12 on 2022-06-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
            ],
        ),
        migrations.AddField(
            model_name='park',
            name='tag',
            field=models.ManyToManyField(to='sns.Tag', verbose_name='タグ'),
        ),
    ]
