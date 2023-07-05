import os

folder_path = ""
yml_file_path = "portfolio.yml"

with open(yml_file_path, "a") as file:
    portfolio_text = ""
    for file_name in os.listdir("."):
        if file_name.endswith(".jpeg"):
            image_name = file_name[:-4]
            image_path = os.path.join(folder_path, file_name)
            webp_file_name = image_name + ".webp"
            webp_file_path = os.path.join(folder_path, webp_file_name)
            portfolio_text += f"- name: {image_name}\n"
            portfolio_text += f"  image: {image_path}\n"
            portfolio_text += f"  image_webp: {webp_file_path}\n"
            portfolio_text += f"  categories: [\"每日寄语\"]\n"
            portfolio_text += "\n"
    print(portfolio_text)   
    file.write(portfolio_text)