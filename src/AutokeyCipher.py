ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('enter message:\n')
    key = input('enter your key:\n')
    mode = input('encrypt or decrypt\n')
    ## if len(key) < len(message):
        ## key = key[0:] + message[:100]
    #print(key)
    if mode == 'encrypt':
       cipher = encryptMessage(message, key)
    elif mode == 'decrypt':
       cipher = decryptMessage(message, key)
    #print(' message:',  (mode.title()))
    print(cipher)


## def encryptMessage (keys, messages):
##     return cipherMessage(keys, messages, 'encrypt')
  def encryptMessage (messages, keys):  
    return cipherMessage(messages, keys, 'encrypt')


## def decryptMessage(keys,messages):
##     return cipherMessage(keys, messages, 'decrypt')
def decryptMessage(messages, keys):
    return cipherMessage(messages, keys, 'decrypt')
def cipherMessage (messages, keys, mode):
    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        ## if text != -1:
        if mode == 'encrypt':
             text += ALPHA.find(key[k_index])
             key += i.upper()  # add current char to keystream

        elif mode == 'decrypt':
             text -= ALPHA.find(key[k_index])
             key += ALPHA[text]  # add current char to keystream
        text %= len(ALPHA)
        ## k_index += -1
        k_index += 1
        ## if k_index == len(key):
        ##     k_index = 0
        ## else:
        cipher.append(ALPHA[text])
    return ''.join(cipher)

if __name__ == "__main__":
    main()
