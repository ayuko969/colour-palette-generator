import requests

def fetch_colour_palette(seed_colour):
    url = f'https://www.thecolorapi.com/scheme?hex={seed_colour}&mode=monochrome&count=5'
    print (f'Fetching data from: {url}')

    try: 
        response = requests.get(url)
        response.raise_for_status()
    except:
        print ("Error fetching data")
        quit()

    return response.json()
    
def desplay_colour_palette(palette_data):
    if not palette_data or 'colors' not in palette_data:
        print("No palette data found.")
        return
    
    colours = palette_data['colors']
    print("Generated Colour Palette:")
    for idx, color in enumerate(colours, start=1):
        colour_hex = color['hex']['value']
        rgb = color['rgb']
        print (f"Color {idx}: {colour_hex} (RGB: {rgb['r']}, {rgb['g']}, {rgb['b']})")

def main():
    seed_colour = input("Enter the seed colour in hex format (e.g. 'ff5633'): ").strip('#')
    palette_data = fetch_colour_palette(seed_colour)

    if palette_data:
        desplay_colour_palette(palette_data)
    else:
        print ("Failed to fetch the colour palette.")

main()