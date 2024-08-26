



import unittest
from powerreviews_backend_test import (
    initialize_items_available,
    sort_items_by_weight,
    add_initial_items,
    fill_remaining_capacity,
    pack_food_backpack,
)

class TestPackFoodBackpack(unittest.TestCase):
    def test_pack_food_backpack(self):
        # Test with bag capacity 27
        bag_capacity = 27
        expected = [
            {"item": "Bag of Apples", "count": 4},
            {"item": "Trail Mix", "count": 1},
            {"item": "Peanut Butter", "count": 1},
            {"item": "Bread", "count": 2},  # Updated to 2 based on logic
        ]
        result = pack_food_backpack(bag_capacity)
        self.assertEqual(result, expected)

        # Test with bag capacity 38
        bag_capacity = 38
        expected = [
            {"item": "Bag of Apples", "count": 6},
            {"item": "Trail Mix", "count": 1},
            {"item": "Peanut Butter", "count": 2},
            {"item": "Bread", "count": 1},
        ]
        result = pack_food_backpack(bag_capacity)
        self.assertEqual(result, expected)

        # Test with bag capacity 15
        bag_capacity = 15
        expected = [
            {"item": "Bag of Apples", "count": 1},
            {"item": "Trail Mix", "count": 2},
            {"item": "Peanut Butter", "count": 1},
            {"item": "Bread", "count": 2},
        ]
        result = pack_food_backpack(bag_capacity)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()





