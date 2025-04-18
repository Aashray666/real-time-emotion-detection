import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import time

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'')  # Path to your Firebase key
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

# Fetch emotion data from Firebase Realtime Database
ref = db.reference('emotion_data')

# Function to fetch latest data
def fetch_emotion_data():
    data = ref.get()
    if data:
        df = pd.DataFrame(data).T  # Transpose for easier viewing
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    else:
        return pd.DataFrame(columns=['student', 'emotion', 'confidence', 'timestamp'])

# Streamlit components to display data
st.title('Real-time Emotion Detection Dashboard')

# Show latest emotion data
st.header('Latest Emotion Data')

df = fetch_emotion_data()

if not df.empty:
    latest_data = df.iloc[-1]  # Latest emotion entry
    st.write(f"**Student:** {latest_data['student']}")
    st.write(f"**Emotion:** {latest_data['emotion']}")
    st.write(f"**Confidence:** {latest_data['confidence']:.2f}%")
    st.write(f"**Timestamp:** {latest_data['timestamp']}")
else:
    st.write("No emotion data available.")

# Show full data in a table
st.header('All Emotion Data')
st.write(df)

# Analytics Section
st.header('Emotion Trends')

if not df.empty:
    emotion_counts = df['emotion'].value_counts()  # Count each emotion
    st.write(f"Emotion Counts: {emotion_counts}")

    # Optional: Bar chart visualization of emotions
    st.bar_chart(emotion_counts)
else:
    st.write("No emotion data available for analytics.")

# Add real-time updates (Auto-refresh every 10 seconds)
st.text("The data will auto-update every 10 seconds.")
time.sleep(10)
st.experimental_rerun()
