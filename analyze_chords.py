#!/usr/bin/env python3
"""
Example script showing how to analyze the comprehensive chord CSV file
with the new chord_type and chord_extension columns.
"""

import csv
from collections import defaultdict

def analyze_chord_data(csv_file="comprehensive_chords.csv"):
    """Analyze the chord data from the CSV file."""
    
    # Data structures for analysis
    chords_by_type = defaultdict(list)
    chords_by_extension = defaultdict(list)
    chords_by_type_and_extension = defaultdict(lambda: defaultdict(list))
    
    # Read the CSV file
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chord_name = row['chord_name']
            notes = row['notes']
            chord_type = row['chord_type']
            chord_extension = row['chord_extension']
            
            chords_by_type[chord_type].append((chord_name, notes))
            chords_by_extension[chord_extension].append((chord_name, notes))
            chords_by_type_and_extension[chord_type][chord_extension].append((chord_name, notes))
    
    return chords_by_type, chords_by_extension, chords_by_type_and_extension

def find_chords_by_criteria(csv_file="comprehensive_chords.csv", 
                           chord_type=None, chord_extension=None, 
                           contains_note=None):
    """Find chords matching specific criteria."""
    
    matching_chords = []
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check criteria
            if chord_type and row['chord_type'] != chord_type:
                continue
            if chord_extension and row['chord_extension'] != chord_extension:
                continue
            if contains_note and contains_note not in row['notes']:
                continue
            
            matching_chords.append({
                'name': row['chord_name'],
                'notes': row['notes'],
                'type': row['chord_type'],
                'extension': row['chord_extension']
            })
    
    return matching_chords

def main():
    """Demonstrate chord analysis capabilities."""
    
    print("CHORD DATA ANALYSIS")
    print("=" * 50)
    
    # Basic analysis
    by_type, by_extension, by_type_ext = analyze_chord_data()
    
    print("\n1. CHORD TYPES SUMMARY:")
    print("-" * 30)
    for chord_type in sorted(by_type.keys()):
        count = len(by_type[chord_type])
        print(f"{chord_type:<12} {count:>3} chords")
    
    print("\n2. CHORD EXTENSIONS SUMMARY:")
    print("-" * 30)
    for extension in sorted(by_extension.keys()):
        count = len(by_extension[extension])
        print(f"{extension:<20} {count:>3} chords")
    
    # Example queries
    print("\n3. EXAMPLE QUERIES:")
    print("-" * 30)
    
    # Find all dominant 7th chords
    dom7_chords = find_chords_by_criteria(
        chord_type="Dominant", 
        chord_extension="Dominant 7th"
    )
    print(f"\nDominant 7th chords ({len(dom7_chords)}):")
    for chord in dom7_chords[:5]:  # Show first 5
        print(f"  {chord['name']:<8} = {chord['notes']}")
    if len(dom7_chords) > 5:
        print(f"  ... and {len(dom7_chords) - 5} more")
    
    # Find all chords containing C# note
    cs_chords = find_chords_by_criteria(contains_note="C#")
    print(f"\nChords containing C# ({len(cs_chords)}):")
    for chord in cs_chords[:5]:  # Show first 5
        print(f"  {chord['name']:<8} = {chord['notes']}")
    if len(cs_chords) > 5:
        print(f"  ... and {len(cs_chords) - 5} more")
    
    # Find all minor 9th chords
    min9_chords = find_chords_by_criteria(
        chord_type="Minor", 
        chord_extension="Minor 9th"
    )
    print(f"\nMinor 9th chords ({len(min9_chords)}):")
    for chord in min9_chords:
        print(f"  {chord['name']:<8} = {chord['notes']}")
    
    # Find all suspended chords
    sus_chords = find_chords_by_criteria(chord_type="Suspended")
    print(f"\nSuspended chords ({len(sus_chords)}):")
    for chord in sus_chords[:6]:  # Show first 6
        print(f"  {chord['name']:<8} = {chord['notes']}")
    if len(sus_chords) > 6:
        print(f"  ... and {len(sus_chords) - 6} more")
    
    print("\n4. CHORD TYPE & EXTENSION MATRIX:")
    print("-" * 30)
    print("Type\\Extension breakdown:")
    for chord_type in sorted(by_type_ext.keys()):
        print(f"\n{chord_type}:")
        for extension in sorted(by_type_ext[chord_type].keys()):
            count = len(by_type_ext[chord_type][extension])
            print(f"  {extension:<20} {count:>2} chords")

if __name__ == "__main__":
    main()