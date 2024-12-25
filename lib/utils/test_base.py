#!/usr/bin/env python3

class TestBase:
    def __init__(self, *args, **kwargs):
        self.host = None
        self.test_control = {}
    
    def setup(self, *args, **kwargs):
        pass
    
    def execute(self, *args, **kwargs):
        pass
    
    def cleanup(self, *args, **kwargs):
        pass