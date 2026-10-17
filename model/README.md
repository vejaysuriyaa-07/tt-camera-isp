# Golden model

Python reference model of the ISP. Every stage exists twice:
- **Float model:** the "perfect" version, used to measure quality (PSNR)
- **Integer model:** matches the chip bit for bit, including rounding and clamping

Chip front-end stages: black level, white balance (8-bit Q2.6 gain per Bayer position), gamma curve.
Crops always start at even row/column so the Bayer pattern doesn't shift.
