# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import spirit.plone.forms


class SpiritPloneFormsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=spirit.plone.forms)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "spirit.plone.forms:default")


SPIRIT_PLONE_FORMS_FIXTURE = SpiritPloneFormsLayer()


SPIRIT_PLONE_FORMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SPIRIT_PLONE_FORMS_FIXTURE,),
    name="SpiritPloneFormsLayer:IntegrationTesting",
)


SPIRIT_PLONE_FORMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SPIRIT_PLONE_FORMS_FIXTURE,),
    name="SpiritPloneFormsLayer:FunctionalTesting",
)


SPIRIT_PLONE_FORMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SPIRIT_PLONE_FORMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="SpiritPloneFormsLayer:AcceptanceTesting",
)
