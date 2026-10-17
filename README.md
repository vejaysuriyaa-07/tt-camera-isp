# Camera ISP on Silicon

**How close can a small fixed-point hardware ISP get to a full-precision software pipeline on real photos, and at what area and power cost?**

This project builds a camera image signal processor (ISP) from scratch: a bit-exact Python golden model driven by my own RAW photos, a SystemVerilog implementation verified against it, and the front end taped out on the Tiny Tapeout SKY130 shuttle.

## Status
- [ ] Golden model (Python)
- [ ] Chip RTL + cocotb tests
- [ ] Tiny Tapeout submission (Nov 2026)
- [ ] UVM verification environment
- [ ] Full ISP (demosaic + color correction)
- [ ] Silicon bring-up

## Repo layout
- `model/` Python golden model
- `src/` Verilog for the chip
- `test/` cocotb tests
- `docs/` chip documentation for Tiny Tapeout

Built on the [Tiny Tapeout SKY130 Verilog template](https://github.com/TinyTapeout/ttsky-verilog-template).
