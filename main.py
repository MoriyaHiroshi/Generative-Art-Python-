from PIL import Image, ImageDraw, ImageChops
import random
import colorsys

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_color_hsv():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

# This function will generate the artwork and will be reflected in a PNG file
def generate_art(path: str):
    print("Creating Art...")

    # Image Values & Setup
    image_px = 500
    image_size_px = (image_px, image_px)
    image_bg_color = (0, 0, 0)
    image = Image.new("RGB", image_size_px, image_bg_color)

    # Drawing on Image
    thickness = 0
    padding_px = 20 # This ensures that lines do not exceed outside the boundaries of the image
    for _ in range(20):
        randomPoint1 = (random.randint(padding_px, image_px - padding_px), random.randint(padding_px, image_px - padding_px))
        randomPoint2 = (random.randint(padding_px, image_px - padding_px), random.randint(padding_px, image_px - padding_px))

        # Overlay
        overlay_image = Image.new("RGB", image_size_px, image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        draw = ImageDraw.Draw(image)
        line_xy = (randomPoint1, randomPoint2)
        line_color = random_color()
        thickness = 10 
        overlay_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_image)
    # Updates image to PNG file
    
    image.save(path)



if __name__ == "__main__":
    generate_art("test_art.png")