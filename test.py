# import unittest
# import json
# from lab5 import pound
# # from insertion import insertion_sort
# # from algo.mergesort import merge_sort
# # from algo.binary import binary_search

# class MyTest(unittest.TestCase):

#     def setUp(self) -> None:

#         '''
#         # self.test = []
#         # self.answers = []
#         # with open("test.txt", "r") as file:
#         #     for line in file:
#         #         parts = line.strip().split("   ")
#         #         if len(parts) == 2:
#         #             self.test.append(int(parts[0]))
#         #             self.answers.append(int(parts[1]))
    
#         # print("TEST CASE HAS STARTED.")
#         # def tearDown(self) -> None:
        
#         #     print("TEST CASE HAS ENDED.")

#         # def insertionSort(self):

#         #     for i, q in zip(self.test, self.answers):
#         #         self.assertEqual(insertion_sort(i), q)
        
#         # def mergeSort(self):

#         #     for i, q in zip(self.test, self.answers):
#                 # self.assertEqual(merge_sort(i), q)
        
#         # def binarySearch(self):

#         #     for i in range(20):
#         #         self.assertEqual(binary_search(self.sortArray[i], 0, len(self.sortArray[i]), self.targets[i]), self.sortArray[i].index(self.targets[i]))
#         '''
#         with open('test5.json', 'r') as file:
#             self.test_cases = json.load(file)['test_cases5']
#         print("hahaa")
        
    
    
#     def lab5(self):

#         for case in self.test_cases:
#             self.assertEqual(pound(case['input'][0], case["input"][1]), case["expected"])


# unittest.main(verbosity=2)


import unittest
import json
from lab5 import pound
from lab5 import optimal_bst
from lab5 import fractional_knapsack
from lab8 import coinChange

class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('test5.json', 'r') as file:
            self.test_cases = json.load(file)['test_cases5']
        
        with open('test5.json', 'r') as file:
            self.test_cases2 = json.load(file)['test_cases6']
        
        with open('test5.json', 'r') as file:
            self.test_cases3 = json.load(file)['test_cases7']
        
        with open('test5.json', 'r') as file:
            self.test_cases4 = json.load(file)['test_cases8']
        
        print("Setup complete, test cases loaded.")

    def test_lab5(self):
        for case in self.test_cases:
            input_data = case['input']
            expected = case['expected']
            self.assertEqual(pound(input_data[0], input_data[1]), expected)
            print("Test loaded.")
    
    def test_lab6(self):
        for case in self.test_cases2:
            self.assertEqual(optimal_bst(case["keys"], case["freq"], len(case["keys"])), case["expected"])
    
    def test_lab7(self):
        for case in self.test_cases3:
            self.assertEqual(fractional_knapsack(case["goods"], case["pound"]), case["expected"])
    
    def test_lab8(self):
        for case in self.test_cases4:
            self.assertEqual(coinChange(case["keys"], case["amount"]), case["answer"])
    

unittest.main()

