

import unittest

from problem_1 import print_depth
from problem_2 import print_depth_2
from problem_2 import Person
from problem_3 import lca, Node

node_1 = Node(1, None)
node_2 = Node(2, node_1)
node_3 = Node(3, node_1)
node_4 = Node(4, node_2)
node_5 = Node(5, node_2)
node_6 = Node(6, node_3)
node_7 = Node(7, node_3)
node_8 = Node(8, node_4)
node_9 = Node(9, node_4)

a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }


        
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
b = {
        "key1": 2,
        "obj_key": person_b
}

class Test_1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(print_depth(a), "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n", "Should be 6")

class Test_2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(print_depth_2(b), "key1 1\nobj_key 1\nfirst_name 2\nlast_name 2\nfather 2\nfirst_name 3\nlast_name 3\nfather 3\n")

class Test_3(unittest.TestCase):
    def test_3_1(self):
        self.assertEqual(lca(node_9, node_5), node_2)
    def test_3_2(self):
        self.assertEqual(lca(node_8, node_5), node_2)
    def test_3_3(self):
        self.assertEqual(lca(node_8, node_4), node_4)
    def test_3_4(self):
        self.assertEqual(lca(node_3, node_7), node_3)
    def test_3_3(self):
        self.assertEqual(lca(node_6, node_1), node_1)


if __name__ == '__main__':
    unittest.main()
