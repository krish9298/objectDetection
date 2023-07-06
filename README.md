Object detection is a computer technology related to computer vision and image
processing that deals with detecting instances of semantic objects of a certain class
(such as humans, buildings, or cars) in digital images and videos. Well-researched
domains of object detection include face detection and pedestrian detection. Object detection has applications in many areas of computer vision, including image
retrieval and video surveillance. Every object class has its own special features that
helps in classifying the class for example all circles are round. Object class detection
uses these special features. For example, when looking for circles, objects that are
at a particular distance from a point (i.e. the center) are sought. Similarly, when
looking for squares, objects that are perpendicular at corners and have equal side
lengths are needed. A similar approach is used for face identification where eyes,
nose, and lips can be found and features like skin color and distance between eyes
can be found. In deep learning, a convolutional neural network (CNN, or ConvNet)
is a class of deep neural networks, most commonly applied to analyzing visual imagery.
The algorithm we used for the object detection model is the Faster RCNN Inception v2. RCNN stands for Region Convolutional Neural Network, differentiating
from regular convolutional neural networks which are used for image classification,
whereas in this algorithm, there is another part to itthe region. In object detection,
an RCNN is used to focus on regions since determining the location of multiple
objects is essential to this type of model.
