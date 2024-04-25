from tkinter import *
import requests
from tkhtmlview import HTMLLabel


class HTMLFetcher:
    @staticmethod
    def fetch_html_content(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch content from {url}"


class WindowUx:
    def __init__(self):
        title = "The BrianMungai Browser"
        self.title = title
        self.width = None
        self.height =  None
        self.root = Tk()
        self.aspect_ratio = 16/9 
    
    def set_size(self):
        #update window before getting screen size
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        screen_percentage = 0.8

        self.width = int(screen_width * screen_percentage)
        self.height = int(screen_height * screen_percentage)

    def setup_window(self):
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")

    def run(self):
        self.set_size()
        self.setup_window()
        self.root.mainloop()

class Features:
    def __init__(self, root):
        #win is the Tk() object from WindowUx
        self.root = root

    def address_bar(self):
        #top howrizontal frame for the address bar
        top_frame = Frame(self.root)
        top_frame.pack(fill="x")

        #Enter URL text
        label = Label(top_frame, text="Enter URL:")
        label.pack(side="left")
        label.update_idletasks()
        label_width = label.winfo_width()

        #The text entry field
        screen_width = self.root.winfo_screenwidth()
        entry_width = int(screen_width / 8)
        entry = Entry(top_frame, width=entry_width)
        entry.pack(side="left")

        #Go when enter is clicked
        entry.bind("<Return>", lambda event: self.button_clicked(event, entry))
        
    def button_clicked(self, event, entry):
        if not event or entry.get():
            url = entry.get()
            html_content = HTMLFetcher.fetch_html_content(url)
            self.display_html_content(html_content)
    
    def display_html_content(self, html_content):
        result_frame = Frame(self.root)
        result_frame.pack(fill=BOTH, expand=True)

        # Create a Text widget
        text = Text(result_frame, wrap=WORD)
        text.pack(side=LEFT, fill=BOTH, expand=True)

        # Add Scrollbars
        scrollbar_y = Scrollbar(result_frame, orient=VERTICAL, command=text.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(result_frame, orient=HORIZONTAL, command=text.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)

        # Configure Text widget to use Scrollbars
        text.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Insert HTML content into the Text widget
        text.insert(END, html_content)


            
    def all_features(self):
        self.address_bar()
        

def main():
    window = WindowUx()
    features = Features(window.root)
    features.all_features()
    window.run()
main()