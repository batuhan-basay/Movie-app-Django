# Generated by Django 3.2.7 on 2022-06-25 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Filmler'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Kişi', 'verbose_name_plural': 'Kişiler'},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='describe',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='bio',
            new_name='biography',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='date',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='person',
            name='duty_type',
            field=models.CharField(choices=[('1', 'Görevli'), ('2', 'Oyuncu'), ('3', 'Yönetmen'), ('4', 'Senarist')], max_length=1, verbose_name='görev'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Erkek'), ('F', 'Kadın')], max_length=1, verbose_name='cinsiyet'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='movies')),
                ('is_active', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie')),
            ],
        ),
    ]
