

# Code={
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
#   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
#   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
#   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
#   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
#   'Z': '--..', 
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
#   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
#   '0': '-----', 
#   '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
#   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
#   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
#   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '|'
# }

# Inversed_Code={value:key for key,value in Code.items()}

# if __name__=="__main__":
#   inp=int(input("Enter 1 for Morse Code Generator and 2 for Morse Code Decoder: "))
#   s=input("Enter the string: ")
#   if inp == 1:
#         s = s.upper()
#         morse_code = ""
#         for i in s:
#           morse_code += Code.get(i,"") + " "
#         print("Morse Code: ", morse_code)
    
#   elif inp == 2:
#       text = ""
#       for i in s.split(" "):
#         text += Inversed_Code.get(i,"")
#       print("Text: ", text)
  
#   else:
#         print("Invalid input")




import sys
import winsound  # For sound playback (Windows-specific)
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QRadioButton, QGroupBox
from PyQt5.QtCore import Qt

Code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '|'
}
Inversed_Code={value:key for key,value in Code.items()}

def playMorseSound(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(1000, 200)  # Dot (short beep)
        elif symbol == '-':
            winsound.Beep(1000, 500)  # Dash (long beep)
        else:
            # Space or invalid characters
            pass

class MorseCodeApp(QWidget):
    isPlayable = False
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Morse Code Generator and Decoder")
        self.setGeometry(300, 300, 700, 500) # x, y, width, height
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        # Input field
        self.input_label = QLabel("Input:", self)
        self.input_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.input_label)
        self.text_input = QTextEdit(self)
        self.text_input.setPlaceholderText("Enter text here")
        self.text_input.setGeometry(100, 50, 500, 100)
        self.text_input.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.text_input)

        # Radio buttons for Encoder/Decoder
        self.encoderBtn = QRadioButton("Encoder", self)
        self.decoderBtn = QRadioButton("Decoder", self)
        self.encoderBtn.setStyleSheet("font-size: 18px;")
        self.decoderBtn.setStyleSheet("font-size: 18px;")
        self.encoderBtn.setChecked(True)

        # Grouping the radio buttons
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.encoderBtn)
        radio_layout.addWidget(self.decoderBtn)

        radio_group = QGroupBox("Choose Mode", self)
        radio_group.setLayout(radio_layout)
        layout.addWidget(radio_group)

        # Output field
        self.output_label = QLabel("Output:", self)
        self.output_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.output_label)
        self.output = QTextEdit(self)
        self.output.setPlaceholderText("Output will appear here")
        self.output.setReadOnly(True)
        self.output.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.output)

        # Buttons
        self.convertBtn = QPushButton("Convert", self)
        self.convertBtn.clicked.connect(self.convert)
        self.convertBtn.setStyleSheet(""" font-size: 18px; 
                                        color: white; 
                                        background-color:#007bff;
                                        border: none;
                                        padding: 10px 20px;
                                        border-radius: 10px;
                                        """)
        self.convertBtn.setEnabled(True)
        layout.addWidget(self.convertBtn)

        self.playBtn = QPushButton("Play Sound", self)
        self.playBtn.clicked.connect(self.playSound)
        self.playBtn.setStyleSheet("font-size: 18px; color: white; background-color:#007bff; padding: 10px 20px; border-radius: 10px;")
        layout.addWidget(self.playBtn)

        self.setLayout(layout)

    def convert(self):
        input_text = self.text_input.toPlainText().upper()
        
        if self.encoderBtn.isChecked():
            morse_code = ""
            for i in input_text:
                morse_code += Code.get(i,"") + " "
            self.output.setText(morse_code)
            self.isPlayable = True
        elif self.decoderBtn.isChecked():
            morse_code = input_text.split(" ")
            text = ""
            for i in input_text.split(" "):
              text += Inversed_Code.get(i,"")
            self.output.setText(text)
            self.isPlayable = False

    def playSound(self):
        morse_code = self.output.toPlainText()
        if self.isPlayable:
            playMorseSound(morse_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MorseCodeApp()
    ex.show()
    sys.exit(app.exec_())
