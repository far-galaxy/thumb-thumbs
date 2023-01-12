import os
from PIL import Image, UnidentifiedImageError

dirs = [name for name in os.listdir(".") if os.path.isdir(name)]

for d in dirs:
    files = [name for name in os.listdir(f"./{d}")]
    files.sort()
    print(f"Current dir: {d};")
    image_list = []
    for file in files:
        p = os.path.abspath(f"./{d}/{file}")
        try:
            print(f"\tOpen /{d}/{file}")
            img = Image.open(p)
            img = img.convert('RGB')
            image_list.append(img)
        except UnidentifiedImageError:
            if file.lower().find(".heic") != -1:
                print("\tIt is HEIC, I will do it later")
            else:
                print(f"\tWarning: unsupported format: /{d}/{file}, ignoring file")
            
    if len(image_list) != 0:
        print(f"Saving: {d}.pdf")
        image_list[0].save(
            os.path.abspath(f"./{d}.pdf"),
            save_all=True,
            append_images=image_list[1:],
        )
    else:
        print(f"Warning: current directory is empty or contains no images: {d}")
