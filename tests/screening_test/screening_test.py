#!/usr/bin/env python3

from lib.utils.test_base import TestBase
from lib.utils.log import Log

class ScreeningTest(TestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        TESTS = {
            "sleep_test": self.sleep,
        }
        self.tests = self.test_control.get("tests", {})

    def setup(self):
        super().setup()

    def execute(self):
        for test in self.tests:
            if test in self.TESTS:
                self.TESTS(test)()
            else:
                Log.log_info("Test not found! .")
            
    def cleanup(self):
        # test cleanup
        super().cleanup()
    
    @staticmethod
    def sleep(time=60):
        time.sleep(time)
