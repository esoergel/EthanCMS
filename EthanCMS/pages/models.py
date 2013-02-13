from django.db import models
import markdown

"""
{{page.parent}}
{{page.body_html}}
{{page.created}}
{{page.modified}}
{{page.url}}

{{page.title}}
{{page.sub_title}}

{{page.body}}
{{page.slug}}
{{page.tags}}
"""

class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    # auto generated
    parent = models.ForeignKey("Page", blank=True, null=True,
        related_name="children")
    body_html = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)

    # basic options
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    # advanced options
    slug = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    template = models.CharField(max_length=150, default="default.html")

    def __unicode__(self):
        return self.url

    def save(self):
        self.body_html = markdown.markdown(self.body)
        self.url = self.get_url()
        super(Page, self).save()

    def get_url(self):
        if self.parent:
            print u"%s has a parent %s." % (self.title, self.parent)
            base = self.parent.url()
            return u"%s/%s" % (base, self.slug)
        else:
            print u"%s has no parent." % (self.title)
            return u"/%s/" % self.slug

# class Page(models.Model):
#     parent = models.ForeignKey("Page", blank=True, null=True,
#         related_name="children")
#     title = models.CharField(max_length=150)
#     sub_title = models.CharField(max_length=150, blank=True, null=True)
#     page_type = models.CharField(max_length=150, blank=True, null=True)
#     slug = models.CharField(max_length=100, blank=True, null=True)

#     def __unicode__(self):
#         return self.title


# class ContentPage(Page):
#     body = models.TextField()
#     body_html = models.TextField(blank=True, null=True)
#     created = models.DateTimeField('date created', auto_now_add=True)
#     modified = models.DateTimeField('date modified', auto_now=True)
#     tags = models.ManyToManyField(Tag, blank=True, null=True)

#     def save(self):
#         self.body_html = markdown.markdown(self.body)
#         super(BlogEntry, self).save()
