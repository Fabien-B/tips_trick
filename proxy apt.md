#Proxy pour apt-get

##sol1 :

export http_proxy="http://<login>:<mot de passe>@<IP>:<port>"

puis :  
sudo -E apt-get ...


##sol2 :

sudo nano /etc/apt/apt.conf.d/proxy

commenter/decommenter la/les lignes à écrire dans ce fichier:

Acquire::http::Proxy "http://<login>:<mot de passe>@<IP>:<port>";  

puis :  
sudo apt-get ...
