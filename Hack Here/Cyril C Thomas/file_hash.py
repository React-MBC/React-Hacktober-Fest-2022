import hashlib

def hash_file(filename):
   h = hashlib.sha1()

   with open(filename,'rb') as file:

       chunk = 0
       while chunk != b'':

           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()

hash_ = hash_file("a.py")
print(hash_)
