#!/usr/bin/env python3

from lib.utils.test_base import TestBase
from lib.utils.log import Log

class ScreeningTest(TestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self):
        super().setup()

    def execute(self):
        self.connect()
            
    def cleanup(self):
        # test cleanup
        super().cleanup()
    
    def connect(self):
        self.retries = self.test_control.get("retries")
        if self.retries:
            for attempt in self.retries:
                self.host.connect()
        else:
            self.host.connect()
