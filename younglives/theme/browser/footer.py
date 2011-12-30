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

# local
from younglives.content.interfaces import ISiteTabMarker, IHomePage, IHomepageBoxAware

class FooterViewlet(ViewletBase):
    """ Footer viewlet """
    
    def isHomepage(self):
        return IHomePage.providedBy(self.context)
    
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

    def getHomeBoxes(self):
        items = []
        homepage = self.getHomePage()
        
        home_boxes_ref = homepage.getHomeBoxes()
        for box_ref in home_boxes_ref:
            if IHomepageBoxAware.providedBy(box_ref):
                item = dict(title = box_ref.Title(),
                            url = box_ref.absolute_url(),
                            description = box_ref.Description(),
                            links = [])
                brains = box_ref.queryCatalog()
                for brain in brains:
                    item['links'].append(dict(title = brain.Title,
                                              url = brain.getURL(),))                            
                items.append(item)
        
        return items
