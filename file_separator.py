import os
import shutil
import pandas as pd

unbalanced_image_path = "dataset/unbalanced/"
running_image_path = "dataset/running/"
sitting_image_path = "dataset/sitting/"
sleeping_image_path = "dataset/sleeping/"
csv_path = "labels.csv"

#image_files = os.listdir(unbalanced_image_path)

df = pd.read_csv(csv_path, names=["ImageName", "labels"])

running_df = df[df['labels'] == "running"]
sitting_df = df[df['labels'] == "sitting"]
sleeping_df = df[df['labels'] == "sleeping"]

#print(list(running_df["ImageName"]))

for x in range(len(list(sleeping_df["ImageName"]))):
    source_image_path = os.path.join(unbalanced_image_path, list(sleeping_df["ImageName"])[x])
    dest_image_path = os.path.join(sleeping_image_path, list(sleeping_df["ImageName"])[x])
    shutil.copyfile(source_image_path, dest_image_path)

#print(list(running_df["ImageName"]))