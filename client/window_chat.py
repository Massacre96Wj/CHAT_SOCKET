from tkinter.scrolledtext import ScrolledText
from tkinter import Toplevel, Text, Button
from tkinter import END, UNITS
from time import  strftime, localtime, time
class WindowChat(Toplevel):
    def __init__(self):
        super(WindowChat, self).__init__()
        self.geometry('%dx%d'%(795, 505))
        self.resizable(False, False)
        self.add_widgets()

    def add_widgets(self):
        chat_textarea = ScrolledText(self)
        chat_textarea['width'] = 110
        chat_textarea['height'] = 30
        chat_textarea.grid(row=0, column=0, columnspan=2)

        chat_textarea.tag_config('green', foreground='#008B00')
        chat_textarea.tag_config('system', foreground='red')
        self.children['chat_textarea'] = chat_textarea

        chat_inputarea = Text(self, name='chat_inputarea')
        chat_inputarea['width'] = 100
        chat_inputarea['height'] = 7
        chat_inputarea.grid(row=1, column=0, pady=10)

        send_button = Button(self, name='send_button')
        send_button['text'] = '发送'
        send_button['width'] = 5
        send_button['height'] = 2
        send_button.grid(row=1, column=1)

    def set_title(self,title):
        self.title('欢迎 %s 进入聊天室' %title)

    def clear_input(self):
        self.children['chat_inputarea'].delete(0.0, END)

    def get_input(self):
        return self.children['chat_inputarea'].get(0.0,END)

    def append_message(self, sender, messages):
        send_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
        sender_info = '%s:  %s' %(sender, send_time)
        self.children['chat_textarea'].insert(END, sender_info, 'green')
        self.children['chat_textarea'].insert(END, ' '+messages+ '\n')

        self.children['chat_text_area'].yview_scroll(3, UNITS)

    def on_window_closed(self,command):
        self.protocol('WM_DELETE_WINDOW', command)

    def on_send_button_click(self, command):
        self.children['send_button']['command'] = command

if __name__ == '__main__':
    window_chat = WindowChat()
    window_chat.set_title("wangjie")
    window_chat.mainloop()
