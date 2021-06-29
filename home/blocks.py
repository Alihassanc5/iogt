from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class MediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <div>
                <video width="320" height="240" controls>
                    {0}
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <audio controls>
                    {0}
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''

        return format_html(player_code, format_html_join(
            '\n', "<source{0}>",
            [[flatatt(s)] for s in value.sources]
        ))


class SocialMediaLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    link = blocks.URLBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = 'site'


class SocialMediaShareButtonBlock(blocks.StructBlock):
    platform = blocks.CharBlock(max_length=255)
    is_active = blocks.BooleanBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'site'


class PageButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=False, max_length=255)
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'blocks/page_button.html'
