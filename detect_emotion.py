import boto3
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Initialize Firebase Admin SDK with your service account credentials
cred = credentials.Certificate(r'C:\Users\aashr\Desktop\pblCC\code\online-class-emotion-firebase-adminsdk-fbsvc-e72260fd4d.json')  # Full path to the Firebase private key JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://online-class-emotion-default-rtdb.firebaseio.com/'  # Your Firebase Realtime Database URL
})

# Initialize Rekognition client
rekognition = boto3.client("rekognition", region_name="us-east-1")

# Emotion mapping based on Rekognition labels
emotion_map = {
    "HAPPY": "happy",
    "BORED": "bored",
    "CONFUSED": "confused",
}

# Read image
with open("frame.jpg", "rb") as image_file:
    image_bytes = image_file.read()

# Call detect_faces
response = rekognition.detect_faces(
    Image={'Bytes': image_bytes},
    Attributes=['ALL']
)

# Extract emotion
face_details = response['FaceDetails']

if not face_details:
    print("❌ No face detected.")
else:
    emotions = face_details[0]['Emotions']
    
    # Sort emotions by confidence
    top_emotion = sorted(emotions, key=lambda x: x['Confidence'], reverse=True)[0]
    top_emotion_type = top_emotion['Type']
    top_emotion_confidence = top_emotion['Confidence']

    # Check if the confidence is high enough (above 80%)
    if top_emotion_confidence >= 80:
        # Map the detected emotion to our simplified set
        mapped_emotion = emotion_map.get(top_emotion_type, "neutral")
        print(f"😃 Detected Emotion: {mapped_emotion} ({top_emotion_confidence:.2f}%)")
    else:
        print(f"❓ Emotion confidence too low: {top_emotion_confidence:.2f}%. Marking as neutral.")
        mapped_emotion = "neutral"

    # Push emotion data to Firebase Realtime Database
    student_name = "Student 1"  # You can modify this based on your app or classroom setup
    timestamp = datetime.now().isoformat()

    emotion_data = {
        "student": student_name,
        "emotion": mapped_emotion,
        "confidence": top_emotion_confidence,
        "timestamp": timestamp
    }

    # Store the emotion data under a unique ID (could be based on timestamp or UUID)
    ref = db.reference('emotion_data')
    ref.push(emotion_data)

    print(f"✅ Emotion data pushed to Firebase: {emotion_data}")
