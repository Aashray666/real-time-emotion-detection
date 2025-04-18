# 🎓 Emotion Detection for Online Classes using AWS Rekognition and Firebase

This project detects human emotions from facial expressions using AWS Rekognition and stores the results in a Firebase Realtime Database. It is designed primarily for monitoring student engagement in online learning environments by analyzing bulk images from classroom snapshots or individual webcam captures.

---

## 📌 Features

- 🤖 **Facial Emotion Recognition** using AWS Rekognition
- 🔥 **Firebase Integration** for real-time data storage
- ✅ Detects emotions like `HAPPY`, `SAD`, `ANGRY`, `CALM`, `SURPRISED`, `CONFUSED`, and `DISGUSTED`
- 💾 Stores emotion data with timestamp and confidence score
- 🔍 Logs each result with appropriate feedback

---

## 📂 Project Structure

```
project-root/
│
├── images/                      # Folder containing input images
├── code/
│   ├── detect_emotion.py        # Main script to detect and push emotions
│   ├── serviceAccountKey.json   # Firebase credentials file
│   └── requirements.txt         # Python dependencies
├── README.md                    # Project documentation
└── screenshots/                 # Output screenshot folder
```

---

## 🚀 Technologies Used

- **AWS Rekognition** – for facial analysis and emotion detection
- **Firebase Realtime Database** – to store emotion results in real-time
- **Python 3.x**
- **OpenCV** – for image preprocessing (optional, but useful)
- **Boto3** – to interact with AWS Rekognition
- **firebase-admin** – to interact with Firebase

---

## 🛠️ Installation

### 1. Clone the repository

### 2. Set up a virtual environment (recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS

Run the following to configure AWS credentials:

```bash
aws configure
```

You'll need to provide your **AWS Access Key ID**, **Secret Access Key**, region (e.g., `us-east-1`), and output format (`json`).

---

## 🔑 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a project and navigate to **Project Settings > Service Accounts**
3. Generate a private key (`serviceAccountKey.json`)
4. Save the file in the `code/` directory
5. Update the Firebase URL inside the Python script (`detect_emotion.py`)

---

## 📸 How to Use

1. Add your test images in the `images/` folder.
2. Run the script:

```bash
python detect_emotion.py
```

3. Output will display detected emotions and upload confirmation.
4. Check Firebase Realtime Database to see the pushed data.

---

## 📊 Sample Output (Firebase Entry)

```json
{
  "student": "student1",
  "emotion": "happy",
  "confidence": 98.65,
  "timestamp": "2025-04-17T20:04:15.226940"
}
```

## 📈 Future Enhancements

- Real-time webcam integration using OpenCV
- Live dashboard for visualizing engagement
- Multi-label emotion detection
- Integration with classroom platforms like Google Meet or Zoom

---

## 📄 License

This project is for academic use only and not intended for commercial deployment without permission.

---

## 🤝 Acknowledgements

- AWS Rekognition
- Firebase by Google
- Python Community

---

Feel free to fork, modify, and submit a pull request. Happy coding! 😄
```

---

Let me know if you'd like to include a project logo, GitHub badges, or add deployment instructions (e.g., Streamlit, web integration).
