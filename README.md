# KOR app for FIS lab
###  by Andrei Surugiu and Bogdan Caliman
**requires python 3.8 and pip3**  
Can be installed with ``sudo apt install python3-pip``

Build using ``python3 setup.py develop ``  
Execute using ``python3 main.py`` in your directory  
Or create a symlink `` ln -s path_to_main_py your_location_of_choice``  

The default admin credentials are ``admin:admin1!``,it is strongly suggested you change your admin password.  

Data is hashed using sha512 + salt and your files are encrypted using AES encryption.  

You can create groups and add other users which you can share an encrypted directory with.  

Guest accounts are deleted 8 hours after creation.  

  
![1]
![2]

[1]:./images/login_page.png
[2]:./images/register_page.png
