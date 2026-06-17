from pyscript import when, display, web  # type: ignore # pylint: disable=import-error

import pyfiglet
from PIL import Image, ImageDraw, ImageFont, ImageText

TEXT = "Hello from Python"
FONT = "dos_rebel"
IMG_WIDTH = 1920
IMG_HEIGHT = 1080
BG_COLOR = "#000"
COLOR = "#0f0"
MONO_FONT = ""
WIDTH = 200
SIZE = 20


@when("click", "#figlet-button")
def handle():
    """Show figlet in page"""
    text = pyfiglet.figlet_format(text=TEXT, font=FONT, width=WIDTH)
    figlet_div = web.page["figlet-output"]
    figlet_div.textContent = text
    print(text)


@when("click", "#save-button")
def generate():
    """Generate image"""
    image = Image.new(mode="RGB", size=(IMG_WIDTH, IMG_HEIGHT), color=BG_COLOR)
    ascii_art = pyfiglet.figlet_format(TEXT, font=FONT, width=WIDTH or 80)
    # A monospaced font is needed in this case, because the characters might be missaligned otherwise
    font = ImageFont.truetype(font=MONO_FONT, size=SIZE)
    text = ImageText.Text(ascii_art, font)

    bbox = text.get_bbox()
    # Calculate the position for the text to be in the center of the image
    x = (IMG_WIDTH - bbox[2]) // 2
    y = (IMG_HEIGHT - bbox[3]) // 2

    final = ImageDraw.Draw(image)
    # Write the text to the image
    final.text((x, y), text, COLOR)

    # Preview the image
    display(image)
