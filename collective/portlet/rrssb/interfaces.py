from zope.interface import Interface
from zope import schema

from collective.portlet.rrssb import PloneMessageFactory as _
from plone.app.textfield import RichText
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Weekday portlet" this interface must be its layer
    """

class IRRSSBContent(Interface):
    """
    This interface defines the weekdays record on the registry
    """
    
    render_email = schema.Bool(
        title=_(u"render_email", default=u"Email"),
        required=False)
    
    render_facebook = schema.Bool(
        title=_(u"render_facebook", default=u"Facebook"),
        default=False,
        required=False)
    
    render_linkedin = schema.Bool(
        title=_(u"render_linkedin", default=u"Linkedin"),
        default=False,
        required=False)
    
    render_twitter = schema.Bool(
        title=_(u"render_twitter", default=u"Twitter"),
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


    
    