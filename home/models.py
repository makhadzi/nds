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

PROVINCE_LIMPOPO = 'limpopo'
PROVINCE_GAUTENG = 'gauteng'
PROVINCE_MPUMALANGA = 'mpumalanga'
PROVINCE_NORTH_WEST = 'northwest'
PROVINCE_KWAZULU_NATAL = 'kwazulunatal'
PROVINCE_EASTERN_CAPE = 'easterncape'
PROVINCE_WESTERN_CAPE = 'westerncape'
PROVINCE_NORTHERN_CAPE = 'northerncape'
PROVINCE_FREE_STATE = 'freestate'

PROVINCES = (
    (PROVINCE_EASTERN_CAPE, 'Eastern Cape'),
    (PROVINCE_FREE_STATE, 'Free State'),
    (PROVINCE_GAUTENG, 'Gauteng'),
    (PROVINCE_KWAZULU_NATAL, 'Kwazulu Natal'),
    (PROVINCE_LIMPOPO, 'Limpopo'),
    (PROVINCE_MPUMALANGA, 'Mpumalanga'),
    (PROVINCE_NORTH_WEST, 'North West'),
    (PROVINCE_NORTHERN_CAPE, 'Northern Cape'),
    (PROVINCE_WESTERN_CAPE, 'Western Cape'),
)


class Main(Page):
    parent_page_types = []


class Section(Page):
    subpage_types = ['home.Section', 'home.NewsEvent']


class NewsEventTag(TaggedItemBase):
    content_object = ParentalKey('home.NewsEvent', related_name='tagged_items')


class NewsEvent(Page, TagSearchable):
    parent_page_types = ['home.Section']
    subpage_types = []

    date_start = models.DateField(_("Start date"))
    date_end = models.DateField(
        _("End date"),
        null=True,
        blank=True,
        help_text=_("Not required if event is on a single day")
    )
    time_start = models.TimeField(_("Start time"), null=True, blank=True)
    time_end = models.TimeField(_("End time"), null=True, blank=True)
    location = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=NewsEventTag, blank=True)

    search_fields = Page.search_fields + TagSearchable.search_fields + (
        index.SearchField('location'),
        index.SearchField('body'),
    )
    province = models.CharField(
        max_length=255, choices=PROVINCES, blank=True)

NewsEvent.content_panels = [
    FieldPanel('title', classname="full title"),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('date_start'), FieldPanel('date_end')],
            classname="label-above"),
        FieldRowPanel([
            FieldPanel('time_start'), FieldPanel('time_end')],
            classname="label-above")],
        _("Date & Time")),
    FieldPanel('tags'),
    FieldPanel('location'),
    FieldPanel('province'),
    FieldPanel('body', classname="full"),
]
