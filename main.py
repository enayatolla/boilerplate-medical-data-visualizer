# This file is used for development and local testing
import medical_data_visualizer
import unittest

# Test your functions by calling them to generate figures
print("Generating Categorical Plot...")
medical_data_visualizer.draw_cat_plot()

print("Generating Heat Map...")
medical_data_visualizer.draw_heat_map()

# Run the automated assertions
print("\nRunning Unit Tests:")
unittest.main(module='test_module', exit=False)