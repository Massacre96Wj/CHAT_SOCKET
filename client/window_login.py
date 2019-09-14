from tkinter import Tk, Label, Entry, Button, Frame
from tkinter import LEFT, END
class WindowLogin(Tk):
    def __init__(self):
        super(WindowLogin, self).__init__()
        self.window_init()
        self.add_widgets()

    def window_init(self):
        self.title("登录窗口")
        self.resizable(False, False)
        window_width = 255
        window_height = 95

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        pos_x = (screen_width - window_width) / 2
        pos_y = (screen_height - window_height) / 2
        self.geometry('%dx%d+%d+%d'%(window_width, window_height, pos_x, pos_y))

    def add_widgets(self):
        username_lable = Label(self)
        username_lable['text'] = '用户名'
        username_lable.grid(row = 0, column = 0, padx = 10 , pady = 5)

        username_entry = Entry(self, name='username_entry')
        username_entry['width'] = 25
        username_entry.grid(row=0, column=1)

        password_lable = Label(self)
        password_lable['text'] = '密  码'
        password_lable.grid(row = 1, column = 0)

        password_entry = Entry(self, name = 'password_entry')
        password_entry['show'] = '*'
        password_entry['width'] = 25
        password_entry.grid(row = 1, column = 1)

        button_frame = Frame(self, name = 'button_frame')

        reset_button = Button(button_frame, name='reset_button')
        reset_button['text'] = '重置'
        reset_button.pack(side = LEFT, padx = 20)

        login_button = Button(button_frame, name='login_button')
        login_button['text'] = '登录'
        login_button.pack(side = LEFT)

        button_frame.grid(row = 2, columnspan = 2, pady = 5)

    def get_username(self):
        return self.children['username_entry'].get()

    def clear_username(self):
        self.children['username_entry'].delete(0,END)

    def get_password(self):
        return self.children['password_entry'].get()

    def clear_password(self):
        self.children['password_entry'].delete(0, END)

    def on_login_button_click(self, command):
        self.children['button_frame'].children['login_button']['command'] = command

    def on_reset_button_click(self, command):
        self.children['button_frame'].children['reset_button']['command'] = command

    def on_window_closed(self,command):
        self.protocol('WM_DELETE_WINDOW', command)
"""
if __name__ == '__main__':
    window_login = WindowLogin()
    window_login.mainloop()
"""
