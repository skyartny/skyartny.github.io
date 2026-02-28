import textwrap
from PIL import Image, ImageDraw, ImageFont
import os

# --- Configuration ---
WIDTH, HEIGHT = 1000, 1400  # Canvas Size
BG_COLOR = (255, 255, 255)
DEVICE_COLOR = (245, 245, 247)  # Light gray for device body
STROKE_COLOR = (200, 200, 200)  # Light gray for outlines
TEXT_COLOR = (50, 50, 50)       # Dark gray for text
ACCENT_COLOR_IOS = (0, 122, 255) # iOS Blue
ACCENT_COLOR_ANDROID = (66, 133, 244) # Android Blue
SHADOW_COLOR = (0, 0, 0, 30)    # Transparent black for shadow

# Fonts
try:
    # Try to load a nice system font (San Francisco or Arial)
    FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
    if not os.path.exists(FONT_PATH):
        FONT_PATH = "/Library/Fonts/Arial.ttf"
    if not os.path.exists(FONT_PATH):
        FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" # Linux fallback
    
    title_font = ImageFont.truetype(FONT_PATH, 60)
    body_font = ImageFont.truetype(FONT_PATH, 30)
    small_font = ImageFont.truetype(FONT_PATH, 24)
    icon_font = ImageFont.truetype(FONT_PATH, 50)
except Exception:
    title_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()
    icon_font = ImageFont.load_default()

def create_base_image():
    return Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)

def draw_shadow(draw, xy, radius, offset=(10, 10), color=SHADOW_COLOR):
    shadow_xy = [x + o for x, o in zip(xy, offset * 2)]
    # Create a separate image for shadow to handle alpha properly if needed, 
    # but for simple shapes on white bg, drawing directly with alpha color works if image is RGBA.
    # Since base is RGB, we need an overlay.
    pass # implemented in main draw loop by drawing shadow first

def draw_rounded_rect_shadow(img, xy, radius, color, shadow_color=SHADOW_COLOR, shadow_offset=(10, 10)):
    # Create a transparent overlay for shadow
    shadow_layer = Image.new("RGBA", img.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    
    x0, y0, x1, y1 = xy
    sx, sy = shadow_offset
    
    shadow_draw.rounded_rectangle(
        (x0 + sx, y0 + sy, x1 + sx, y1 + sy),
        radius=radius,
        fill=shadow_color
    )
    
    # Composite shadow
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow_layer), (0,0))
    
    # Draw main rect
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(xy, radius=radius, fill=color)
    return img

def create_ios_guide():
    img = create_base_image().convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    # Phone Outline
    phone_margin = 150
    phone_rect = (phone_margin, 200, WIDTH - phone_margin, HEIGHT - 100)
    draw.rounded_rectangle(phone_rect, radius=60, outline=STROKE_COLOR, width=4)
    
    # Browser Bar (Bottom)
    bar_height = 120
    bar_y = phone_rect[3] - bar_height
    draw.line([(phone_rect[0], bar_y), (phone_rect[2], bar_y)], fill=STROKE_COLOR, width=2)
    
    # URL Bar (Abstract)
    url_rect = (phone_rect[0] + 40, bar_y + 30, phone_rect[2] - 40, bar_y + 90)
    draw.rounded_rectangle(url_rect, radius=20, fill=(240, 240, 240))
    
    # Share Icon (Center Bottom) - Abstract Square with Arrow
    share_icon_size = 50
    cx = (phone_rect[0] + phone_rect[2]) // 2
    cy = bar_y + bar_height // 2 + 60 # Below the URL bar area in a real UI, but for abstract guide, let's put it in the "toolbar" area below URL
    
    # Re-adjust: Safari usually has URL bar at bottom (new) or top (old). 
    # Let's do the "Bottom Tab Bar" style which is current.
    # Tab Bar is at the very bottom.
    tab_bar_y = phone_rect[3] - 100
    
    # Share Icon is usually center in the toolbar
    share_x = cx
    share_y = tab_bar_y + 50
    
    # Draw Share Icon (Square + Arrow)
    # Box
    box_w, box_h = 40, 40
    draw.rectangle(
        (share_x - box_w/2, share_y - box_h/2, share_x + box_w/2, share_y + box_h/2), 
        outline=ACCENT_COLOR_IOS, width=3
    )
    # Arrow
    draw.line(
        [(share_x, share_y - box_h/2 + 10), (share_x, share_y - box_h/2 - 25)], 
        fill=ACCENT_COLOR_IOS, width=3
    )
    draw.line(
        [(share_x, share_y - box_h/2 - 25), (share_x - 15, share_y - box_h/2 - 10)], 
        fill=ACCENT_COLOR_IOS, width=3
    )
    draw.line(
        [(share_x, share_y - box_h/2 - 25), (share_x + 15, share_y - box_h/2 - 10)], 
        fill=ACCENT_COLOR_IOS, width=3
    )
    
    # Step 1 Label
    draw.text((share_x + 60, share_y - 15), "1. Tap Share", font=body_font, fill=TEXT_COLOR)
    
    # Popup Menu (Sheet)
    sheet_h = 500
    sheet_y = phone_rect[3] - sheet_h
    sheet_rect = (phone_rect[0] + 20, sheet_y, phone_rect[2] - 20, phone_rect[3] - 20)
    
    # Draw shadow for sheet
    shadow_layer = Image.new("RGBA", img.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    shadow_draw.rounded_rectangle(
        (sheet_rect[0]+10, sheet_rect[1]+10, sheet_rect[2]+10, sheet_rect[3]+10), 
        radius=30, fill=(0,0,0,40)
    )
    img = Image.alpha_composite(img, shadow_layer)
    draw = ImageDraw.Draw(img)
    
    # Draw Sheet
    draw.rounded_rectangle(sheet_rect, radius=30, fill="white", outline=STROKE_COLOR, width=1)
    
    # "Add to Home Screen" Item
    item_h = 80
    item_y = sheet_y + 250
    
    # Highlight box
    draw.rounded_rectangle(
        (sheet_rect[0] + 20, item_y, sheet_rect[2] - 20, item_y + item_h),
        radius=15, fill=(240, 245, 255)
    )
    
    # Icon (Plus in square)
    plus_box_x = sheet_rect[0] + 60
    plus_box_y = item_y + item_h // 2
    draw.rectangle(
        (plus_box_x - 15, plus_box_y - 15, plus_box_x + 15, plus_box_y + 15),
        outline=ACCENT_COLOR_IOS, width=2
    )
    draw.line([(plus_box_x, plus_box_y - 10), (plus_box_x, plus_box_y + 10)], fill=ACCENT_COLOR_IOS, width=2)
    draw.line([(plus_box_x - 10, plus_box_y), (plus_box_x + 10, plus_box_y)], fill=ACCENT_COLOR_IOS, width=2)
    
    # Text
    draw.text((plus_box_x + 40, item_y + 25), "Add to Home Screen", font=body_font, fill=TEXT_COLOR)
    
    # Step 2 Label (Pointer)
    draw.text((sheet_rect[2] + 20, item_y + 20), "2. Select", font=body_font, fill=TEXT_COLOR)
    draw.line([(sheet_rect[2], item_y + 40), (sheet_rect[2] + 15, item_y + 40)], fill=TEXT_COLOR, width=1)

    # "Add" Button (Top Right of sheet or modal)
    # Actually, after tapping "Add to Home Screen", a new modal appears with "Add" in top right.
    # We can visualize this abstractly by showing a "Confirm" button.
    # Let's just put an "Add" button at the top right of this sheet for simplicity/abstraction,
    # or draw a second mini-modal.
    # Prompt says: "Image 1: iOS Installation ... 4. 'Add' button"
    
    # Let's draw a small "Add" button in the top right corner of the sheet (simulating the next screen)
    add_btn_x = sheet_rect[2] - 80
    add_btn_y = sheet_y + 40
    draw.text((add_btn_x, add_btn_y), "Add", font=body_font, fill=ACCENT_COLOR_IOS)
    
    # Step 3 Label
    draw.text((add_btn_x + 60, add_btn_y), "3. Tap Add", font=body_font, fill=TEXT_COLOR)
    
    # Header Text
    draw.text((50, 50), "iOS Installation", font=title_font, fill=TEXT_COLOR)
    draw.text((50, 120), "Safari Browser", font=body_font, fill=(150, 150, 150))
    
    # Save
    img.save("ios_install.png")
    print("Created ios_install.png")

def create_android_guide():
    img = create_base_image().convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    # Phone Outline
    phone_margin = 150
    phone_rect = (phone_margin, 200, WIDTH - phone_margin, HEIGHT - 100)
    draw.rounded_rectangle(phone_rect, radius=60, outline=STROKE_COLOR, width=4)
    
    # Browser Bar (Top) - Chrome Style
    bar_height = 100
    bar_y = phone_rect[1] + 40
    
    # URL Bar container
    draw.rounded_rectangle(
        (phone_rect[0] + 20, bar_y, phone_rect[2] - 20, bar_y + bar_height),
        radius=20, fill=(240, 240, 240)
    )
    
    # Menu Icon (3 dots) - Top Right
    menu_x = phone_rect[2] - 60
    menu_y = bar_y + bar_height // 2
    
    dot_radius = 4
    for i in range(-1, 2):
        draw.ellipse(
            (menu_x - dot_radius, menu_y + i*15 - dot_radius, menu_x + dot_radius, menu_y + i*15 + dot_radius),
            fill=ACCENT_COLOR_ANDROID
        )
        
    # Step 1 Label
    draw.text((menu_x + 40, menu_y - 15), "1. Tap Menu", font=body_font, fill=TEXT_COLOR)
    
    # Menu Dropdown
    menu_w = 400
    menu_h = 500
    menu_rect = (phone_rect[2] - menu_w - 30, bar_y + bar_height + 10, phone_rect[2] - 30, bar_y + bar_height + 10 + menu_h)
    
    # Shadow
    shadow_layer = Image.new("RGBA", img.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    shadow_draw.rounded_rectangle(
        (menu_rect[0]+10, menu_rect[1]+10, menu_rect[2]+10, menu_rect[3]+10), 
        radius=10, fill=(0,0,0,40)
    )
    img = Image.alpha_composite(img, shadow_layer)
    draw = ImageDraw.Draw(img)
    
    # Menu Box
    draw.rounded_rectangle(menu_rect, radius=10, fill="white", outline=STROKE_COLOR, width=1)
    
    # "Install App" Item
    item_h = 70
    item_y = menu_rect[1] + 200 # Midway down
    
    # Highlight
    draw.rectangle(
        (menu_rect[0], item_y, menu_rect[2], item_y + item_h),
        fill=(240, 245, 255)
    )
    
    # Icon (Phone with arrow or just arrow)
    icon_x = menu_rect[0] + 40
    icon_y = item_y + item_h // 2
    draw.rectangle(
        (icon_x - 10, icon_y - 15, icon_x + 10, icon_y + 15),
        outline=ACCENT_COLOR_ANDROID, width=2
    )
    draw.line([(icon_x, icon_y), (icon_x, icon_y + 8)], fill=ACCENT_COLOR_ANDROID, width=2)
    
    # Text
    draw.text((icon_x + 40, item_y + 20), "Install App", font=body_font, fill=TEXT_COLOR)
    
    # Step 2 Label
    draw.text((menu_rect[0] - 140, item_y + 20), "2. Select Install", font=body_font, fill=TEXT_COLOR)
    draw.line([(menu_rect[0] - 10, item_y + 35), (menu_rect[0], item_y + 35)], fill=TEXT_COLOR, width=1)
    
    # Confirmation Dialog (Center)
    confirm_w, confirm_h = 500, 250
    cx, cy = (phone_rect[0] + phone_rect[2]) // 2, (phone_rect[1] + phone_rect[3]) // 2 + 200
    confirm_rect = (cx - confirm_w//2, cy - confirm_h//2, cx + confirm_w//2, cy + confirm_h//2)
    
    # Shadow
    shadow_layer = Image.new("RGBA", img.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    shadow_draw.rounded_rectangle(
        (confirm_rect[0]+10, confirm_rect[1]+10, confirm_rect[2]+10, confirm_rect[3]+10), 
        radius=20, fill=(0,0,0,40)
    )
    img = Image.alpha_composite(img, shadow_layer)
    draw = ImageDraw.Draw(img)
    
    # Dialog Box
    draw.rounded_rectangle(confirm_rect, radius=20, fill="white", outline=STROKE_COLOR, width=1)
    
    # Title
    draw.text((confirm_rect[0] + 30, confirm_rect[1] + 30), "Install app?", font=body_font, fill=TEXT_COLOR)
    
    # Install Button
    btn_w, btn_h = 150, 60
    btn_x = confirm_rect[2] - btn_w - 30
    btn_y = confirm_rect[3] - btn_h - 30
    
    draw.rounded_rectangle(
        (btn_x, btn_y, btn_x + btn_w, btn_y + btn_h),
        radius=30, fill=ACCENT_COLOR_ANDROID
    )
    draw.text((btn_x + 40, btn_y + 15), "Install", font=body_font, fill="white")
    
    # Step 3 Label
    draw.text((confirm_rect[2] + 20, btn_y + 15), "3. Confirm", font=body_font, fill=TEXT_COLOR)
    
    # Header Text
    draw.text((50, 50), "Android Installation", font=title_font, fill=TEXT_COLOR)
    draw.text((50, 120), "Chrome Browser", font=body_font, fill=(150, 150, 150))
    
    # Save
    img.save("android_install.png")
    print("Created android_install.png")

if __name__ == "__main__":
    create_ios_guide()
    create_android_guide()
