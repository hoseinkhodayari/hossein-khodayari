import re

# Read the file
with open('game_data.py', 'r') as f:
    content = f.read()

# Function to sanitize name for filename
def sanitize(name):
    return re.sub(r'[^\w\s-]', '', name).replace(' ', '_').lower()

# Find all dicts and add image
def add_image(match):
    dict_str = match.group(0)
    # Extract name
    name_match = re.search(r"'name':\s*'([^']+)'", dict_str)
    if name_match:
        name = name_match.group(1)
        image_path = f"images/{sanitize(name)}.jpg"
        # Insert before the closing }
        dict_str = re.sub(r'}\s*$', f", 'image': '{image_path}'" + '\n}', dict_str, flags=re.MULTILINE)
    return dict_str

# Replace all dicts
updated_content = re.sub(r'\{[^}]*\}', add_image, content)

# Write back
with open('game_data.py', 'w') as f:
    f.write(updated_content)

print("Updated game_data.py with image paths")