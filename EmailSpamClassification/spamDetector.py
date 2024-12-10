import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
  speak= Dispatch(("SAPI.SpVoice"))
  speak.Speak(text)
model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))

def main():
  st.title("Email Spam Classification Apps")
  st.subheader("Build with Streamlit & python")
  msg=st.text_input("Enter a Text: ")
  if st.button("predict"):
     data=[msg]
     vect=cv.transform(data).toarray()
     prediction=model.predict(vect)
     result=prediction[0]
     if result==1:
        st.error("this is a spam mail")
        speak("this is a spam mail")
     else:
        st.success("this is a ham mail")
main()