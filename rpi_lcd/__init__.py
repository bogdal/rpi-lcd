from smbus import SMBus
from time import sleep

ALIGN_FUNC = {
    'left': 'ljust',
    'right': 'rjust',
    'center': 'center'}
CLEAR_DISPLAY = 0x01
ENABLE_BIT = 0b00000100
LINES = {
    1: 0x80,
    2: 0xC0,
    3: 0x94,
    4: 0xD4}


class LCD(object):

    def __init__(self, address=0x27, bus=1, width=20):
        self.address = address
        self.bus = SMBus(bus)
        self.delay = 0.0005
        self.width = width

        self.write(0x33)
        self.write(0x32)
        self.write(0x06)
        self.write(0x0C)
        self.write(0x28)
        self.write(CLEAR_DISPLAY)
        sleep(self.delay)

    def _write_byte(self, byte):
        self.bus.write_byte(self.address, byte)
        self.bus.write_byte(self.address, (byte | ENABLE_BIT))
        sleep(self.delay)
        self.bus.write_byte(self.address,(byte & ~ENABLE_BIT))
        sleep(self.delay)

    def write(self, byte, mode=0):
        self._write_byte(mode | (byte & 0xF0) | 0x08)
        self._write_byte(mode | ((byte << 4) & 0xF0) | 0x08)

    def text(self, text, line, align='left'):
        self.write(LINES.get(line, LINES[1]))
        text = getattr(text, ALIGN_FUNC.get(align, 'ljust'))(self.width)
        for char in text:
            self.write(ord(char), mode=1)

    def clear(self):
        self.write(CLEAR_DISPLAY)
