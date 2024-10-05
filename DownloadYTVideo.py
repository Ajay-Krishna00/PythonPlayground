import tkinter as tk
from tkinter import font 
import yt_dlp

root=tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("550x400+450+150")
root.configure(bg="#f0f0f0")

customFontH1=font.Font(family="Nunito",size=15)
customFontH2=font.Font(family="Nunito",size=13)

def on_click():
  output_path=None
  if entry2.get()!="":
    output_path=entry2.get()
  inp=entry1.get()
  try:
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s' if output_path else '%(title)s.%(ext)s',
        'format': 'best',  # Downloads the best quality available
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([inp])
    success.config(text="Download Successful")
  except Exception as e:
    print(f"An error occurred: {e}")

success=tk.Label(root,text="",font=customFontH2,fg="green",bg="#f0f0f0")
success.pack(pady=5,padx=50)
label=tk.Label(root,text="Welcome",font=customFontH1)
label.pack(pady=30,padx=50)
url=tk.Label(root,text="Enter the URL of the Video",font=customFontH2)
url.pack(pady=5,padx=50)
entry1=tk.Entry(root,width=30, bg="#ffffff", borderwidth=1,relief="raised",font=customFontH2)
entry1.pack(pady=5)
output_path=tk.Label(root,text="Enter output path (leave empty for current directory)",font=customFontH2)
output_path.pack(pady=5,padx=50)
entry2=tk.Entry(root,width=30, bg="#ffffff", borderwidth=1,relief="raised",font=customFontH2)
entry2.pack(pady=5)
button=tk.Button(root,text="Download",command=on_click,bg="#4CAF50", fg="white", font=customFontH2,
                      activebackground="#45a049", padx=10, pady=5,borderwidth=0)
button.pack(pady=20)
label=tk.Label(root,text="",font=customFontH2)
label.pack(pady=10,padx=10)

root.mainloop()

