try:
    import pyperclip
except ImportError:
    pass

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('ceaser cipher, by Sololiqht')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    respone = input('> ').lower()
    if respone.startswith('e'):
        mode = 'encrypt'
        break
    elif respone.startswith('d'):
        mode = 'decrypt'
        break
    print('Please ender the letter e or d.')

while True:
    maxKey = len(symbols) - 1
    print('Please enter the key (0 to {}) to use.', format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

print('Enter the message to {}', format(mode))
message = input('>')
message = message.upper()
translated = ''

for symbol in message:
    if symbol in symbols:
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode =='decrypt':
            num = num - key

        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)

        translated = translated + symbols[num]
    
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
except:
    pass


