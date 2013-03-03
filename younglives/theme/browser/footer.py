# Zope
from Acquisition import aq_inner, aq_parent
from zope.component import getMultiAdapter

# Plone
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.navigation.root import getNavigationRoot
from plone.memoize.view import memoize
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.CMFCore.utils import getToolByName

from younglives.homepage.interfaces import IHomePage

class FooterViewlet(ViewletBase):
    """ Footer viewlet """

    def isHomepage(self):
        if IHomePage.providedBy(self.context):
            return True
        return False

    @memoize
    def getHomePage(self):
        """ For other sites - get homepage and use it's settings """
        catalog = getToolByName(self.context, 'portal_catalog')
        homepages = catalog.searchResults(object_provides = IHomePage.__identifier__)
        if homepages:
            return homepages[0].getObject()
        return None
    
    def boxes(self):
        homepage = self.getHomePage()
        if homepage is None:
            # don't blow up if there is no hompage
            return
        wtool = getToolByName(self.context, 'portal_workflow')
        results = []
        for box in ["1","2","3"]:
            links = eval("homepage.getBox%sLinks()" % box) or []
            results.append( dict(
                title = eval("homepage.getBox%sTitle" % box),
                description = eval("homepage.getBox%sDescription" % box),
                image = eval("homepage.getBox%sImage" % box),
                links = [{'title':x.Title,'url':x.absolute_url} for x in links],))
        return results

    def footer_image(self):
        homepage = self.getHomePage()
        try:
            return homepage.getHomeFooterImage()
        except AttributeError:
            return None
