## How it works

This project is the front end of a camera image signal processor (ISP). It takes raw 8-bit pixels from a Bayer-pattern image sensor and processes them in fixed-point hardware:

1. **Black level correction:** subtracts the sensor's black level, with the result floored at 0
2. **White balance:** multiplies each pixel by a gain chosen by its Bayer color position (8-bit Q2.6 gains, rounded and saturated)
3. **Gamma:** applies a piecewise-linear tone curve

The hardware is verified bit for bit against a Python golden model driven by real RAW photos.

**Status:** work in progress. The current RTL is still the Tiny Tapeout example design. The ISP front end replaces it before submission.

## How to test

Set the black level and white balance gains over SPI on the bidirectional pins, then stream Bayer pixels on `ui_in` and read the processed pixels on `uo_out`. Full pin details will be added with the RTL.

## External hardware

None. Uses the Tiny Tapeout demo board.
