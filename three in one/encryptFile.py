import pyAesCrypt

password = input('Введите пароль для файла: ')


todo = input('Вы хотете расшифровать или зашифровать? Введите decry или encry').lower()

if todo == 'decry':
    pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
elif todo == 'encry':
    pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
else:
    print('Введите правильно, что нужно сделать')
