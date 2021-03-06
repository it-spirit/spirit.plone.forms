# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from spirit.plone.forms.testing import INTEGRATION_TESTING

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that spirit.plone.forms is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if spirit.plone.forms is installed."""
        self.assertTrue(self.installer.is_product_installed("spirit.plone.forms"))

    def test_browserlayer(self):
        """Test that ISpiritPloneFormsLayer is registered."""
        from plone.browserlayer import utils
        from spirit.plone.forms.interfaces import ISpiritPloneFormsLayer

        self.assertIn(ISpiritPloneFormsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("spirit.plone.forms")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if spirit.plone.forms is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("spirit.plone.forms"))

    def test_browserlayer_removed(self):
        """Test that ISpiritPloneFormsLayer is removed."""
        from plone.browserlayer import utils
        from spirit.plone.forms.interfaces import ISpiritPloneFormsLayer

        self.assertNotIn(ISpiritPloneFormsLayer, utils.registered_layers())
