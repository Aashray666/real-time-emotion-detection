import boto3
import os
import datetime
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate(r'C:\Users\aashr\Desktop\pblCC\code\online-class-emotion-firebase-adminsdk-fbsvc-e72260fd4d.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://online-class-emotion-default-rtdb.firebaseio.com/'
})

# AWS Rekognition client
rekognition = boto3.client('rekognition')

# Directory with images
img_dir = r'C:\Users\aashr\Desktop\pblCC\images'

# Firebase reference
ref = db.reference('emotion_data')

# Loop through all images
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(img_dir, filename)
        with open(img_path, 'rb') as image_file:
            bytes_data = image_file.read()
        
        response = rekognition.detect_faces(
            Image={'Bytes': bytes_data},
            Attributes=['ALL']
        )
        
        if response['FaceDetails']:
            emotions = response['FaceDetails'][0]['Emotions']
            top_emotion = max(emotions, key=lambda x: x['Confidence'])
            emotion_label = top_emotion['Type'].lower()
            confidence = top_emotion['Confidence']
            
            data = {
                "student": filename.split('.')[0],  # or hardcode e.g., 'Student 1'
                "emotion": emotion_label,
                "confidence": confidence,
                "timestamp": datetime.datetime.now().isoformat()
            }

            ref.push(data)
            print(f"✅ {filename}: {emotion_label} ({confidence:.2f}%) - Uploaded to Firebase")
        else:
            print(f"⚠️ {filename}: No face detected.")
