#-*- encoding: utf-8 -*-
from typing import List


class Family:
    def __init__(self, father_name: str, mother_name: str, offspring: List['Family']):
        self.father_name = father_name
        self.mother_name = mother_name
        self.offspring = offspring

    def jsonf(self):
        '''
        递归
        :param data:
        :return:
        '''
        res = {}
        res['FatherName'] = self.father_name
        res['MotherName'] = self.mother_name
        res['offspring'] = []
        print(self.offspring)
        if len(self.offspring) > 0:
            pass


# example:

# Input
parent = Family('Carol', 'Dan', [
    Family('Alice', 'Bob', []),
    Family('Eve', 'Dave', [
        Family('Grace', 'Harry', []),
        Family('Ivy', 'John', []),
    ]),
])

parent.jsonf()


# Expected Output
res = {
    "FatherName": "Carol",
    "MotherName": "Dan",
    "OffSpring": [
        {
            "FatherName": "Alice",
            "MotherName": "Bob",
            "OffSpring": []
        },
        {
            "FatherName": "Eve",
            "MotherName": "Dave",
            "OffSpring": [
                {
                    "FatherName": "Grace",
                    "MotherName": "Harry",
                    "OffSpring": []
                },
                {
                    "FatherName": "Ivy",
                    "MotherName": "John",
                    "OffSpring": []
                }
            ]
        }
    ]
}