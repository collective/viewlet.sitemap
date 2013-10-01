# -*- coding: utf-8 -*-
import unittest

from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_ID, setRoles
from collective.viewlet.sitemap.testing import \
    VIEWLET_SITEMAP_INTEGRATION_TESTING

PACKAGE_NAME = 'collective.viewlet.sitemap'


class ViewletSitemapTest(unittest.TestCase):

    layer = VIEWLET_SITEMAP_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.quick_installer = getToolByName(self.portal,
                                             'portal_quickinstaller')
        self.portal_setup = getToolByName(self.portal,
                                          'portal_setup')

    def test_installable(self):
        self.failUnless(PACKAGE_NAME in
                        self.quick_installer.listInstallableProfiles())
        self.quick_installer.installProduct(PACKAGE_NAME)
        installed = [x for x in self.quick_installer.listInstalledProducts() if
                     x.get('id') == PACKAGE_NAME]
        self.failUnless(installed and isinstance(installed, list) and
                        len(installed))
        installed = installed[0]
        self.failUnless(installed and installed.get('status') == 'installed')


#EOF
