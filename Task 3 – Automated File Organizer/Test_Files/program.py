import cv2
import matplotlib.pyplot as plt
# Read the image. OpenCV loads a colour image in BGR order.
img_bgr = cv2.imread("butterfly.jpg")
# Check whether the image was loaded successfully.
if img_bgr is None:
raise FileNotFoundError("butterfly.jpg was not found. Upload it first.")
# Convert BGR to RGB because Matplotlib displays colour as RGB.
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# Convert the original BGR image to a single-channel grayscale image.
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# Display the colour and grayscale images side by side.
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.tight_layout()
plt.show()
# Save both outputs. Convert RGB back to BGR before saving with OpenCV.
cv2.imwrite("butterfly_rgb_output.jpg",
cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
cv2.imwrite("butterfly_grayscale_output.jpg", gray)
print("Both images were saved successfully.")
