import base64
from io import BytesIO

import pyfiglet
from PIL import Image, ImageDraw, ImageFont, ImageText
from pyscript import when, web, document  # type: ignore # pylint: disable=import-error


TEXT = "Hello from Python"
FONT = "dos_rebel"
IMG_WIDTH = 1920
IMG_HEIGHT = 1080
BG_COLOR = "#000"
COLOR = "#0f0"
MONO_FONT = "./FiraCode-Regular.ttf"
WIDTH = 200
SIZE = 15


@when("click", "#save-button")
def generate():
    """Generate image"""
    image = Image.new(mode="RGB", size=(IMG_WIDTH, IMG_HEIGHT), color=BG_COLOR)
    text_input = str(web.page["text-input"].value)
    ascii_art = pyfiglet.figlet_format(text_input, font=FONT, width=WIDTH or 80)
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
    img_display = web.page["img-display"]
    img_display.src = img_to_base64(image)

    # Activate the download button after generating the image
    web.page["download-button"].disabled = False


def img_to_base64(img):
    """Function to convert image to base64"""
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    value = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{value}"


@when("click", "#download-button")
def download():
    """Function to download the generate image"""
    downloadlink = document.createElement("a")  # type: ignore
    downloadlink.download = "output.png"
    downloadlink.href = web.page["img-display"].src
    downloadlink.click()
