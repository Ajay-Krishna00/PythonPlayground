# this is a simple youtube video downloader using tkinter and yt_dlp

import re
import tkinter as tk
from tkinter import font 
from tkinter.ttk import Radiobutton,Style,OptionMenu
import yt_dlp
from yt_dlp.utils import sanitize_filename


root=tk.Tk()
root.title("Video & Audio Downloader")
root.geometry("580x600+450+100") #widthxheight+x_offset+y_offset
root.configure(bg="#f0f0f0")

customFontH1=font.Font(family="Nunito",size=15)
customFontH2=font.Font(family="Nunito",size=13)

style=Style()
style.configure("LargeFont.TRadiobutton",font=("Arial",14))

choice="Download Video"
VFormat="mp4"
AFormat="mp3"

# # Sanitize video title function to remove invalid characters for filenames
# def sanitize_filename(filename):
#     # Replace any character that is not alphanumeric, space, or allowed punctuation
#     filename = re.sub(r'[^\w\s.-]', '', filename)
#     return filename

# Function to download the video
def on_click():
  output_path=None
  if entry2.get()!="":
    output_path=entry2.get()
  inp=entry1.get()
  try:
    
    success.pack_forget()

    # Use yt-dlp to fetch video metadata and sanitize the title
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(inp, download=False)
        title = info_dict.get('title', 'Unknown Title')
        print(f"Downloading {title}...")

    # Sanitize the video title to remove invalid characters
    sanitized_title = sanitize_filename(title)

    if choice=="Download Video":
      ydl_opts = {
          'outtmpl': f'{output_path}/{sanitized_title}.%(ext)s' if output_path else f'{sanitized_title}.%(ext)s',
          'format': 'bestvideo+bestaudio/best',  # Downloads the best quality available
          'postprocessors': [{
                              'key': 'FFmpegVideoConvertor',
                              'preferedformat': VFormat,  
                            }]
      }
    else:
      ydl_opts={
        'outtmpl':f'{output_path}/{sanitized_title}.%(ext)s' if output_path else f'{sanitized_title}.%(ext)s',
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat':AFormat,
      }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([inp])
    success.pack(pady=5,padx=50)
    success.config(text="Download Successful")
  except Exception as e:
    print(f"An error occurred: {e}")
    error_message = f"An error occurred: {e}"
    success.config(text=error_message, bg="red")
    success.pack(pady=5, padx=50)

def on_select():
  global choice, VFormat, AFormat
  choice=selected.get()
  if choice=="Download Audio":
    menuL.pack(pady=5)
    menuL.config(text="Select Audio Format:")
    menuAudio.pack(pady=5)
    menuVideo.pack_forget()
    AFormat=selectedAudioFormat.get()
  else:
    menuL.pack(pady=5)
    menuL.config(text="Select Video Format:")
    menuAudio.pack_forget()
    menuVideo.pack(pady=5)
    VFormat=selectedVideoFormat.get()

# Helper function to open the Help window
def open_help():
    help_window = tk.Toplevel(root)  # Create a new Toplevel window
    help_window.title("Help - Video & Audio Downloader")
    help_window.geometry("600x500+480+130")
    help_window.configure(bg="#f0f0f0")

    # Add content to the Help window
    help_content = """
Welcome to the YouTube Video & Audio Downloader!

This application allows you to download videos and audio from YouTube and other supported platforms using yt-dlp.

Here's how to use the app:

1. **Enter the Video URL**: 
  - Paste the URL of the video or audio you wish to download in the 'Enter the URL of the Video' field.

2. **Choose Download Type**:
  - Select whether you want to download the video or just the audio using the radio buttons.
  - If you choose **Download Video**, the app will download the video in the best available format.
  - If you choose **Download Audio**, the app will extract the audio from the video in your preferred audio format.

3. **Select Format**:
  - For video downloads, choose your preferred video format (e.g., MP4, MKV, etc.).
  - For audio downloads, choose your preferred audio format (e.g., MP3, WAV, etc.).

4. **Optional Output Path**:
  - You can specify the folder where you want the file to be saved. If left empty, the file will be saved in the current working directory.

5. **Start Download**:
  - Click the **Download** button to begin the process.
  - Once the download is complete, a success message will appear on the screen.

Note: The app uses `yt-dlp`, a command-line tool, to download videos and audio. It supports various websites, including YouTube, Vimeo, and others.

For any issues or troubleshooting, please refer to the documentation of yt-dlp at https://github.com/yt-dlp/yt-dlp.

Enjoy your downloads!
"""

    
    help_text = tk.Text(help_window, font=customFontH2, bg="#f0f0f0", wrap="word", height=19, width=55)
    help_text.insert(tk.END, help_content)
    help_text.config(state=tk.DISABLED)  # To make the Text widget read-only
    help_text.pack()


    # Button to close the Help window
    close_button = tk.Button(help_window, text="Close", command=help_window.destroy, bg="#4CAF50", fg="white",borderwidth=0, font=customFontH2)
    close_button.pack(pady=10)

# Create a Help button in the main window
help_button = tk.Button(root, text="Help", command=open_help, bg="white", fg="black",borderwidth=0, font=customFontH2)
help_button.place(relx=1.0, x=-10, y=10, anchor="ne")  # Positioned top right (with slight margin) #relx=1.0: This positions the button relative to the right edge of the window (1.0 means the right edge). -> x=-10: This shifts the button 10 pixels to the left to create a small margin from the edge. -> y=10: This positions the button 10 pixels from the top edge. -> anchor="ne": This anchors the button to its top-right corner. The "ne" stands for north-east.


selected=tk.StringVar(value="Download Video")
selectedAudioFormat=tk.StringVar(value="mp3")
selectedVideoFormat=tk.StringVar(value="mp4")

frm3=tk.Frame(root)
frm3.pack(pady=(40,0))
success=tk.Label(frm3,text="",font=customFontH2,bg="green",fg="#ffffff")
success.pack_forget()

label=tk.Label(root,text="Welcome",font=customFontH1)
label.pack(pady=15,padx=35)

frm=tk.Frame(root,bg="#ffffff")
frm.pack(pady=20)
tk.Label(frm,text="Choose Download type",bg="#ffffff",font=customFontH1).pack(pady=10)
choice1=Radiobutton(frm,text="Download Video",value="Download Video",variable=selected,command=on_select,style="LargeFont.TRadiobutton")
choice1.pack(side="left",padx=10,pady=10)
choice2=Radiobutton(frm,text="Download Audio",value="Download Audio",variable=selected,command=on_select,style="LargeFont.TRadiobutton")
choice2.pack(side="left",padx=10,pady=10)

frm2=tk.Frame(root)
frm2.pack()
menuL=tk.Label(frm2,text="Select Video Format:",font=customFontH2)
menuL.pack(pady=5)
audio_formats=["mp3","mp3","wav","ogg","acc","flac"]
menuAudio=OptionMenu(frm2,selectedAudioFormat,*audio_formats,style="LargeFont.TRadiobutton")
menuAudio.pack_forget()
video_formats=["mp4","mp4","mkv","webm","flv","avi"]
menuVideo=OptionMenu(frm2,selectedVideoFormat,*video_formats,style="LargeFont.TRadiobutton")
menuVideo.pack(pady=5)

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

root.mainloop()

