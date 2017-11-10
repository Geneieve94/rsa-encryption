# rsa-encryption

this file include three artifacts:
the rsa-enc.py rsa-dec.py rsa-keygen.py


How to execute them:


1.python rsa-keygen.py -p public -s private -n (random number you want)
2.encryption:
python rsa-enc.py -i input -o output(cipher) -k public    
3.decryption:
python rsa-dec.py -i cipher(output) -o recover -k private
