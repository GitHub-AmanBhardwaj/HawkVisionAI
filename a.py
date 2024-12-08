import os
import subprocess
import sys

# List of packages to check and install
packages = [
    'streamlit',
    'opencv-python',
    'pillow',
    'numpy',
    'onnx',
    'onnxruntime',
    'insightface',
    'psutil',
    'tk',
    'customtkinter',
    'tkinterdnd2',
    'tensorflow',
    'opennsfw2',
    'protobuf',
    'tqdm',
    'gfpgan'
]

# Function to install packages
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Error installing {package}")

# Check and install each package
for package in packages:
    install_package(package)



import streamlit as st
import os
from PIL import Image

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
# st.title("ℍ𝕒𝕨𝕜𝕍𝕚𝕤𝕚𝕠𝕟𝔸𝕀")
st.markdown('<h1 class="subheader-text">ᴛʀᴀɴꜱꜰᴏʀᴍᴀᴛɪᴏɴ ɨռƈօʍɨռɢ...</h1>', unsafe_allow_html=True)
# st.markdown("### ᴛʀᴀɴꜱꜰᴏʀᴍᴀᴛɪᴏɴ ɨռƈօʍɨռɢ...")
st.markdown("\n")

source_image = st.file_uploader("Upload Source Image (Image to be swapped)", type=["jpg", "png", "jpeg"])
target_image = st.file_uploader("Upload Target Image (Image to receive the face)", type=["jpg", "png", "jpeg"])

if st.button("𝚂𝚝𝚊𝚛𝚝 𝚂𝚠𝚊𝚙𝚙𝚒𝚗𝚐"):
    if source_image and target_image:   

        source_path = "source.jpg"
        target_path = "target.jpg"
        output_path = "output.jpg"

        with open(source_path, "wb") as f:
            f.write(source_image.read())
        with open(target_path, "wb") as f:
            f.write(target_image.read())

        st.write("Processing , please wait...")
        command = f"python run.py --source {source_path} --target {target_path} --output {output_path}"
        result = os.system(command)

        if result == 0 and os.path.exists(output_path):
            st.success("Swap Complete! Take a Look 😊")
            swapped_image = Image.open(output_path)
            st.image(swapped_image, caption="Final Image", use_column_width=True)

            with open(output_path, "rb") as f:
                img_bytes = f.read()

            st.download_button(
                label="Download Swapped Image",
                data=img_bytes,
                file_name="swapped_face.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("An error occurred during face swapping.")
    else:
        st.error("Please upload both source and target images.")

st.markdown("""
    <div>
        <h2 align="center">Why Choose us?</h2>
        <br>
        No Login Required:
        Jump straight into the action—upload, swap, and download without signing up.
        <br><br>
        Unlimited Face Swaps:
        Experiment without limits. There are no restrictions on the number of swaps you can perform.
        <br><br>
        Advanced AI Technology:
        Powered by cutting-edge machine learning models, FaceSwapper ensures precise face alignment and realistic results.
        <br><br>
        User-Friendly Interface:
        No technical skills required, Our intuitive interface makes face-swapping simple for everyone.
        <br><br>
        Privacy First:
        Your images are processed securely. We never store or share your files.
        <br>
        <br>
        <br>
        <br>
        <h2>How It Works</h2>
    </div>
            """
,
unsafe_allow_html=True
)  

st.image("a.jpg", caption="How It Works", use_column_width=True, 
         clamp=True, channels="RGB", output_format="JPEG")

st.markdown("""
    <div>
        Step 1: Upload the source image (the face to replace).<br>
        Step 2: Upload the target image (where the face will be swapped).<br>
        Step 3: Click "Start Swapping" and let our AI do the rest!<br>
        Step 4: Download your high-quality face-swapped image instantly.<br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <h2>Features You'll Love</h2>
        ✅ High-Resolution Outputs<br>
        -Enjoy crisp, clear images without sacrificing quality.<br>
        ✅ Fast Processing<br>
        -Experience lightning-fast face swaps in seconds.<br>
        ✅ Cross-Platform Access<br>
        -Use FaceSwapper on desktop, tablet, or mobile—anytime, anywhere.<br>
        ✅ Customizable Options<br>
        -Adjust face blending settings to match your vision perfectly.<br>

    </div>

""",
unsafe_allow_html=True
)

st.markdown("")
st.markdown("---")
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
