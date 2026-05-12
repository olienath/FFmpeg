# test_ffmpegbuild.py
"""
Tests for FFmpegBuild module.
"""

import unittest
from ffmpegbuild import FFmpegBuild

class TestFFmpegBuild(unittest.TestCase):
    """Test cases for FFmpegBuild class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FFmpegBuild()
        self.assertIsInstance(instance, FFmpegBuild)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FFmpegBuild()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
