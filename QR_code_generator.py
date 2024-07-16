import streamlit as st
import qrcode
from PIL import Image
import io

# Title and developer name
st.title("QR Code Generator")
st.write("Developed by Shahid")

st.write("This application generates a QR code with a dark background for a given URL.")

# Input URL
url = st.text_input("Enter the URL")

# Generate button
if st.button("Generate QR Code"):
    if url:
        # Create QR code instance with smaller box_size
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,  # Smaller size
            border=2,    # Adjust border size if needed
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR code with a dark background
        img = qr.make_image(fill_color='white', back_color=(0, 0, 0))

        # Resize the image to 50x50 pixels
        img = img.resize((200, 200), Image.LANCZOS)

        # Save the image to a bytes buffer
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)

        # Display the QR code
        st.image(buf, caption="Generated QR Code", width=200)

        # Provide download button
        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a URL.")
