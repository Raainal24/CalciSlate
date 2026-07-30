from PIL import ImageGrab

from config import SCREENSHOT_PATH


def capture_canvas(canvas):
    """
    Capture only the drawing canvas.
    Returns the saved image path.
    """

    canvas.update()

    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    image = ImageGrab.grab(bbox=(x, y, x1, y1))

    image.save(SCREENSHOT_PATH)

    return SCREENSHOT_PATH