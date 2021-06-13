# Generated by Django 3.1.12 on 2021-06-13 16:50

import django.db.models.deletion
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0059_apply_collection_ordering"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("votes", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Choice",
                "verbose_name_plural": "Choices",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PollIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "description",
                    wagtail.core.fields.StreamField(
                        [
                            ("paragraph", wagtail.core.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "thank_you_text",
                    wagtail.core.fields.StreamField(
                        [
                            ("paragraph", wagtail.core.blocks.RichTextBlock()),
                            ("media", home.blocks.MediaBlock(icon="media")),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "thank_you_link_text",
                    models.CharField(
                        blank=True,
                        default="Check more",
                        help_text="Text to be linked",
                        max_length=40,
                        null=True,
                    ),
                ),
                (
                    "thank_you_external_link",
                    models.URLField(
                        blank=True,
                        help_text="Optional external link to which user after questions can go e.g., https://www.google.com",
                        null=True,
                    ),
                ),
                (
                    "allow_anonymous_submissions",
                    models.BooleanField(
                        default=False,
                        help_text="Check this to allow users who are NOT logged in to complete surveys.",
                    ),
                ),
                (
                    "show_results",
                    models.BooleanField(
                        default=True,
                        help_text="This option allows the users to see the results.",
                    ),
                ),
                (
                    "result_as_percentage",
                    models.BooleanField(
                        default=True,
                        help_text="If not checked, the results will be shown as a total instead of a percentage.",
                    ),
                ),
                (
                    "allow_multiple_choice",
                    models.BooleanField(
                        default=False,
                        help_text="Allows the user to choose more than one option.",
                    ),
                ),
                (
                    "randomise_options",
                    models.BooleanField(
                        default=False,
                        help_text="Randomising the options allows the options to be shown in a different order each time the page is displayed.",
                    ),
                ),
                (
                    "thank_you_internal_link",
                    models.ForeignKey(
                        blank=True,
                        help_text="Optional page to which user after questions can go",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="question",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Poll",
                "verbose_name_plural": "Polls",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ChoiceVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("submission_date", models.DateField(auto_now_add=True, null=True)),
                (
                    "choice",
                    models.ManyToManyField(blank=True, to="questionnaires.Choice"),
                ),
                (
                    "poll",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="questionnaires.poll",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="choice_votes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="choice",
            name="choice_votes",
            field=models.ManyToManyField(
                blank=True, related_name="choices", to="questionnaires.ChoiceVote"
            ),
        ),
    ]
