"""
Test script for checking that Minkowski coordinates compile.
"""

# Modules
import scripts.utils.athena as athena

# Prepare Athena++
def prepare():
  athena.configure('gtb',
      prob='gr_shock_tube',
      coord='minkowski',
      flux='hlle')
  athena.make()

# Run Athena++
def run():
  pass

# Analyze outputs
def analyze():
  return True
