from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Mazey") 
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.running = True
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        

def main():        
    win = Window(420, 420)
    
if __name__ == '__main__':
    main()

