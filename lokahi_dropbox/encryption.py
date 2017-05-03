from Crypto.Cipher import XOR
from Crypto.Hash import MD5


def get_file_size(file_handler):
   file_handler.seek(0,2)
   return file_handler.tell()


def get_hashed_key(key):
   h = MD5.new(data=key)
   return h.digest()


def encrypt_file(filename, key):
   key = get_hashed_key(key.encode('utf-8'))

   try:
       file_handler = open(filename, 'rb')

       out_filename = filename + '.enc'
       out_file_handler = open(out_filename, 'wb')

       symmetric_key = XOR.new(key)

       while True:
           chunk = file_handler.read(1)
           if chunk:
               cipher_text = symmetric_key.encrypt(chunk)
               out_file_handler.write(cipher_text)
           else:
               break

       file_handler.close()
       out_file_handler.close()

   except FileNotFoundError:
       print('A file with this name could not be found !')
       exit(1)


def decrypt_file(filename, key):
   key = get_hashed_key(key.encode('utf-8'))

   if not filename[len(filename)-4:] == '.enc':
       print('Incorrect file extension : file must end in .enc')
       exit(1)

   try:
       file_handler = open(filename, 'rb')

       out_filename = 'DEC_' + filename[:-4]
       out_file_handler = open(out_filename, 'wb')

       symmetric_key = XOR.new(key)

       while True:
           chunk = file_handler.read(1)

           if chunk:
               plain_text = symmetric_key.decrypt(chunk)
               out_file_handler.write(plain_text)
           else:
               break

       file_handler.close()
       out_file_handler.close()

   except FileNotFoundError:
       print('A file with this name could not be found !')
       exit(1)