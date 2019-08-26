import unittest2

class TestInput(unittest2.TestCase):

    def test_input_reshape(self):
        """
        Each of the 6 lines of inputs contains 6 space-separated integers
        :return: a list of 6 lists, I think
        """
        testcase = """-9  -9  -9  1  1  1\n 0  -9  0  4  3  2\n -9  -9  -9  1  2  3\n 0  0  8  6  6  0\n 0  0  0  -2  0  0\n 0  0  1  2  4  0"""
        arr = []

        for row in testcase.split("\n "):
            arr.append(list(map(int, row.split("  "))))

        assert arr == [[-9, -9, -9, 1, 1, 1],
                       [0, -9, 0, 4, 3, 2],
                       [-9, -9, -9, 1, 2, 3],
                       [0, 0, 8, 6, 6, 0],
                       [0, 0, 0, -2, 0, 0],
                       [0, 0, 1, 2, 4, 0]]

class TestFindHourglasses(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        smaller_testcase = """-9  -9  -9  1  1  1\n 0  -9  0  4  3  2\n -9  -9  -9  1  2  3"""
        cls.arr = []

        for row in smaller_testcase.split("\n "):
            cls.arr.append(list(map(int, row.split("  "))))

        assert cls.arr ==  [[-9, -9, -9, 1, 1, 1],
                       [0, -9, 0, 4, 3, 2],
                       [-9, -9, -9, 1, 2, 3]]

    def test_find_one_hourglass(self):
        """brute force method"""
        row1_sum = self.arr[0][0] + self.arr[0][1] + self.arr[0][2]
        row2 = self.arr[1][1]
        row3_sum = self.arr[2][0] + self.arr[2][1] + self.arr[2][2]
        total = row1_sum + row2 + row3_sum

        assert total == -63

    def test_iterative_hourglasses(self):
        print(self.arr)
        sums = []
        for i in range(len(self.arr) -2):
            for j in range(len(self.arr[i]) - 2):
                one = self.arr[i][j] + self.arr[i][j+1] + self.arr[i][j+2]
                two = self.arr[i + 1][j + 1]
                three = self.arr[i + 2][j] + self.arr[i + 2][j+1] + self.arr[i + 2][j + 2]
                total = one + two + three
                print(total)
                sums.append(total)

        assert len(sums) == 4
        assert max(sums) == 12

if __name__ == '__main__':
    unittest2.main()