if __name__ == '__main__':
    face_recognition = FacceRecognition()
    face_recognition.train()
    predict_name = face_recognition.predict('image.jpg')
