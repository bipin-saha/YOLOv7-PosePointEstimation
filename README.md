# HTL_Intern_Task

I have tried to implement the ML Intern Task as mentioned [here](https://docs.google.com/document/d/1RQ8L73zms_umaN9q4OTx35Tb3i6pfqqK/edit).

According to the task desciption I have used Yolo V7 and Yolov7-w6-pose weight (.pt) file. The Yolov7 pose estimation points (COCO 17 Skeleton) are as follows

<a href="url"><img src="https://learnopencv.com/wp-content/uploads/2022/10/coco-17-skeleton-topology.png" align="middle" height="240"></a>

For the Task 1, [unbalanced_keypoints.csv](https://github.com/bipin-saha/HTL_Intern_Task/blob/main/unbalanced_keypoints.csv) the file structure is as follows
ImageName
Label
Keypoint Number(kp<sub>n</sub>)
X Coordinate(x<sub>n</sub>)
Y Coordinate(y<sub>n</sub>)
Prediction Strenght Value(v<sub>n</sub>)

For the Task 2, The documnet is mentioned to use SMOTE technique,
I have seracher thorughout the internet and hardly found any method to use SMOTE technique for Image Data.
There are two options suggested by several literatures for handaling unbalanced Image Dataset

* Image Augmentation
* Generative Adversarial Network (GAN)

GAN required huge amount of time for training and higly depended on hyperparameter tuning. As there is time constrains, that is why I followed the first technique of Image Augmentation.

For the image augmentation process using [Albumentation](https://albumentations.ai/), I have used 
  * HorizontalFlip
	* Lambda
	* Perspective
	* PiecewiseAffine

these four techniques, as the number of image required to match the higher number class is quite low. And finally used the same [Colab Notebook](https://github.com/bipin-saha/HTL_Intern_Task/blob/main/yolov7PoseEstimation.ipynb) for the key point extraction process for [balanced_keypoints.csv](https://github.com/bipin-saha/HTL_Intern_Task/blob/main/balanced_keypoints.csv).

You may find the augmented image with balanced dataset from here [Google Drive](https://drive.google.com/file/d/1mmjFhUePYOjAqf5xZ51aBKzOoObJsjXW/view?usp=share_link)
