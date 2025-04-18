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
img_dir = r'C:\Users\aashr\Desktop\pblCC\test'

# Firebase reference
ref = db.reference('emotion_data')

# Mapping AWS emotions into custom categories
def classify_emotion(emotion_type):
    happy_keywords = ['HAPPY']
    bored_keywords = ['SAD', 'DISGUSTED']
    confused_keywords = ['CONFUSED', 'SURPRISED']
    neutral_keywords = ['CALM', 'UNKNOWN']

    if emotion_type in happy_keywords:
        return 'happy'
    elif emotion_type in bored_keywords:
        return 'bored'
    elif emotion_type in confused_keywords:
        return 'confused'
    elif emotion_type in neutral_keywords:
        return 'neutral'
    else:
        return 'neutral'

# Loop through all images
for filename in os.listdir(img_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
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
            raw_emotion = top_emotion['Type']
            final_emotion = classify_emotion(raw_emotion)
            confidence = top_emotion['Confidence']

            data = {
                "student": filename.split('.')[0],
                "emotion": final_emotion,
                "confidence": confidence,
                "timestamp": datetime.datetime.now().isoformat()
            }

            ref.push(data)
            print(f"✅ {filename}: 😃 {final_emotion.upper()} ({confidence:.2f}%) - Uploaded to Firebase")
        else:
            print(f"⚠️ {filename}: No face detected.")
