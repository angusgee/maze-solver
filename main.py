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
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.canvas.pack()
        
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        
def main():        
    print('starting now....')
    win = Window(420, 420)
    win.wait_for_close()
    
if __name__ == '__main__':
    main()

