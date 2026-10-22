from isp_chip import black_level, white_balance

# Black level: subtract, never below 0
assert black_level(120, 16) == 104
assert black_level(16, 16) == 0
assert black_level(10, 16) == 0

# White balance: multiply, round, never above 255
assert white_balance(100, 64) == 100    # x1.0
assert white_balance(100, 96) == 150    # x1.5
assert white_balance(200, 128) == 255   # x2.0, saturates
assert white_balance(0, 255) == 0       # black stays black

print("All tests passed")