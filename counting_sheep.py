#!/usr/bin/env python3
# A simple script that counts upwards from 1 every two seconds
# until the user presses Ctrl+C

import time

def main():
    x = 0

    print("Counting sheep...")

    while True:
        try:
            x = x + 1
            print(x)
            time.sleep(2)
        except KeyboardInterrupt:
            raise

if __name__ == "__main__":
    main()
    
