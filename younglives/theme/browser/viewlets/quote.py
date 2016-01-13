from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets import ViewletBase


class QuoteView(ViewletBase):

    index = ViewPageTemplateFile("quote.pt")

    def update(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        results = portal_catalog(meta_type='HomePage')
        if results:
            object = results[0].getObject()
            #self.quote = object.getField('homeQuote').get(object)
        else:
            self.quote = ''
