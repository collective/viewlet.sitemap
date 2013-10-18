
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SitemapViewlet(ViewletBase):

    index = ViewPageTemplateFile('templates/sitemap.pt')
    item_template = ViewPageTemplateFile('templates/sitemap-item.pt')

    def available(self):
        return True

    def createSiteMap(self):
        context = aq_inner(self.context)
        view = getMultiAdapter((context, self.request),
                               name='sitemap_builder_view')
        data = view.siteMap()
        return self._renderLevel(children=data.get('children', []))

    def _renderLevel(self, children=[], level=2):
        output = ''
        for node in children:
            grandchildren = node.get('children', [])
            if len(grandchildren):
                node['dropdown'] = True
                output += '<li class="dropdown">\n'
            else:
                node['dropdown'] = False
                output += '<li class="">\n'
            output += self.item_template(node=node) 
            
            if len(grandchildren):
                output += \
                    '<ul class="dropdown-menu level%d">\n%s\n</ul>\n' % (
                        level, self._renderLevel(grandchildren, level+1))
                
            output += '</li>\n'
        return output

#EOF
