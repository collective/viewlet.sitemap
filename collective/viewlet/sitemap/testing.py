from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting, FunctionalTesting
from zope.configuration import xmlconfig


class PortletMailman(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.viewlet.sitemap
        xmlconfig.file('configure.zcml',
                       collective.viewlet.sitemap,
                       context=configurationContext)


VIEWLET_SITEMAP_FIXTURE = PortletMailman()
VIEWLET_SITEMAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VIEWLET_SITEMAP_FIXTURE,),
    name="SitemapViewlet:Integration")
VIEWLET_SITEMAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VIEWLET_SITEMAP_FIXTURE,),
    name="SitemapViewlet:Functional")
