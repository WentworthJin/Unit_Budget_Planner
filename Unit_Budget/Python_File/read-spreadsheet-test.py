import unittest
from read_spreadsheet import resourcing_data

class TestMethod(unittest.TestCase):
    def setUp(self):
        print("set up test")

    def test_resourcing_data(self):
        self.sourcing = resourcing_data("CITS1001_Sem1,2021 budget v3.xlsx")
        self.assertEqual(self.sourcing,['[{"Name": "Lyndon While", "Type": "Academic staff", "TeachingCode": null, "Lectures": "No cost", "Workshops": "=I31", "Laboratories": "=I32+I33"}]', '[{"Name": "Manou Rosenberg", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA (Hon Degree)", "Workshops": null, "Laboratories": null}]', '[{"Name": "Casual 2", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA", "Workshops": null, "Laboratories": null}]', '[{"Name": "Casual 3", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA", "Workshops": null, "Laboratories": null}]', '[{"Name": "Casual 4", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA", "Workshops": null, "Laboratories": null}]', '[{"Name": "Casual 5", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA", "Workshops": null, "Laboratories": null}]', '[{"Name": "Casual 6", "Type": "Casual teaching", "TeachingCode": null, "Lectures": "ORAA", "Workshops": null, "Laboratories": null}]'])


if __name__ == '__main__':
    unittest.main()
