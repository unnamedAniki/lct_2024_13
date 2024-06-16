import pandas as pd
from PIL import ImageDraw, ImageFont
from PIL import Image
from settings import dataset_path, short_product_name, background_path
import os


def get_files_for_product(product_name):
    dataset = pd.read_excel(dataset_path)
    filtered_df = dataset[dataset["Продукт"] == short_product_name[product_name]]
    file_names = filtered_df["Название_файла "].tolist()
    file_info = []
    for file_name in file_names:
        if not file_name.startswith("Mega"):
            file_path = os.path.join(background_path, f"{file_name}.png")
            if os.path.exists(file_path):
                with Image.open(file_path) as img:
                    width, height = img.size
                    file_info.append((file_name, width, height))

    return file_info
