import base64
import qrcode
from io import BytesIO

def generate_qr_code(data):
    """Generates a QR code from the given data and returns it as a base64-encoded string."""
    try:
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()
    except Exception as e:
        return None  # Handle errors in model logic
