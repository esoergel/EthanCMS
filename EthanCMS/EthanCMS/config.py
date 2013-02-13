import os

SITE_NAME = 'esoergel.com'
DEFAULT_TEMPLATE = 'default.html'

# Tuple of fields that should be editable
EDITABLE_PAGE_FIELDS = ('title', 'sub_title', 'body', 'slug', 'tags',)
MARKDOWN_INPUT = 'body'
MARKDOWN_OUTPUT = 'body_html'

# Gallery Stuff
IMAGE_ROOT = os.getcwdu() + '/static/gallery/'
GALLERY_DISPLAY_ROOT = '/static/gallery/'
CMS_ROOT = '/content/'


# This dictionary will be available in templates called with
# ContentMixin under {{content.<key>}}
CONTEXT_DICT = {
    'cms_root': CMS_ROOT,
    'gallery_display_root': GALLERY_DISPLAY_ROOT,
    'site_name': SITE_NAME,
}

class ContentMixin(object):
    """
    Adds 'CONTEXT_DICT' to context under the name 'content'
    """
    def get_context_data(self, **kwargs):
        print kwargs
        context = super(ContentMixin, self).get_context_data(**kwargs)
        context['content'] = CONTEXT_DICT
        context['request'] = self.request
        context['params'] = kwargs
        return context




