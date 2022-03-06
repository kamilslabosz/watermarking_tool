import os
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

BG = "White"


def file_watermark():
    directory = file_loc_entry.get()
    watermark = watermark_text_entry.get()
    with Image.open(directory) as img:
        watermarking = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("font/UbuntuMono-B.ttf", 40)
        watermarking.text((10, 10), f"{watermark}", font=fnt, fill=(255, 255, 255, 128))

        img.save("done/watermarked.png", "PNG")


def directory_watermark():
    watermark = watermark_text_entry.get()
    directory = 'to_do'
    img_nr = 1
    for element in os.listdir(directory):
        path = os.path.join(directory, element)
        with Image.open(path) as img:
            watermarking = ImageDraw.Draw(img)
            fnt = ImageFont.truetype("font/UbuntuMono-B.ttf", 40)
            watermarking.text((10, 10), f"{watermark}", font=fnt, fill=(255, 255, 255, 128))

            img.save(f"done/watermarked_{img_nr}.png", "PNG")
        img_nr += 1


window = Tk()
window.title("Watermarking App")
window.config(padx=20, pady=20)

watermark_text_label = Label(text="Watermark text: ")
watermark_text_label.grid(column=0, row=0)

watermark_text_entry = Entry(width=50)
watermark_text_entry.grid(column=1, row=0)

file_location = Label(text="Paste file directory: ")
file_location.grid(column=0, row=1, pady=20)

file_loc_entry = Entry(width=50)
file_loc_entry.grid(column=1, row=1)
file_loc_entry.focus()

button_file = Button(text="Watermark it!", command=file_watermark)
button_file.grid(column=0, row=2, columnspan=2)

watermark_in_dir = Label(text='Or watermark every file in "to_do" directory')
watermark_in_dir.grid(column=0, row=4, columnspan=2, pady=20)

button_directory = Button(text="Go for it!", command=directory_watermark)
button_directory.grid(column=0, row=5, columnspan=2)

window.mainloop()
