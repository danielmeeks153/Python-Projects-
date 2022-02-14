import webbrowser
from tkinter import *
  

win = Tk()
b1 = Button(win, text="Generate")
b1.grid(row=0, column=0)


def makeHTML(self):
    f = open("webpageGenerator.html", "w")
    html = ("""
    <html>
        <body>
            <h1>"""
            + self.txt_browse1.get() +
            """</h1>
        </body>
    </html>
    """)

    f.write(html)
    f.close()
    url = "webpageGenerator.html"
    wb.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

def Generate(self):
    
    v = StringVar()
    e = Entry(win, textvariable = v)
    e.grid()

    v.get()

b1.configure(command=makeHTML)
