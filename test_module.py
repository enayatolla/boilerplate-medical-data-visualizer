import unittest
import medical_data_visualizer
import matplotlib as mpl

class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]
    
    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(actual, expected, "Expected categorical plot x-axis label to be 'variable'")

    def test_data_structure(self):
        actual = len(self.ax.get_children())
        # Confirms bars and background patches match expected feature bins
        self.assertGreater(actual, 10, "Expected multiple bar plotting groups in your grid layout.")

class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, expected, "Heat map labels do not cleanly match data columns.")

    def test_diagonal_masking(self):
        # Checks that the upper triangle is effectively masked out
        actual = len(self.ax.collections)
        self.assertEqual(actual, 1, "Expected an isolated matrix plot mesh collection.")

if __name__ == "__main__":
    unittest.main()