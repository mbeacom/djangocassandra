"""
    This file tests the sorting performance of the djangocassandra back end.

    Tests are implemented for the following features:
        - Verifying that no sort is applied to already sorted data, when properly queried.
        - Verifying that this data is properly sorted.
        - Verifying that only minimal sorting is applied to partially sorted data, when properly queried.
        - Verifying that this data is properly sorted.
        - Verify that the djangocassandra backend raises proper warnings for unaccelerated sorts.
        - Verifying that the djangocassandra correctly sorts data in the unaccelerated case.
"""

from unittest import TestCase

class TestFullOrderingMatch(TestCase):

    def test_correct_sort_application(self):
        pass

    def test_correct_sort_results(self):
        pass



class TestPartialOrderingMatch(TestCase):

    def test_correct_sort_application(self):
        pass

    def test_correct_sort_results(self):
        pass

class TestDefaultSort(TestCase):

    def test_for_warnings(self):
        pass

    def test_correct_sort_results(self):
        pass
