# Generated by Django 4.0.3 on 2022-03-10 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.migrations.operations.special
import django.db.models.deletion


def seed_emotions(apps, _):
    """Inserts default sensations that the app should start with."""
    emotion_model = apps.get_model("body.Emotion")
    emotions = (
        "Surprised",
        "Aroused",
        "Annoyed",
        "Excited",
        "Delighted",
        "Enthusiastic",
        "Glad",
        "Joyful",
        "Content",
        "Serene",
        "At ease",
        "Relaxed",
        "Calm",
        "Irritable",
        "Sleepy",
        "Tired",
        "Bored",
        "Gloomy",
        "Miserable",
        "Depressed",
        "Disgusted",
        "Frustrated",
        "Tense",
        "Afraid",
        "Astonished",
        "Alarmed",
        "Fearful",
        "Angry",
    )

    emotion_model.objects.bulk_create([emotion_model(name=name) for name in emotions])


def seed_body_areas(apps, _):
    """Inserts default body areas that the app should start with."""
    body_area_model = apps.get_model("body.BodyArea")
    body_areas = (
        ("Neck", "cm"),
        ("Shoulders", "cm"),
        ("Bust", "cm"),
        ("Under bust", "cm"),
        ("Waist", "cm"),
        ("Hips", "cm"),
        ("Thighs", "cm"),
        ("Knees", "cm"),
        ("Calves", "cm"),
        ("Feet", "cm"),
        ("Upper arms", "cm"),
        ("Forearms", "cm"),
    )

    body_area_model.objects.bulk_create(
        [body_area_model(name=name, measurement_unit=unit) for name, unit in body_areas]
    )


def seed_categories(apps, _):
    """Inserts default categories that the app should start with."""
    category_model = apps.get_model("body.Category")
    categories = (
        "Work & Career",
        "Social & Friendship",
        "Health & Fitness",
        "Travel & Experiences",
        "Financial & Organisational",
        "Habits & Goals",
    )

    category_model.objects.bulk_create(
        [category_model(name=name) for name in categories]
    )


def seed_sensations(apps, _):
    """Inserts default sensations that the app should start with."""
    sensation_model = apps.get_model("body.Sensation")
    sensations = (
        "Tingling",
        "Sensitive",
        "Sore",
        "Smarting",
        "Pleasurable",
        "Hot",
        "Cold",
        "Stiff",
        "Dry",
        "Sweaty",
        "Numb",
        "Itchy",
        "Irritable",
    )

    sensation_model.objects.bulk_create(
        [sensation_model(name=name) for name in sensations]
    )


def seed_attributes(apps, _):
    """Inserts default sensations that the app should start with."""
    attribute_model = apps.get_model("body.Attribute")
    attributes = (
        "After exercise",
        "After big meal",
        "Feeling bloated",
    )

    attribute_model.objects.bulk_create(
        [attribute_model(name=name) for name in attributes]
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BodyArea",
            options={"ordering": ["name"], "db_table": "bodyarea"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("measurement_unit", models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            options={
                "ordering": ["-when"],
                "db_table": "report",
                "unique_together": {("user", "when")},
            },
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("when", models.DateField()),
                (
                    "weight_in_kg",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Weight (kg)",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sensation",
            options={"ordering": ["name"], "db_table": "sensation"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="BodyImage",
            options={"db_table": "bodyimage"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("notes", models.CharField(blank=True, max_length=500)),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.report",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
            options={
                "ordering": ["body_area"],
                "db_table": "entry",
                "unique_together": {("report", "body_area")},
            },
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "measurement",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("notes", models.CharField(blank=True, max_length=500)),
                (
                    "body_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="body.bodyarea"
                    ),
                ),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.report",
                    ),
                ),
                (
                    "sensations",
                    models.ManyToManyField(blank=True, to="body.sensation"),
                ),
            ],
        ),
        migrations.RunPython(
            code=seed_body_areas,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.RunPython(
            code=seed_sensations,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name="Attribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["name"], "db_table": "attribute"},
        ),
        migrations.AddField(
            model_name="report",
            name="attributes",
            field=models.ManyToManyField(blank=True, to="body.attribute"),
        ),
        migrations.RunPython(
            code=seed_attributes,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["name"],
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("notes", models.CharField(blank=True, max_length=500)),
                ("when", models.DateTimeField()),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="body.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-when"],
                "db_table": "event",
            },
        ),
        migrations.RunPython(
            code=seed_categories,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name="Medicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("current_balance", models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                "ordering": ["name"],
                "db_table": "medicine",
            },
        ),
        migrations.CreateModel(
            name="Consumption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("when", models.DateTimeField()),
                ("quantity", models.PositiveSmallIntegerField()),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.medicine",
                    ),
                ),
            ],
            options={
                "ordering": ["-when"],
                "db_table": "consumption",
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("frequency_in_days", models.PositiveSmallIntegerField(default=1)),
                ("time", models.TimeField()),
                ("quantity", models.PositiveSmallIntegerField(default=1)),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.medicine",
                    ),
                ),
                (
                    "tolerance_mins",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (5, "5m"),
                            (10, "10m"),
                            (15, "15m"),
                            (20, "20m"),
                            (30, "30m"),
                            (45, "45m"),
                            (60, "1h"),
                            (90, "1.5h"),
                            (120, "2h"),
                        ],
                        default=30,
                        verbose_name="Tolerance (mins)",
                    ),
                ),
            ],
            options={
                "ordering": ["-end_date"],
                "db_table": "schedule",
            },
        ),
        migrations.CreateModel(
            name="LedgerEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("when", models.DateTimeField()),
                ("quantity", models.SmallIntegerField()),
                (
                    "consumption",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.consumption",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.medicine",
                    ),
                ),
            ],
            options={
                "ordering": ["-when"],
                "db_table": "ledgerentry",
            },
        ),
        migrations.CreateModel(
            name="Emotion",
            options={"ordering": ["name"], "db_table": "emotion"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="EmotionReport",
            options={"db_table": "emotionreport"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("when", models.DateTimeField()),
                ("notes", models.CharField(blank=True, max_length=200)),
                (
                    "energy_level",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmotionEntry",
            options={"db_table": "emotionentry"},
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("strength", models.PositiveSmallIntegerField()),
                ("notes", models.CharField(blank=True, max_length=200)),
                (
                    "emotion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.emotion",
                    ),
                ),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="body.emotionreport",
                    ),
                ),
            ],
        ),
        migrations.RunPython(
            code=seed_emotions,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
    ]
