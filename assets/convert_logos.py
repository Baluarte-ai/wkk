# assets/convert_logos.py

import os
from PIL import Image

def make_wkk_logo_transparent():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "Logo WKK.jpg")
    output_path = os.path.join(base_dir, "Logo WKK.png")
    
    if not os.path.exists(input_path):
        print(f"Error: WKK logo not found at {input_path}")
        return False
        
    try:
        # Load and convert to RGBA
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # item is (R, G, B, A)
            # Scan for white pixels (R, G, B > 240)
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0)) # Fully transparent
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Success: Transparent WKK logo saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error converting WKK logo: {e}")
        return False

if __name__ == "__main__":
    make_wkk_logo_transparent()
