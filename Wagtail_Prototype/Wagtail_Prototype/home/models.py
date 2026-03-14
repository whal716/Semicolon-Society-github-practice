from django.db import models
from wagtail.admin import blocks
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail import blocks
from wagtail.fields import StreamField


class CourseCircleBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    background_color = blocks.CharBlock(help_text="e.g. #f7b7a3")

    class Meta:
        template = "blocks/course_circle.html"


class HomePage(Page):
    quote = models.TextField(blank=True)
    quote_author = models.CharField(max_length=255, blank=True)
    button_text = models.CharField(max_length=50, default="About EmpowerME")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    courses_section = StreamField([
        ('course_circle', CourseCircleBlock()),
    ], use_json_field=True, null=True, blank=True)



    content_panels = Page.content_panels + [
        FieldPanel('courses_section'),
        FieldPanel('quote'),
        FieldPanel('quote_author'),
        FieldPanel('button_text'),
        FieldPanel('hero_image')
    ]