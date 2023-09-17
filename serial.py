"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ """
        self.start = start
        self.place = start - 1
        
    def generate(self):
        self.place += 1
        return self.place

    def reset(self):
        self.place = self.start - 1



