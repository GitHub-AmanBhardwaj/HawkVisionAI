import subprocess

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

        # Use subprocess to capture both stdout and stderr
        command = ["python", "run.py", "--source", source_path, "--target", target_path, "--output", output_path]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check for errors in the process
        if process.returncode == 0 and os.path.exists(output_path):
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
            st.error(f"An error occurred during face swapping. Error details: {stderr.decode('utf-8')}")
            st.error(f"Command output: {stdout.decode('utf-8')}")
    else:
        st.error("Please upload both source and target images.")
