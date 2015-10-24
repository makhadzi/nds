from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.taggable import TagSearchable
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, FieldRowPanel)


class Main(Page):
    parent_page_types = []


class Section(Page):
    subpage_types = ['home.Section', 'home.NewsEvent']


class NewsEventTag(TaggedItemBase):
    content_object = ParentalKey('home.NewsEvent', related_name='tagged_items')


class NewsEvent(Page, TagSearchable):
    parent_page_types = ['home.Section']
    subpage_types = []

    date_start = models.DateField("Start date")
    date_end = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if event is on a single day"
    )
    time_start = models.TimeField("Start time", null=True, blank=True)
    time_end = models.TimeField("End time", null=True, blank=True)
    location = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=NewsEventTag, blank=True)
    repeat_annually = models.BooleanField(
        default=False,
        help_text=_("Is this an annual event?"))

    search_fields = Page.search_fields + TagSearchable.search_fields + (
        index.SearchField('location'),
        index.SearchField('body'),
    )

NewsEvent.content_panels = [
    FieldPanel('title', classname="full title"),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('date_start'), FieldPanel('date_end')],
            classname="label-above"),
        FieldRowPanel([
            FieldPanel('time_start'), FieldPanel('time_end')],
            classname="label-above")],
        "Date & Time"),
    FieldRowPanel([FieldPanel('repeat_annually')], classname="label-above"),
    FieldPanel('tags'),
    FieldPanel('location'),
    FieldPanel('body', classname="full"),
]
