import qrcode
from io import BytesIO
from base64 import b64encode
from django_otp.plugins.otp_totp.models import TOTPDevice



def generate_totp_qr_code(user):
    """
    Generates a TOTP QR code for the user, to be scanned by an authenticator app.
    :param user: The user for whom to generate the QR code.
    :return: A base64-encoded string representing the QR code.
    """
    # Create a TOTP device for the user, which contains the TOTP secret
    device, created = TOTPDevice.objects.get_or_create(user=user, confirmed=False)
    otp_url = device.config_url  # The URL to be embedded in the QR code

    # Generate the QR code from the OTP URL
    qr = qrcode.make(otp_url)
    stream = BytesIO()
    qr.save(stream, "PNG")
    
    # Convert the QR code to base64 so it can be rendered in HTML
    qr_code_base64 = b64encode(stream.getvalue()).decode()
    return qr_code_base64


