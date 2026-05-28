import unittest
from bin_tree import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    def test_default_tree(self):
        tree = gen_bin_tree()
        self.assertIsInstance(tree, dict)
        self.assertEqual(tree["root"], 1)
        self.assertEqual(tree["left"]["root"], 2)
        self.assertEqual(tree["right"]["root"], 4)

    def test_custom_parameters(self):
        tree = gen_bin_tree(height=3, root=10)
        self.assertEqual(tree["root"], 10)
        self.assertEqual(tree["left"]["root"], 20)
        self.assertEqual(tree["right"]["root"], 13)

    def test_leaf_level(self):
        tree = gen_bin_tree(height=2, root=5)
        self.assertEqual(tree["left"], 10)
        self.assertEqual(tree["right"], 8)

    def test_height_one(self):
        self.assertEqual(gen_bin_tree(height=1, root=7), 7)

    def test_invalid_height(self):
        self.assertIsNone(gen_bin_tree(height=0, root=1))
        self.assertIsNone(gen_bin_tree(height=-3, root=1))


if __name__ == "__main__":
    unittest.main()