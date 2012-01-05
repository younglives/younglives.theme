from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets import ViewletBase

class DocumentActionsViewlet(ViewletBase):

    index = ViewPageTemplateFile("document_actions.pt")

    def update(self):
        super(DocumentActionsViewlet, self).update()

        self.context_state = getMultiAdapter((self.context, self.request),
                                             name=u'plone_context_state')
        self.actions = self.context_state.actions('document_actions')
