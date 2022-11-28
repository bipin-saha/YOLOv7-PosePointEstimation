import os
import pandas as pd

unbalanced_csv_path = "labels2.csv"

augmented_file_path = "augmented/sitting"
image_lists = os.listdir(augmented_file_path)
#print(image_lists)

df = pd.read_csv(unbalanced_csv_path, names=["ImageName", "labels"])

for x in image_lists:
    df = df.append({'ImageName': x, 'labels':"sitting"}, ignore_index=True)

df.to_csv("balanced_keypoints.csv")