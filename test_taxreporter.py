# test_taxreporter.py
"""
Tests for TaxReporter module.
"""

import unittest
from taxreporter import TaxReporter

class TestTaxReporter(unittest.TestCase):
    """Test cases for TaxReporter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TaxReporter()
        self.assertIsInstance(instance, TaxReporter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TaxReporter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
