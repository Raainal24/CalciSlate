import requests

from config import SOLVE_ENDPOINT, REQUEST_TIMEOUT


def solve_image(image_path):
    """
    Sends image to HPC server.

    Returns JSON.
    """

    with open(image_path, "rb") as image:

        files = {
            "file": image
        }

        response = requests.post(
            SOLVE_ENDPOINT,
            files=files,
            timeout=REQUEST_TIMEOUT
        )

    response.raise_for_status()

    return response.json()