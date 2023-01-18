import re 
   
inp_str = "Hello! Folks, we are here to learn, grow and glow!!"
   
print("Original string:\n" + inp_str) 
  
opt = re.sub(r'[^\w\s]','', inp_str) 
   
print("String after deletion of punctuation marks:\n" + opt)  