import csv
import json
from pathlib import Path
from sys import argv
 
# Converts Coordinates.csv into places.json for use with Leaflet.
# The CSV is now the single source of truth for all place data and coordinates.
#
# Usage: python csv_to_places_json.py Coordinates.csv
# Output: places.json (written next to the CSV)
 
MAP_HEIGHT = 6144
MAP_WIDTH = 8192
 
if len(argv) != 2:
    raise Exception("Usage: python csv_to_places_json.py <path_to_Coordinates.csv>")
 
csv_path = Path(argv[1])
 
if not csv_path.exists():
    raise FileNotFoundError(f"Could not find: {csv_path}")
 
places = {}
 
with open(csv_path, newline="", encoding="cp1252") as f:
    reader = csv.DictReader(f)
 
    for row in reader:
        name = row["Name"].strip()
        if not name:
            continue
 
        # Parse coordinates
        try:
            x1 = int(row["X1"].strip())
            y1 = int(row["Y1"].strip())
            x2 = int(row["X2"].strip())
            y2 = int(row["Y2"].strip())
        except (ValueError, KeyError):
            print(f"  Skipping '{name}' — missing or invalid coordinates")
            continue
 
        # Flip Y axis: Leaflet CRS.Simple has 0 at the bottom, image has 0 at top
        leaflet_y1 = MAP_HEIGHT - y1
        leaflet_y2 = MAP_HEIGHT - y2
 
        # Build 4-corner polygon (instead of 2-point rectangle)
        # Leaflet wants [lat, lng] which maps to [y, x]
        coords = [
            [leaflet_y1, x1],  # top-left
            [leaflet_y1, x2],  # top-right
            [leaflet_y2, x2],  # bottom-right
            [leaflet_y2, x1],  # bottom-left
        ]
 
        # Collect optional fields — only include if non-empty
        entry = {
            "place": name,
            "type": row.get("Type", "").strip() or None,
            "region": row.get("Kingdom/Region", "").strip() or None,
            "leader": row.get("Leader", "").strip() or None,
            "description": row.get("Description", "").strip() or None,
            "coords": coords,
        }
 
        # Remove keys with None values to keep JSON clean
        entry = {k: v for k, v in entry.items() if v is not None}
 
        # Handle duplicate names (e.g. "The Great Stone Road" appears 3 times)
        # Append a suffix so all entries are preserved
        key = name
        suffix = 2
        while key in places:
            key = f"{name} ({suffix})"
            suffix += 1
 
        places[key] = entry
 
output_path = Path("places.json")
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(places, out, indent=2, ensure_ascii=False)
 
print(f"Done! Written {len(places)} places to: {output_path}")
 
