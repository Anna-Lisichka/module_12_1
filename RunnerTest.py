import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        road = Runner.Runner('Wall Street')
        for i in range(10):
            road.walk()
        self.assertEqual(road.distance, 50)
        # print(road.distance)

    def test_run(self):
        runner= Runner.Runner('Peter')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        # print(runner.distance)

# при значении 80 тест не будет пройден, т.к. сравниваемое число 100 не равно 80
#         self.assertEqual(runner.distance, 80)
        # print(runner.distance)


    def test_challenge(self):
        partner1 = Runner.Runner('Kate')
        partner2 = Runner.Runner('Anna')
        for _ in range(10):
            partner1.walk()
            partner2.run()
        # self.assertNotEqual(partner1.distance, partner2.distance)
        # print(partner1.distance, partner2.distance)

# если проводить тест на равенство, то тест не будет пройден, поскольку сравниваемые значения 50 и 100
#         self.assertEqual(partner1.distance, partner2.distance)
#         print(partner1.distance, partner2.distance)


if __name__ == '__main__':
    unittest.main()


