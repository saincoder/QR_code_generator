import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator")

st.write("This application generates a QR code with a dark background for a given URL.")

# File uploader for user to input URL
url = st.text_input("Enter the URL")

if url:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='white', back_color=(0, 0, 0))

    # Save the image to a bytes buffer
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    st.image(buf, caption="Generated QR Code", use_column_width=True)

    # Option to download the image
    btn = st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="qrcode.png",
        mime="image/png"
    )
