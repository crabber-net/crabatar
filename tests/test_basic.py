from .context import crabatar
import pytest

class TestModels:
    def test_sample_class(self):
        assert 'pigs' != 'flying'
        sample_instance = crabatar.SampleClass
        assert sample_instance is not None
