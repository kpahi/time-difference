import os
# import flaskr
import unittest
# import tempfile
from datetime import datetime as dt
from datetime import timedelta
import datetime

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        print("Setting UP files")

    def test_find_diff(self):
        date_format = "%Y-%m-%d %H:%M:%S"
        d_start_obj = dt.strptime("2018-10-10 11:11:11",date_format)
        d_end_obj = dt.strptime("2018-10-10 11:11:22", date_format)
        
        timedelta = d_end_obj - d_start_obj
        self.assertEquals(timedelta.total_seconds(),float(11.0))

      
if __name__ == '__main__':
    unittest.main()