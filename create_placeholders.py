from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, text, width=600, height=300, bg_color=(240, 244, 248), text_color=(26, 54, 93)):
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([5, 5, width-5, height-5], outline=text_color, width=3)
    
    # Try loading default font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        
    # Draw text centered
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((width - w) / 2, (height - h) / 2), text, fill=text_color, font=font)
    
    img.save(filename)
    print(f"Created placeholder: {filename}")

if __name__ == "__main__":
    create_placeholder("logo.png", "IILM University Logo Placeholder", width=300, height=300)
    create_placeholder("architecture_diagram.png", "KDI Power System Architecture Diagram", width=800, height=450)
    create_placeholder("image.png", "B2B Lead Intelligence Workflow Pipeline", width=800, height=450)
    create_placeholder("dashboard.png", "KDI Power WhatsApp Sales Dashboard UI", width=800, height=450)
