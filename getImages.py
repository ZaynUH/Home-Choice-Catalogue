import os
import json

# Step 1: Set the directory where your images are stored
directory = 'ItemImages'

# Step 2: List to store image metadata
image_list = []

# Step 3: Loop through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):  # Only process PNG files
        # Remove the '.png' extension
        base_name = filename.replace('.png', '')

        # Split the filename into parts (assuming the format is consistent like 'Double-DivanBed-2Drawer')
        parts = base_name.split('-')

        # Step 4: Assign size, item, and addition (default to 'N/A' if not available)
        size = parts[0]
        item = parts[1]
        addition = parts[2] if len(parts) > 2 else "N/A"

        # Add the image data to the list
        image_list.append({
            "size": size,
            "item": item,
            "addition": addition,
            "src": f"{directory}/{filename}"  # Store the relative path to the image
        })

# Step 5: Save the image data to a JSON file
with open('images.json', 'w') as json_file:
    json.dump(image_list, json_file, indent=4)

print(f"Generated images.json with {len(image_list)} images.")
