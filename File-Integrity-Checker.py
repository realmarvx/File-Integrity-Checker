import hashlib
def hashfiles (filePath):
  hash_Object = hashlib.sha1()
  with open(filePath, 'rb') as file:

    chunk =file.read(4096)
    while chunk:
      hash_Object.update(chunk)
      chunk=file.read(4096)
  return hash_Object.hexdigest()

    # I can write it with walrus operator ":=" and will look like 
    # while chunk := file.read(4096):
    #   hash_Object.update(chunk) 

def compareFiles(file1,file2):
  hash1 = hashfiles(file1)
  hash2 = hashfiles(file2)


  if hash1 is None or hash2 is None:
    print ("Could not compare amd error came up")

  if hash1== hash2:
    print("The files are identical")
  else:
    print("The files are diffrent")
  
    


compareFiles ("File 1.pdf","file1 mirror.pdf")

