import unittest
from typing import Dict, List

def gen_bin_tree(
    height: int = 3,
    root: int = 2
) -> Dict[str, list]:
    """
    Рекурсивно генерирует бинарное дерево в виде словаря.

    Параметры:
    height : int
        Высота дерева. Если 0, возвращается лист без потомков.
    root : int
        Значение текущего узла дерева.

    Возвращает:
    Dict[str, list]
        Дерево в виде словаря, где ключ — значение узла, 
        а значение — список из двух дочерних деревьев (левое и правое).

    Формулы для потомков:
    - Левый потомок = root * 3
    - Правый потомок = root + 5
    """
    if height == 0:
        return {str(root): []}

    left_subtree = gen_bin_tree(height - 1, root * 3)
    right_subtree = gen_bin_tree(height - 1, root + 5)
    
    return {str(root): [left_subtree, right_subtree]}


class TestGenBinTree(unittest.TestCase):
    
    def test_height_1(self):
        expected = {'2': [{'6': []}, {'7': []}]}  # левый = 2*3=6, правый = 2+5=7
        result = gen_bin_tree(1, 2)
        self.assertEqual(result, expected)
    
    def test_height_2(self):
        expected = {
            '2': [
                {'6': [{'18': []}, {'11': []}]}, 
                {'7': [{'21': []}, {'12': []}]}
            ]
        }
        result = gen_bin_tree(2, 2)
        self.assertEqual(result, expected)
    
    def test_height_3(self):
        expected = {
            '2': [
                {'6': [{'18': [{'54': []}, {'23': []}]}, {'11': [{'33': []}, {'16': []}]}]}, 
                {'7': [{'21': [{'63': []}, {'26': []}]}, {'12': [{'36': []}, {'17': []}]}]}
            ]
        }
        result = gen_bin_tree(3, 2)
        self.assertEqual(result, expected)


unittest.main(argv=[''], verbosity=2, exit=False)
