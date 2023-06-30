# Read VOTI Detection Raw X-ray Data Format Files

a simple script to read the raw data format exported from VOTI Detection X-ray Scanners

## Data Format
- filename is of the format: ``SERIAL-DATE-TIME-VIEW.voti`` (e.g.  ``001234-20230630-160512-0.voti``) 
- 32-bit unsigned integer, no file header
- data comprises 2 images of same view at different energy levels (i.e. raw dual-energy X-ray response - high and low X-ray images)
- images resolution in px is _[ 640 x  L ]_, where _L_ is the length of the item in scanlines passing through the X-ray beam and is variable dependent on the item being scanned

## Usage

``
python3 ./read-voti.py filename.voti
``

## Observations
- data is uncorreected 64 x 10 samples from X-ray detector be 
