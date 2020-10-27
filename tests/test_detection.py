
from pytest_bdd import scenario, given, when, then

from face_recognition.face_detection import FaceDetection


@scenario('face_recognition.face_detection', 'Publishing the article')
def test_publish():
    pass


@given("I'm an author user")
def author_user(faces):
    detection = FaceDetection()
    image = cv2.imread('images/test1.jpg')
    faces = detection.detect(image)


@then("the article should be published")
def article_is_published(faces):
    assert len(faces) == 2
