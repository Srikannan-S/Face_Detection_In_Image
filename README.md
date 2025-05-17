👤 Face Detection using OpenCV

A simple Python project that uses OpenCV and Haar Cascade to detect human faces in an image and highlight them with rectangles.

🔥 Features

1. Loads a pretrained Haar Cascade classifier for face detection  
2. Converts color images to grayscale for processing  
3. Detects all faces in the image  
4. Draws rectangles around detected faces  
5. Displays the final image with bounding boxes  

🚀 Technologies Used

1. Python – Programming language  
2. OpenCV – Library for image processing  
3. Haar Cascade – Pretrained face detection algorithm  

⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/face-detection-opencv.git
   cd face-detection-opencv
   ```

2. Install the required package:
   ```bash
   pip install opencv-python
   ```

3. Make sure the following files are in your project directory:
   - `cricket.jpg` (input image)
   - `haarcascade_frontalface_default.xml` (Haar cascade file, [download here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml))

4. Run the script:
   ```bash
   python app.py
   ```

🛠️ How It Works

- Loads the Haar Cascade face detection model.  
- Reads an image named `cricket.jpg`.  
- Converts the image to grayscale.  
- Uses `detectMultiScale()` to find face coordinates.  
- Draws red rectangles around each detected face.  
- Displays the output for 5 seconds before closing.  

📂 Project Structure

📁 face-detection-opencv  
├── app.py                        # Main Python script  
├── cricket.jpg                   # Input image (user-provided)  
├── haarcascade_frontalface_default.xml  # Face detection model  
└── README.md                     # Project documentation  
