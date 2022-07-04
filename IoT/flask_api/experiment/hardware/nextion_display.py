from time import sleep
import string
import serial
from typing import List
from typing import AnyStr


class NextionDisplay:
    def __init__(self) -> None:
        self._time_sleep = 0.1
        self._uart = serial.Serial('/dev/ttyS0', 9600) # secondary Raspberry Pi serial port

    @staticmethod
    def _separate_text(msg:AnyStr) -> List:
        _text:List = []
        for letter in range(len(msg)):
            _text.append(msg[letter].lower())
        return _text

    def _create_msg_hex(self, msg:AnyStr) -> List:
        _final_lines = [0xff, 0xff, 0xff]
        msg_to_bytes = bytes(msg, 'UTF-8')
        msg_to_hex = [ part for part in msg_to_bytes ]
        return msg_to_hex + _final_lines

    def write_speak(self, msg:AnyStr) -> None:
        base_instruction = 'add 1,0,'
        text = self._separate_text(msg)
        for letter in text:
            _index = 0 if letter == ' ' else string.ascii_lowercase.index(letter)
            text_hex = self._create_msg_hex(f'{base_instruction}{_index*5}')
            self._uart.write(serial.to_bytes(text_hex))
            sleep(self._time_sleep)
        self._uart.close()


if __name__=='__main__':
    NextionDisplay().write_speak('Halo ! Memulai proses...    ')
