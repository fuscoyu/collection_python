import unittest

from unittest.mock import patch

# from src.context import DemoContext
from ..src import context

class TestDemoContext(unittest.TestCase):

    @patch("src.context")
    def test_mock_demo_context(self):
        ctx = context.instance()
