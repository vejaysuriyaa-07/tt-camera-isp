"""Chip-mode golden model. Must match the RTL bit for bit."""

def black_level(px, bl):
   return max(px - bl, 0)

def white_balance(px, gain):
    scaled = (px * gain + 32) >> 6
    return min(scaled, 255)