import cv2


class FaceDetection:
    """
    Detect the face in photo.

    use detect() method for images.

    """
    def __init__(self, method='haarcascade'):
        if method == 'haarcascade':
            self.model = cv2.CascadeClassifier('model/haar/haarcascade_frontalface_default.xml')

    def detect(self, image):
        '''detect face in input image

        :param:image: numpy image.
        '''
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        return faces

    def draw_rectangle(self, image, faces_point):

        for (x,y,w,h) in faces_point:
            image = cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
            display('image', image)

    def display(window_name, image)
        cv2.imshow(window_name ,image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

