import tempfile
from ifnude import detect

def convert_to_sd(img):
    chunks = detect(img)
    shapes = [chunk["score"] > 0.7 for chunk in chunks]
    return [any(shapes), tempfile.NamedTemporaryFile(delete=False, suffix=".png")]
