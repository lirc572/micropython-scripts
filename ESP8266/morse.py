#letters separated by a space of duration equal to three dots
#words separated by a space equal to seven dots
class Morse:
    def __init__(self, pin = None, timeunit = 60):
        self.pin = pin
        self.pin.on()
        self.code = []
        self.text = ""
        self.timeunit = timeunit
    def fromStr(self, string):
        self.text = string
        self.code = []
        for char in string:
            self.code.append(self._encodeChar(char))
    def play(self):
        import time
        self.pin.on()
        for char in self.code:
            if char[0] == -1:
                time.sleep_ms(self.timeunit * 7)
                continue
            print(char)
            for i in char:
                self.pin.off()
                time.sleep_ms(self.timeunit)
                if i == 1:
                    time.sleep_ms(self.timeunit * 2)
                self.pin.on()
                time.sleep_ms(self.timeunit)
            time.sleep_ms(self.timeunit * 3)
    def _encodeChar(self, char):
        code_list = ((0,1),         #A
                     (1,0,0,0),     #B
                     (1,0,1,0),     
                     (1,0,0),       #D
                     (0,),          #E
                     (0,0,1,0),     #F
                     (1,1,0),       #G
                     (0,0,0,0),     #H
                     (0,0),         #I
                     (0,1,1,1),     #J
                     (1,0,1),       #K
                     (0,1,0,0),     #L
                     (1,1),         #M
                     (1,0),         #N
                     (1,1,1),       #O
                     (0,1,1,0),     #P
                     (1,1,0,1),     #Q
                     (0,1,0),       #R
                     (0,0,0),       #S
                     (1,),          #T
                     (0,0,1),       #U
                     (0,0,0,1),     #V
                     (0,1,1),       #W
                     (1,0,0,1),     #X
                     (1,0,1,1),     #Y
                     (1,1,0,0),     #Z
                     (1,1,1,1,1),   #0
                     (0,1,1,1,1),   #1
                     (0,0,1,1,1),   #2
                     (0,0,0,1,1),   #3
                     (0,0,0,0,1),   #4
                     (0,0,0,0,0),   #5
                     (1,0,0,0,0),   #6
                     (1,1,0,0,0),   #7
                     (1,1,1,0,0),   #8
                     (1,1,1,1,0))   #9
        if char >= 'A' and char <= 'Z':
            return code_list[ord(char)-65]
        elif char >= 'a' and char <= 'z':
            return code_list[ord(char)-97]
        elif char >= '0' and char <= '9':
            return code_list[ord(char)-22]
        elif char == '.':
            return (0,1,0,1,0,1)
        elif char == ',':
            return (1,1,0,0,1,1)
        elif char == '?':
            return (0,0,1,1,0,0)
        elif char == '/':
            return (1,0,0,1,0)
        elif char == '@':
            return (0,1,1,0,1,0)
        else:
            return (-1,)