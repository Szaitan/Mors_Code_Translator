import tkinter
from tkinter import messagebox
import os
import sys
from morse_dic import morse_alphabet


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MorseCode(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Morse Code Translator")
        self.main_window_size = (485, 455)
        self.iconbitmap(bitmap=resource_path("Images/favicon.ico"))
        self.welcome_font = ("Calibre lights", 14, 'bold')
        self.pick_font = ("Calibre body", 12, 'bold')
        self.font_in_text = ("Calibre body", 10, 'normal')
        self.bg_color = "#b9f0c8"
        self.config(background=self.bg_color)

        self.first_entry = None
        self.second_entry = None
        self.first_scroll = None
        self.separation_col = None
        self.second_scroll = None
        self.left_normal_lang = None
        self.welcome_label = None
        self.from_morse_button = None
        self.to_morse_button = None
        self.letter = None
        self.summary()

    def main_window_position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_width = screen_width / 2 - self.main_window_size[0] / 2
        position_height = screen_height / 2 - self.main_window_size[1] / 2
        return int(position_width), int(position_height)

    def creating_geometry(self, width, height):
        self.geometry(f"{self.main_window_size[0]}x{self.main_window_size[1]}+{width}+{height}")

    def create_widgets(self):
        # Welcome Label
        self.welcome_label = tkinter.Label(text="Welcome to Morse Code Translator!", font=self.welcome_font,
                                           background=self.bg_color)
        self.welcome_label.grid(row=0, column=0, columnspan=2)

        # Write Lang Write Morse
        self.left_normal_lang = tkinter.Label(text="Input:", font=self.pick_font, background=self.bg_color)
        self.left_normal_lang.grid(row=1, column=0, columnspan=2)

        self.welcome_label = tkinter.Label(text="Output:", font=self.pick_font, background=self.bg_color)
        self.welcome_label.grid(row=4, column=0, columnspan=2)

        # First Text and Scroll bar
        self.first_scroll = tkinter.Scrollbar()
        self.first_scroll.grid(row=2, column=2, sticky="NS")

        self.first_entry = tkinter.Text(width=66, height=10,
                                        yscrollcommand=self.first_scroll.set, font=self.font_in_text)
        self.first_entry.grid(row=2, column=0, columnspan=2)

        self.first_scroll.config(command=self.first_entry.yview)

        # Second Text and Scroll bar
        self.second_scroll = tkinter.Scrollbar()
        self.second_scroll.grid(row=5, column=2, sticky="NS")

        self.second_entry = tkinter.Text(width=66, height=10,
                                         yscrollcommand=self.second_scroll.set, font=self.font_in_text)
        self.second_entry.grid(row=5, column=0, columnspan=2)

        self.second_scroll.config(command=self.second_entry.yview)

        # Buttons
        self.to_morse_button = tkinter.Button(text="Text to Morse", command=self.text_to_morse,
                                              activebackground=self.bg_color)
        self.to_morse_button.grid(row=3, column=0, pady=5)

        self.from_morse_button = tkinter.Button(text="Morse to Text", command=self.morse_to_text,
                                                activebackground=self.bg_color)
        self.from_morse_button.grid(row=3, column=1, pady=5)

    def summary(self):
        position_of_window = self.main_window_position()
        self.creating_geometry(position_of_window[0], position_of_window[1])
        self.create_widgets()

    def text_to_morse(self):
        text_to_translate = str(self.first_entry.get(1.0, "end-1c")).upper()
        text_to_display = ""
        for word in text_to_translate:
            try:
                self.letter = morse_alphabet[0][word]
            except KeyError:
                messagebox.showerror(title="Wrong data", message=f"'{word}' is causing the problem.\n"
                                                                 f"Please provide latin alphabet data.")
                break
            else:
                text_to_display += self.letter + " "
        self.second_entry.delete("1.0", tkinter.END)
        self.second_entry.insert("1.0", text_to_display)

    def morse_to_text(self):
        text_to_translate = str(self.first_entry.get(1.0, "end-1c")).lower()
        text_to_translate = text_to_translate.split(" ")
        text_to_display = ""
        for word in text_to_translate:
            if "\n" in word:
                letter = morse_alphabet[1][word.replace("\n", "")]
                text_to_display += "#" + letter
            else:
                try:
                    self.letter = morse_alphabet[1][word]
                except KeyError:
                    messagebox.showerror(title="Wrong data", message=f"'{word}' is causing the problem.\n"
                                                                     f"Please provide morse code data.")
                    break
                else:
                    text_to_display += self.letter

            # try:
            #     letter = morse_alphabet[1][word]
            # except KeyError:
            #     test = word.replace("\n", "")
            #     letter = morse_alphabet[1][test]
            #     text_to_display += "#" + letter
            # else:
            #     text_to_display += letter
        text_to_display = text_to_display.upper()

        self.second_entry.delete("1.0", tkinter.END)
        self.second_entry.insert("1.0", text_to_display)


morse_code = MorseCode()
morse_code.mainloop()
