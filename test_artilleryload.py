# test_artilleryload.py
"""
Tests for ArtilleryLoad module.
"""

import unittest
from artilleryload import ArtilleryLoad

class TestArtilleryLoad(unittest.TestCase):
    """Test cases for ArtilleryLoad class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtilleryLoad()
        self.assertIsInstance(instance, ArtilleryLoad)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtilleryLoad()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
