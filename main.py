from tkinter import Tk, ttk, END
from youtube_download import download_split
from instagram import download_split_ig

def handle_ig_btn():
    user_input = input_element.get()
    success = download_split_ig(user_input)
    if success:
        result_lbl["text"] = f"Instagram videos for '{user_input}' downloaded successfully"
        input_element.delete(0, END)
    else:
        result_lbl["text"] = f"Failed to download Instagram videos for '{user_input}'"


def handle_yt_btn():
    user_input = input_element.get()
    success = download_split(user_input)
    if success:
        result_lbl["text"] = f"Youtube videos for '{user_input}' downloaded successfully"
        input_element.delete(0, END)
    else:
        result_lbl["text"] = f"Failed to download Youtube videos for '{user_input}'"


window = Tk()
window.title("Social video downloader")
frm = ttk.Frame(window, padding=10)
frm.grid()
ttk.Label(frm, text="Enter keyword:").grid(row=0, column=0)
input_element = ttk.Entry(frm)
input_element.grid(row=1, column=0)
result_lbl = ttk.Label(frm)
result_lbl.grid(row=2, column=0)
yt_btn = ttk.Button(frm, text="Youtube download", command=handle_yt_btn)
yt_btn.grid(row=3, column=0)
tiktok_btn = ttk.Button(frm, text="Instagram download", command=handle_ig_btn)
tiktok_btn.grid(row=4, column=0)
exit_btn = ttk.Button(frm, text="Quit", command=window.destroy)
exit_btn.grid(row=5, column=0)


if __name__ == "__main__":
    window.mainloop()
