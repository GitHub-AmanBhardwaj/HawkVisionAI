import streamlit as st
import os
from PIL import Image
import subprocess

st.set_page_config(page_title="HawkVisionAI", layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #2A3C44;  /* Dark Slate background */
            color: #F7F5EB;  /* Soft Cream text */
        }
        .stApp {
            background-color: #2A3C44;
        }
        .stButton>button {
            background-color: #547C84;  /* Slate Blue button */
            color: #F7F5EB;  /* Soft Cream text */
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #F7F5EB;  /* Soft Cream hover effect */
            color: #2A3C44;  /* Dark Slate text */
        }
        .stFileUploader>label {
            color: #A3BCC7;  /* Muted Blue Gray label color */
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #F7F5EB;  /* Soft Cream footer text */
        }
        .stMarkdown {
            color: #F7F5EB;  /* Soft Cream for instructions or titles */
        }
        .stImage {
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
        .header-text {
            font-size: 36px;
            font-weight: bold;
            color: #F7F5EB;  /* Soft Cream header */
            text-align: center;
            padding: 20px;
        }
        .subheader-text {
            font-size: 18px;
            color: #F7F5EB;  /* Soft Cream subheader */
            text-align: center;
            padding: 10px;
        }
        .stSuccess {
            color: #81C784;  /* Light Green for success messages */
        }
        .stError {
            color: #C94F3C;  /* Muted Red for error messages */
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<h1 class="header-text">ℍ𝕒𝕨𝕜𝕍𝕚𝕤𝕚𝕠𝕟𝔸𝕀</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="subheader-text">ᴛʀᴀɴꜱꜰᴏʀᴍᴀᴛɪᴏɴ ɨռƈօʍɨռɢ...</h1>', unsafe_allow_html=True)

source_image = st.file_uploader("Upload Source Image (Image to be swapped)", type=["jpg", "png", "jpeg"])
target_image = st.file_uploader("Upload Target Image (Image to receive the face)", type=["jpg", "png", "jpeg"])

if st.button("𝚂𝚝𝚊𝚛𝚝 𝚂𝚠𝚊𝚙𝚙𝚒𝚗𝚐"):
    if source_image and target_image:
        source_path = "source.jpg"
        target_path = "target.jpg"
        output_path = "output.jpg"

        # Save uploaded files to disk
        with open(source_path, "wb") as f:
            f.write(source_image.read())
        with open(target_path, "wb") as f:
            f.write(target_image.read())

        st.write("Processing, please wait...")

        # Use subprocess to capture both stdout and stderr
        command = ["python", "run.py", "--source", source_path, "--target", target_path, "--output", output_path]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check for errors in the process
        if process.returncode == 0 and os.path.exists(output_path):
            st.success("Swap Complete! Take a Look 😊")
            swapped_image = Image.open(output_path)
            st.image(swapped_image, caption="Final Image", use_column_width=True)

            # Prepare image for download
            with open(output_path, "rb") as f:
                img_bytes = f.read()

            st.download_button(
                label="Download Swapped Image",
                data=img_bytes,
                file_name="swapped_face.jpg",
                mime="image/jpeg"
            )
        else:
            # Display error messages if the face swapping fails
            st.error("An error occurred during face swapping.")
            st.error(f"Error details: {stderr.decode('utf-8')}")
            st.error(f"Command output: {stdout.decode('utf-8')}")
    else:
        st.error("Please upload both source and target images.")

# Footer
st.markdown("###")
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p> 𝙈𝙖𝙙𝙚 𝙬𝙞𝙩𝙝 ❤️ by 𝕋𝕦𝕣𝕚𝕟𝕘ℍ𝕚𝕧𝕖</p>
    </div>
    """, 
    unsafe_allow_html=True
)
