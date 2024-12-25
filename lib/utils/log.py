#!/usr/bin/env python3

class Log:
    def log_info(msg):
        print(msg)
        
    def log_error(msg):
        print(f"ERROR: {msg}")
    
    def log_warning(msg):
        print(f"Warning: {msg}")