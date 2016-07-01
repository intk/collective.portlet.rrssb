import random

from AccessControl import getSecurityManager

from zope.interface import implements
from zope.component import getMultiAdapter, getUtility

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form

from plone.memoize.instance import memoize

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
#from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue

from plone.i18n.normalizer.interfaces import IIDNormalizer

from Products.CMFCore.utils import getToolByName
from datetime import date
from DateTime import DateTime
import time

from collective.portlet.rrssb import PloneMessageFactory as _

from Acquisition import aq_inner
from z3c.form import form, field, button, group
from plone.app.z3cform.layout import wrap_form
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone.utils import getFSVersionTuple

PLONE5 = getFSVersionTuple()[0] >= 5

if PLONE5:
    base_AddForm = base.AddForm
    base_EditForm = base.EditForm
else:
    from plone.app.portlets.browser.z3cformhelper import AddForm as base_AddForm  # noqa
    from plone.app.portlets.browser.z3cformhelper import EditForm as base_EditForm  # noqa
    from z3c.form import field

class IRRSSBPortlet(IPortletDataProvider):
    """A portlet that renders the Ridiculously Responsive Social Sharing Buttons
    """
    render_email = schema.Bool(
        title=_(u"render_email", default=u"Email"),
        required=False)
    
    render_facebook = schema.Bool(
        title=_(u"render_facebook", default=u"Facebook"),
        default=False,
        required=False)

    render_twitter = schema.Bool(
        title=_(u"render_twitter", default=u"Twitter"),
        default=False,
        required=False)
    
    render_linkedin = schema.Bool(
        title=_(u"render_linkedin", default=u"Linkedin"),
        default=False,
        required=False)

    render_googleplus = schema.Bool(
        title=_(u"render_googleplus", default=u"Google +"),
        required=False)
    
    render_pinterest = schema.Bool(
        title=_(u"render_pinterest", default=u"Pinterest"),
        default=False,
        required=False)

    render_tumblr = schema.Bool(
        title=_(u"render_tumblr", default=u"Tumblr"),
        required=False)

class Assignment(base.Assignment):
    """
    Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """
    implements(IRRSSBPortlet)
    render_email = False
    render_facebook = False
    render_linkedin = False
    render_twitter = False
    render_googleplus = False
    render_youtube = False
    render_pinterest = False
    render_tumblr = False
    
    def __init__(self, render_email = False, render_facebook = False, render_instagram = False, render_linkedin = False, render_twitter = False, render_googleplus = False, render_youtube = False, render_pinterest = False, render_tumblr = False):
        self.render_email = render_email
        self.render_facebook = render_facebook
        self.render_instagram = render_instagram
        self.render_linkedin = render_linkedin
        self.render_twitter = render_twitter
        self.render_googleplus = render_googleplus
        self.render_youtube = render_youtube
        self.render_pinterest = render_pinterest
        self.render_tumblr = render_tumblr
        
        
    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave or
        static string if title not defined.
        """
        return _(u'rrssb_portlet', default=u"RRSSB Portlet")

class Renderer(base.Renderer):

    _template = ViewPageTemplateFile('rrssb.pt')
    render = _template

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    @property
    def available(self):
        return True
    
    def css_class(self):
        return "portlet-rrssb"
    
    def getTitle(self):
        if self.data.header:
            return self.data.header
        else:
            return DateTime().strftime("%A %d %B %Y")
    
    def render_email(self):
        return self.data.render_email

    def render_facebook(self):
        return self.data.render_facebook

    def render_linkedin(self):
        return self.data.render_linkedin

    def render_twitter(self):
        return self.data.render_twitter

    def render_googleplus(self):
        return self.data.render_googleplus

    def render_pinterest(self):
        return self.data.render_pinterest

    def render_tumblr(self):
        return self.data.render_tumblr

class AddForm(base_AddForm):
    if PLONE5:
        schema = IRRSSBPortlet
    else:
        fields = field.Fields(IRRSSBPortlet)

    label = _(u"Add RRSSB portlet")
    description = _(u"This portlet renders the Ridiculously Responsive Social Sharing Buttons.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base_EditForm):
    if PLONE5:
        schema = IRRSSBPortlet
    else:
        fields = field.Fields(IRRSSBPortlet)

    label = _(u"Edit RRSSB portlet")
    description = _(u"This portlet renders the Ridiculously Responsive Social Sharing Buttons.")


