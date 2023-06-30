# Read VOTI Detection Raw X-ray Data Format Files

a simple script to read the raw data format exported from VOTI Detection X-ray Scanners

## Data Format

- 32-bit unsigned integer, no file header
- data comprises 2 images at different energy levels (dual-energy X-ray response - high and low X-ray images)
- images resolution in px is _[ 640 x  L ]_, where _L_ is the length of the item in scanlines  passing through the X-ray and is variable dependent on the item being scanned

## Usage

``
python3 ./read-voti.py filename.voti
``

## Observations
