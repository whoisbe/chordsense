#!/usr/bin/env python3
"""
Demo script showing various ways to use the ChordGenerator class.
"""

from chord_generator import ChordGenerator

def demo_enharmonic_equivalents():
    """Demonstrate enharmonic equivalent chords (sharp vs flat)."""
    generator = ChordGenerator()
    
    print("ENHARMONIC EQUIVALENT CHORDS")
    print("=" * 40)
    
    # Define some test chords that have enharmonic equivalents
    test_pairs = [
        ('C#', 'Db'),
        ('D#', 'Eb'),
        ('F#', 'Gb'),
        ('G#', 'Ab'),
        ('A#', 'Bb')
    ]
    
    chord_types = ['minor', 'major', 'major7', 'dominant7']
    
    for sharp_root, flat_root in test_pairs:
        print(f"\n{sharp_root} vs {flat_root} chords:")
        print("-" * 30)
        
        for chord_type in chord_types:
            # Generate sharp version
            sharp_chord = generator.format_chord_name(sharp_root, chord_type)
            sharp_notes = generator.generate_chord_notes(sharp_root, chord_type, use_sharps=True)
            
            # Generate flat version
            flat_chord = generator.format_chord_name(flat_root, chord_type)
            flat_notes = generator.generate_chord_notes(flat_root, chord_type, use_sharps=False)
            
            print(f"{sharp_chord:<8} ({', '.join(sharp_notes):<12}) | {flat_chord:<8} ({', '.join(flat_notes)})")

def demo_chord_progressions():
    """Demonstrate common chord progressions."""
    generator = ChordGenerator()
    
    print("\n\nCOMMON CHORD PROGRESSIONS")
    print("=" * 40)
    
    # Common progressions in different keys
    progressions = {
        "vi-IV-I-V (C major)": [('Am', 'minor'), ('F', 'major'), ('C', 'major'), ('G', 'major')],
        "I-V-vi-IV (G major)": [('G', 'major'), ('D', 'major'), ('Em', 'minor'), ('C', 'major')],
        "ii-V-I (jazz, C major)": [('Dm', 'minor7'), ('G', 'dominant7'), ('C', 'major7')],
        "I-VI-ii-V (doo-wop, C major)": [('C', 'major'), ('A', 'major'), ('Dm', 'minor'), ('G', 'major')]
    }
    
    for progression_name, chords in progressions.items():
        print(f"\n{progression_name}:")
        chord_info = []
        for root_note, chord_type in chords:
            # Extract root note (handle cases like 'Am' where 'm' is part of chord name)
            if root_note.endswith('m'):
                actual_root = root_note[:-1]
                actual_type = 'minor'
            else:
                actual_root = root_note
                actual_type = chord_type
            
            notes = generator.generate_chord_notes(actual_root, actual_type)
            chord_name = generator.format_chord_name(actual_root, actual_type)
            chord_info.append(f"{chord_name} ({', '.join(notes)})")
        
        print(" → ".join(chord_info))

def demo_chord_family():
    """Demonstrate all variations of chords built on the same root."""
    generator = ChordGenerator()
    
    print("\n\nCHORD FAMILIES (All C chords)")
    print("=" * 40)
    
    root_note = 'C'
    chord_types = [
        'major', 'minor', 'major7', 'minor7', 'dominant7',
        'major6', 'minor6', 'sus2', 'sus4', 'diminished',
        'augmented', 'major9', 'minor9', 'dominant9'
    ]
    
    for chord_type in chord_types:
        chord_name = generator.format_chord_name(root_note, chord_type)
        notes = generator.generate_chord_notes(root_note, chord_type)
        print(f"{chord_name:<12} ({', '.join(notes)})")

def demo_find_specific_chords():
    """Demonstrate finding specific chords by name."""
    generator = ChordGenerator()
    
    print("\n\nFIND SPECIFIC CHORDS")
    print("=" * 40)
    
    search_chords = [
        'C#m', 'Dbm', 'F#maj7', 'Gbmaj7', 'Am7', 'Dm9', 
        'G7sus4', 'Bdim7', 'Eaug', 'Abmaj9'
    ]
    
    print("Searching for chords:")
    for chord_name in search_chords:
        chord = generator.find_chord(chord_name)
        if chord:
            notes_str = ", ".join(chord['notes'])
            print(f"{chord['chord']:<10} ({notes_str})")
        else:
            print(f"{chord_name:<10} (Not found)")

def main():
    """Run all demonstrations."""
    demo_enharmonic_equivalents()
    demo_chord_progressions()
    demo_chord_family()
    demo_find_specific_chords()
    
    print("\n\nFILE OUTPUT OPTIONS")
    print("=" * 40)
    
    generator = ChordGenerator()
    
    # Generate CSV file (default)
    print("Generating CSV file...")
    generator.save_chords_to_csv("demo_chords.csv")
    
    # Generate text file (optional)
    print("Generating text file...")
    generator.save_chords_to_file("demo_chords.txt")
    
    # Generate both files at once
    print("Generating both files...")
    generator.save_chords("all_chords.csv", "all_chords.txt")
    
    print("\nFor the complete list:")
    print("- CSV format: comprehensive_chords.csv")
    print("- Text format: comprehensive_chords.txt")

if __name__ == "__main__":
    main()