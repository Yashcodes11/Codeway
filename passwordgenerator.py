import random
import string
import PySimpleGUI as psg

# upper=random.sample(string.ascii_uppercase,2)
# lower=random.sample(string.ascii_lowercase,2)
# digits=random.sample(string.digits,2)
# symbols=random.sample(string.punctuation,2)

# total=upper + lower + digits + symbols
# total=random.sample(total,len(total))
# total=''.join(total)
# print(total)


psg.theme('darkblue6')
psg.set_options(font='verdana 17')


layout=[
    [psg.Text('Uppercase :'),psg.Push(),psg.Input(size=15 , key='-UP-')],
    [psg.Text('Lowercase :'),psg.Push(),psg.Input(size=15, key='-LOW-')],
    [psg.Text('Digits :'),psg.Push(),psg.Input(size=15 , key='-DIG-')],
    [psg.Text('Special characters :'),psg.Push(),psg.Input(size=15 , key='-spchar-')],
    [psg.Button('Generate Password '),psg.Button('Cancel')],
    [psg.Text('Password :'),psg.Push(),psg.Multiline(size=15,no_scrollbar=True,
     disabled=True,key='-PASS-')]
                                                     
]

window=psg.Window('Password Generator',layout)


while True:
    event , values = window.read()
    if event== 'Cancel' or event==psg.WIN_CLOSED:
        break

    if event=='Generate Password':
        try:
            u_upper=int(values['-UP-'])
            upper=random.sample(string.ascii_uppercase,u_upper)
            u_lower=int(values['-LOW-'])
            lower=random.sample(string.ascii_lowercase,u_lower)
            u_digits=int(values['-DIG-'])
            digits=random.sample(string.digits,u_digits)
            u_symbols=int(values['-spchar-'])
            symbols=random.sample(string.punctuation,u_symbols)

            total=upper + lower + digits  + symbols
            total=random.sample(total,len(total))
            total=''.join(total)
            window['-PASS-'].update(total)

        except ValueError: 
            window['-PASS-'].update("no valid number")   

        



window.close()