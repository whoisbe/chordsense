# Comprehensive Chord Generator

This Python script generates a comprehensive list of chords with both sharp and flat variations, including all their corresponding notes. **Now generates CSV files by default** with chord families for easy data analysis!

## Features

- **374 total chords** across all 12 chromatic notes
- **Both sharp and flat variations** (e.g., C#m and Dbm as separate entries)
- **22 different chord types** based on standard chord structures
- **CSV output by default** with chord name, notes, chord type, and chord extension columns
- **Music theory-based classification** with proper chord types and extensions
- **Text file option** still available for human-readable format
- **Enharmonic equivalents** properly handled
- **Easy lookup** of specific chords
- **Detailed chord categorization** (6 chord types, 18 chord extensions)

## Supported Chord Types

Based on the chord structure chart provided:

### Major Chords
- **Major** (1 • 3 • 5)
- **Major 6** (1 • 3 • 5 • 6)
- **Major 7** (1 • 3 • 5 • 7)
- **Major 9** (1 • 3 • 5 • 7 • 9)
- **Major 11** (1 • 3 • 5 • 7 • 9 • 11)

### Suspended Chords
- **Sus 2** (1 • 2 • 5)
- **Sus 4** (1 • 4 • 5)

### Dominant Chords
- **Dominant 7** (1 • 3 • 5 • b7)
- **Dominant 9** (1 • 3 • 5 • b7 • 9)
- **Dominant 11** (1 • 3 • 5 • b7 • 9 • 11)
- **Dominant 7 Sus 4** (1 • 4 • 5 • b7)

### Minor Chords
- **Minor** (1 • b3 • 5)
- **Minor 6** (1 • b3 • 5 • 6)
- **Minor 7** (1 • b3 • 5 • b7)
- **Minor/Major 7** (1 • b3 • 5 • 7)
- **Minor 9** (1 • b3 • 5 • b7 • 9)
- **Minor 11** (1 • b3 • 5 • b7 • 9 • 11)

### Diminished Chords
- **Diminished** (1 • b3 • b5)
- **Diminished 7** (1 • b3 • b5 • bb7)
- **Half Diminished 7** (1 • b3 • b5 • b7)

### Augmented Chords
- **Augmented** (1 • 3 • #5)
- **Augmented 7** (1 • 3 • #5 • b7)

## Usage Examples

### CSV Output (Default)
```python
from chord_generator import ChordGenerator

generator = ChordGenerator()

# Generate CSV file with chord families (default)
generator.save_chords_to_csv("my_chords.csv")

# Generate both CSV and text files
generator.save_chords("chords.csv", "chords.txt")
```

### Basic Chord Lookup
```python
# Find a specific chord
chord = generator.find_chord('C#m')
print(f"{chord['chord']}: {', '.join(chord['notes'])}")
# Output: C#m: C#, E, G#

# Generate notes for a chord
notes = generator.generate_chord_notes('Db', 'minor', use_sharps=False)
print(f"Dbm: {', '.join(notes)}")
# Output: Dbm: Db, E, Ab
```

### Text Output (Optional)
```python
# Generate text file only
generator.save_chords_to_file("my_chords.txt")

# Print all chords of a specific type
generator.print_chords_by_type('minor')
```

### Enharmonic Equivalents Example

The script correctly generates both sharp and flat variations:

- **C#m**: C#, E, G#
- **Dbm**: Db, E, Ab

These are enharmonically equivalent but represented as separate entries with their respective notation systems.

## Files Generated

1. **chord_generator.py** - Main ChordGenerator class
2. **chord_demo.py** - Demonstration script with examples
3. **comprehensive_chords.csv** - Complete list of all 374 chords in CSV format (DEFAULT)
4. **comprehensive_chords.txt** - Complete list in text format for reading
5. **README.md** - This usage guide

## CSV File Format

The CSV file contains four columns based on music theory:
- **chord_name**: The chord symbol (e.g., "C#m", "Dbmaj7")
- **notes**: Comma-separated list of notes (e.g., "C#, E, G#")
- **chord_type**: The broad chord category (Major, Minor, Dominant, etc.)
- **chord_extension**: The specific chord variation (Triad, 7th, 9th, etc.)

### Chord Types (Broad Categories):
- **Major** (85 chords): All major-based harmonies
- **Minor** (102 chords): All minor-based harmonies  
- **Dominant** (68 chords): All dominant-function chords
- **Diminished** (51 chords): All diminished harmonies
- **Augmented** (34 chords): All augmented harmonies
- **Suspended** (34 chords): All suspended chords

### Chord Extensions (Specific Variations):
- **Triad** (68 chords): Basic three-note chords
- **6th** (34 chords): Added sixth chords
- **Major 7th** (17 chords): Major seventh chords
- **Minor 7th** (17 chords): Minor seventh chords
- **Dominant 7th** (17 chords): Dominant seventh chords
- **Major 9th** (17 chords): Major ninth chords
- **Minor 9th** (17 chords): Minor ninth chords
- **Dominant 9th** (17 chords): Dominant ninth chords
- **Major 11th** (17 chords): Major eleventh chords
- **Minor 11th** (17 chords): Minor eleventh chords
- **Dominant 11th** (17 chords): Dominant eleventh chords
- **Sus2** (17 chords): Suspended second chords
- **Sus4** (17 chords): Suspended fourth chords
- **Diminished 7th** (17 chords): Fully diminished seventh chords
- **Half Diminished 7th** (17 chords): Half-diminished seventh chords
- **Augmented 7th** (17 chords): Augmented seventh chords
- **Minor Major 7th** (17 chords): Minor chords with major seventh
- **Dominant 7th Sus4** (17 chords): Dominant seventh suspended fourth chords

## Running the Scripts

```bash
# Run the main generator (creates both CSV and TXT files)
python chord_generator.py

# Run the demonstration examples
python chord_demo.py
```

## Output Formats

### CSV Format (Default):
```csv
chord_name,notes,chord_type,chord_extension
C#m,"C#, E, G#",Minor,Triad
Dbm,"Db, E, Ab",Minor,Triad
F#maj7,"F#, A#, C#, F",Major,Major 7th
Gbmaj7,"Gb, Bb, Db, F",Major,Major 7th
C9,"C, E, G, A#, D",Dominant,Dominant 9th
Am11,"A, C, E, G, B, D",Minor,Minor 11th
```

### Text Format:
```
ChordName    (Note1, Note2, Note3, ...)
```

Example:
```
C#m          (C#, E, G#)
Dbm          (Db, E, Ab)
F#maj7       (F#, A#, C#, F)
Gbmaj7       (Gb, Bb, Db, F)
```

## Total Chord Count

The generator creates **374 total chords**:
- 12 root notes × 22 chord types = 264 base chords
- Plus enharmonic equivalents for sharps/flats = 110 additional chords
- **Total: 374 chords**

This comprehensive collection covers all standard chord types with both sharp and flat notations as requested.