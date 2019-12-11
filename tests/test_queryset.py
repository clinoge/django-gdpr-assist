try:
    from unittest import mock
except ImportError:
    import mock

from django.apps import apps
from django.db import models
from django.test import TestCase

import gdpr_assist
from gdpr_assist.apps import GdprAppConfig
from gdpr_assist.registry import registry
from gdpr_assist.models import (
    PrivacyMeta,
    PrivacyModel,
    PrivacyManager,
    PrivacyQuerySet,
)

from .gdpr_assist_tests_app.models import (
    ModelWithCustomManager,
    ModelWithCustomManagerQuerySet,
)

from .gdpr_assist_tests_app.models import (
    ModelWithPrivacyMeta,
    ModelWithoutPrivacyMeta,
)

class TestCustomManagerOnly(TestCase):
    def test_casts_manager(self):
        self.assertTrue(
            issubclass(ModelWithCustomManager.objects.__class__, PrivacyManager)
        )


class TestCustomQuerySet(TestCase):
    def test_casts_manager(self):
        self.assertTrue(
            issubclass(ModelWithCustomManagerQuerySet.objects.__class__, PrivacyManager)
        )
    def test_casts_queryset(self):
        self.assertTrue(
            issubclass(ModelWithCustomManagerQuerySet.objects.all().__class__, PrivacyQuerySet)
        )
