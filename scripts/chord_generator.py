#!/usr/bin/env python3
"""
Comprehensive Chord Generator
Generates chords with both sharp and flat variations and their corresponding notes.
Based on standard chord structures for various chord types.
"""

import csv

class ChordGenerator:
    def __init__(self):
        # Define all 12 chromatic notes in both sharp and flat notations
        self.chromatic_notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.chromatic_notes_flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        
        # Enharmonic equivalents mapping
        self.enharmonic_map = {
            'C#': 'Db', 'Db': 'C#',
            'D#': 'Eb', 'Eb': 'D#',
            'F#': 'Gb', 'Gb': 'F#',
            'G#': 'Ab', 'Ab': 'G#',
            'A#': 'Bb', 'Bb': 'A#'
        }
        
        # Chord intervals (in semitones from root)
        self.chord_intervals = {
            # Major chords
            'major': [0, 4, 7],                    # 1 • 3 • 5
            'major6': [0, 4, 7, 9],               # 1 • 3 • 5 • 6
            'major7': [0, 4, 7, 11],              # 1 • 3 • 5 • 7
            'major9': [0, 4, 7, 11, 14],          # 1 • 3 • 5 • 7 • 9
            'major11': [0, 4, 7, 11, 14, 17],     # 1 • 3 • 5 • 7 • 9 • 11
            
            # Suspended chords
            'sus2': [0, 2, 7],                    # 1 • 2 • 5
            'sus4': [0, 5, 7],                    # 1 • 4 • 5
            
            # Dominant chords
            'dominant7': [0, 4, 7, 10],           # 1 • 3 • 5 • b7
            'dominant9': [0, 4, 7, 10, 14],       # 1 • 3 • 5 • b7 • 9
            'dominant11': [0, 4, 7, 10, 14, 17],  # 1 • 3 • 5 • b7 • 9 • 11
            
            # Minor chords
            'minor': [0, 3, 7],                   # 1 • b3 • 5
            'minor6': [0, 3, 7, 9],               # 1 • b3 • 5 • 6
            'minor7': [0, 3, 7, 10],              # 1 • b3 • 5 • b7
            'minormajor7': [0, 3, 7, 11],         # 1 • b3 • 5 • 7
            'minor9': [0, 3, 7, 10, 14],          # 1 • b3 • 5 • b7 • 9
            'minor11': [0, 3, 7, 10, 14, 17],     # 1 • b3 • 5 • b7 • 9 • 11
            
            # Diminished chords
            'diminished': [0, 3, 6],              # 1 • b3 • b5
            'diminished7': [0, 3, 6, 9],          # 1 • b3 • b5 • bb7
            'half_diminished7': [0, 3, 6, 10],    # 1 • b3 • b5 • b7
            
            # Augmented chords
            'augmented': [0, 4, 8],               # 1 • 3 • #5
            'augmented7': [0, 4, 8, 10],          # 1 • 3 • #5 • b7
            
            # Special chord
            'dominant7sus4': [0, 5, 7, 10],       # 1 • 4 • 5 • b7
        }
        
        # Chord suffix mapping for display
        self.chord_suffixes = {
            'major': '',
            'major6': '6',
            'major7': 'maj7',
            'major9': 'maj9',
            'major11': 'maj11',
            'sus2': 'sus2',
            'sus4': 'sus4',
            'dominant7': '7',
            'dominant9': '9',
            'dominant11': '11',
            'minor': 'm',
            'minor6': 'm6',
            'minor7': 'm7',
            'minormajor7': 'm(maj7)',
            'minor9': 'm9',
            'minor11': 'm11',
            'diminished': 'dim',
            'diminished7': 'dim7',
            'half_diminished7': 'm7b5',
            'augmented': 'aug',
            'augmented7': 'aug7',
            'dominant7sus4': '7sus4'
        }
        
        # Chord type mapping (broad categories)
        self.chord_types = {
            'major': 'Major',
            'major6': 'Major',
            'major7': 'Major',
            'major9': 'Major',
            'major11': 'Major',
            'sus2': 'Suspended',
            'sus4': 'Suspended',
            'dominant7': 'Dominant',
            'dominant9': 'Dominant',
            'dominant11': 'Dominant',
            'minor': 'Minor',
            'minor6': 'Minor',
            'minor7': 'Minor',
            'minormajor7': 'Minor',
            'minor9': 'Minor',
            'minor11': 'Minor',
            'diminished': 'Diminished',
            'diminished7': 'Diminished',
            'half_diminished7': 'Diminished',
            'augmented': 'Augmented',
            'augmented7': 'Augmented',
            'dominant7sus4': 'Dominant'
        }
        
        # Chord extension mapping (specific variations)
        self.chord_extensions = {
            'major': 'Triad',
            'major6': '6th',
            'major7': 'Major 7th',
            'major9': 'Major 9th',
            'major11': 'Major 11th',
            'sus2': 'Sus2',
            'sus4': 'Sus4',
            'dominant7': 'Dominant 7th',
            'dominant9': 'Dominant 9th',
            'dominant11': 'Dominant 11th',
            'minor': 'Triad',
            'minor6': '6th',
            'minor7': 'Minor 7th',
            'minormajor7': 'Minor Major 7th',
            'minor9': 'Minor 9th',
            'minor11': 'Minor 11th',
            'diminished': 'Triad',
            'diminished7': 'Diminished 7th',
            'half_diminished7': 'Half Diminished 7th',
            'augmented': 'Triad',
            'augmented7': 'Augmented 7th',
            'dominant7sus4': 'Dominant 7th Sus4'
        }
    
    def get_note_at_interval(self, root_note, interval, use_sharps=True):
        """Get the note at a specific interval from the root note."""
        note_list = self.chromatic_notes_sharp if use_sharps else self.chromatic_notes_flat
        
        try:
            root_index = note_list.index(root_note)
        except ValueError:
            # If note not found in current list, try the other list
            other_list = self.chromatic_notes_flat if use_sharps else self.chromatic_notes_sharp
            try:
                root_index = other_list.index(root_note)
                note_list = other_list
            except ValueError:
                raise ValueError(f"Invalid note: {root_note}")
        
        target_index = (root_index + interval) % 12
        return note_list[target_index]
    
    def generate_chord_notes(self, root_note, chord_type, use_sharps=True):
        """Generate the notes for a specific chord."""
        if chord_type not in self.chord_intervals:
            raise ValueError(f"Unknown chord type: {chord_type}")
        
        intervals = self.chord_intervals[chord_type]
        notes = []
        
        for interval in intervals:
            note = self.get_note_at_interval(root_note, interval, use_sharps)
            notes.append(note)
        
        return notes
    
    def format_chord_name(self, root_note, chord_type):
        """Format the chord name with proper suffix."""
        suffix = self.chord_suffixes.get(chord_type, '')
        return f"{root_note}{suffix}"
    
    def generate_all_chords(self):
        """Generate all chords in both sharp and flat variations."""
        all_chords = []
        
        # Generate chords for each root note
        for root_note in self.chromatic_notes_sharp:
            # Skip notes that don't have enharmonic equivalents (C, D, E, F, G, A, B)
            natural_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
            
            for chord_type in self.chord_intervals.keys():
                # Generate sharp version
                chord_name = self.format_chord_name(root_note, chord_type)
                notes = self.generate_chord_notes(root_note, chord_type, use_sharps=True)
                all_chords.append({
                    'chord': chord_name,
                    'notes': notes,
                    'type': chord_type,
                    'root': root_note
                })
                
                # Generate flat version if the root note has an enharmonic equivalent
                if root_note in self.enharmonic_map:
                    flat_root = self.enharmonic_map[root_note]
                    flat_chord_name = self.format_chord_name(flat_root, chord_type)
                    flat_notes = self.generate_chord_notes(flat_root, chord_type, use_sharps=False)
                    all_chords.append({
                        'chord': flat_chord_name,
                        'notes': flat_notes,
                        'type': chord_type,
                        'root': flat_root
                    })
        
        return all_chords
    
    def print_chords_by_type(self, chord_type=None):
        """Print chords organized by type."""
        all_chords = self.generate_all_chords()
        
        if chord_type:
            # Filter by specific chord type
            filtered_chords = [chord for chord in all_chords if chord['type'] == chord_type]
            chords_to_print = filtered_chords
        else:
            chords_to_print = all_chords
        
        # Group by chord type
        chords_by_type = {}
        for chord in chords_to_print:
            chord_type_key = chord['type']
            if chord_type_key not in chords_by_type:
                chords_by_type[chord_type_key] = []
            chords_by_type[chord_type_key].append(chord)
        
        # Print organized output
        for chord_type_key in sorted(chords_by_type.keys()):
            print(f"\n{chord_type_key.upper().replace('_', ' ')} CHORDS:")
            print("-" * 50)
            
            for chord in sorted(chords_by_type[chord_type_key], key=lambda x: x['chord']):
                notes_str = ", ".join(chord['notes'])
                print(f"{chord['chord']:<12} ({notes_str})")
    
    def save_chords_to_csv(self, filename="comprehensive_chords.csv"):
        """Save all chords to a CSV file with chord name, notes, chord type, and chord extension."""
        all_chords = self.generate_all_chords()
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['chord_name', 'notes', 'chord_type', 'chord_extension']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Sort chords by chord type, then by chord extension, then by chord name
            sorted_chords = sorted(all_chords, key=lambda x: (
                self.chord_types[x['type']], 
                self.chord_extensions[x['type']], 
                x['chord']
            ))
            
            # Write chord data
            for chord in sorted_chords:
                notes_str = ", ".join(chord['notes'])
                chord_type = self.chord_types[chord['type']]
                chord_extension = self.chord_extensions[chord['type']]
                
                writer.writerow({
                    'chord_name': chord['chord'],
                    'notes': notes_str,
                    'chord_type': chord_type,
                    'chord_extension': chord_extension
                })
        
        print(f"Chords saved to {filename}")
    
    def save_chords_to_file(self, filename="comprehensive_chords.txt"):
        """Save all chords to a text file."""
        all_chords = self.generate_all_chords()
        
        with open(filename, 'w') as f:
            f.write("COMPREHENSIVE CHORD LIST\n")
            f.write("=" * 50 + "\n\n")
            
            # Group by chord type
            chords_by_type = {}
            for chord in all_chords:
                chord_type_key = chord['type']
                if chord_type_key not in chords_by_type:
                    chords_by_type[chord_type_key] = []
                chords_by_type[chord_type_key].append(chord)
            
            # Write organized output
            for chord_type_key in sorted(chords_by_type.keys()):
                f.write(f"\n{chord_type_key.upper().replace('_', ' ')} CHORDS:\n")
                f.write("-" * 50 + "\n")
                
                for chord in sorted(chords_by_type[chord_type_key], key=lambda x: x['chord']):
                    notes_str = ", ".join(chord['notes'])
                    f.write(f"{chord['chord']:<12} ({notes_str})\n")
        
        print(f"Chords saved to {filename}")
    
    def save_chords(self, csv_filename="comprehensive_chords.csv", txt_filename="comprehensive_chords.txt"):
        """Save chords to both CSV and text files."""
        self.save_chords_to_csv(csv_filename)
        self.save_chords_to_file(txt_filename)
    
    def find_chord(self, chord_name):
        """Find a specific chord and return its notes."""
        all_chords = self.generate_all_chords()
        
        for chord in all_chords:
            if chord['chord'].lower() == chord_name.lower():
                return chord
        
        return None


def main():
    """Main function to demonstrate the chord generator."""
    generator = ChordGenerator()
    
    print("COMPREHENSIVE CHORD GENERATOR")
    print("=" * 50)
    
    # Example: Show minor chords
    print("\nExample - All Minor Chords:")
    generator.print_chords_by_type('minor')
    
    # Example: Find specific chords
    print("\n\nExample - Specific Chord Lookup:")
    test_chords = ['C#m', 'Dbm', 'F#maj7', 'Gbmaj7']
    for chord_name in test_chords:
        chord = generator.find_chord(chord_name)
        if chord:
            notes_str = ", ".join(chord['notes'])
            print(f"{chord['chord']:<8} ({notes_str})")
        else:
            print(f"{chord_name} - Not found")
    
    # Generate and save all chords to both CSV and text files
    print(f"\nGenerating comprehensive chord list...")
    generator.save_chords()  # This now saves to both CSV and TXT by default
    
    # Show total count
    all_chords = generator.generate_all_chords()
    print(f"Total chords generated: {len(all_chords)}")
    print("Files created:")
    print("- comprehensive_chords.csv (CSV format with chord types and extensions)")
    print("- comprehensive_chords.txt (Text format for reading)")


if __name__ == "__main__":
    main()