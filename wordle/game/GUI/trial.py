from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import win32clipboard

def emoji_img(size, text):
    font = ImageFont.truetype("seguiemj.ttf", size=int(round(size*72/96, 0))) 
    # pixels = points * 96 / 72 : 96 is windowsDPI
    im = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.text((size/2, size/2), text, embedded_color=True, font=font, anchor="mm")
    return ImageTk.PhotoImage(im)

def copy():
    emoji_data = button['text']
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, emoji_data)
    win32clipboard.CloseClipboard()
    print("Copied!", emoji_data)

root = tk.Tk()
text="😄"
emoji = emoji_img(80, text)
button = tk.Button(root, image=emoji, text=text, command=copy)
button.pack()
root.mainloop()