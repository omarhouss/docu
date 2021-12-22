doc = {
    "systeme d'expolitation" : "Un système d'exploitation est le support qui permet de faire la liaison entre l'utilisateur ,une application et l'hardware de l'ordinateur",
    "kernel" : "c'est un espace memoire contenant les donnees principales du systeme d'exploitation , houwa li kay3ti l stysteme l'interface de programmation bch yste3ml lmateriel ",
    "virtualisation" : "houwa le fait de creer une ou plusieurs version logiciel sur une seul machine w les resources dyl dak machine kykounou divises mabin douk les os w les os kaykounou separe ela be3dyathoum b wahed lhaja katsema l'hyperviseur",
    "l'hyepirviseur" : "houwa softwer li kaykhlina n creyiw wVMs kaye3ti lkoule machine ses besoins de ressours , s'assure ano mtkounch binathpoum interaction wkynin jouj dyl anwa3e bare metal w host meetal , bare metale houwa li katkoun endou relation direct me#a hardwere w kyji fou9e mno os invite, wkyne host metale li kykoutoune fou9e mn os hote w 3ade kyji fou9ou os invite ",
    "Architecture" :"hya la structure generale inhernete lwahed systeme informatique , l'organisation dyl l'element de systeme soit logicel ou materielle ",
    "metadata" : "Les métadonnées sont des « données qui fournissent des informations sur d'autres données »,[1] mais pas sur le contenu des données, comme le texte d'un message ou l'image elle-même",
    "package manager" : "houwa wahed collection dyl programms li katautomatisi l process dyl instalation , configuration , suprrision dyl progams for a computer",
    "debian vs Centos" : "kayn fer9e f architecture , debian katsupoti MIPSel, MIPS64el and s390x ",
    "sudo" : "super user do hya wahed la commande knsta3mlouha f les systeme d'exploitation de type unix kte3tina la possibilete bch nlosiw une commande en tant que administrateur de systeme ",
    "lvm" : "houwa logical volume manager houwa wahed logiciel wela methode li kate3ina la possibilte bch ngestioniw des espaces de stockage d'un odinateur f les systeme d'esxploitation de type unix ",
    "root" : "houwa le compte le plus puissant fwahed la machine sous debian le compte root ky(der ydir koulchi fdik la mchine houwa superutilisateur whouwa superviseur",
    "su" : "hya wahed lcommade kanste3mlouha bch ntchangaw l onther user wila derna hi su bouhdha kantconnektaw en tant que user",
    "apt" : "advanced package tool hya wahed la commande kanste3mlouha pour instaaler ,  update , remove packege on debian ",
    "aptitude" : "hya wahed front end advanced package tool li katzide user interface  w katsmeh l user bch y9lb ela package bch y instale w ysuprimihe",
    "apt vs aptitude" : "apt hya line commande bla GUI w aptitude katsuporte GU w aptitude is heigh level package manager l3eks dyl apt li hya low-level package manger wt9der tsete3ml mn taraf other heigh levl package manager ",
    "SELinux" : "Security-Enhanced Linux hya wahed l'architecture dyl securite pour les systeme linux li ktkheli les adminastrateurs de bien controler les acces ldak systeme kykhdem bwahed l politique de securite  ye3ni wahed l'ensemble des regles de securite li kaydifinw l systme chno y9der luser yacceder lihe mnin wahed l'application katsift whaed la requete bch taaceder lwahed objet hna fin kykhdem SElinux hit kayconsulter wahed cahe AVC fin kykounou mstokyin les autorisation d'acces pour les differnts objets ",
    "AppArmor" : "est un logiciel libre de sécurité pour Linux. AppArmor permet à l'administrateur système d'associer à chaque programme un profil de sécurité qui restreint les capacités de celui-ci.",
    "SSH" : "c'est un protocole de communication securise li kaye3ti l'utilisateur wahed le moyen securise pour aceder lwahed ordinateur via un resau no securise",
    "Cryptographie symétrique" : "hya wahed la facon de cryptage li 9dima elle permet a la fois de chifferer et de dechiffrer des messages a l'aid d'un meme mot cle",
    "chiffremet" : "houwa wahed technique li katkhlina nsecurisiw la communication mabine jouj hwayj bch nmene3o wahed la personne anaha te3erf douk les donnes li kaynin fdik discussion",
    "authentification" : "hya wahed l'operation li katkhli systeme ye3erf bli l'expiditeur houwa la bonne personne",
    "apt-get update" : "ktrecupiri les information dyl dak package mn repository",
    "usermode" : "hywa wahed la commande kanste3mlouha pour changer les propriete d'un utilisateur hit min kancreyiw wahed luser kn9dero nchagiw fhl passwords wela some attributes  ",
    "sudo grouo" : "houwa group dyl super user li endhoum acces l root account",
    "firewall" : "houwa wahed softwer li kansta3mlouh bch nfeltriw les paquets li kayweslouna mn networks had filtrage kykoun selon wahed rules o policies wkykawn mn jouj hwayj packet filtering w application level gateway",
    "packet" : "houwa wahed l'ensemble des informations qui circule sur internet dak lpacket kaykounou fihe les informations lmouhimin bch twesl l point de destination ",
    "check ufw" : "sudo ufw status numbered",
    "check ssh" : " sudo systemctl status ssh",
    "systemsctl" : "wahed commande li katllowi to start wela stop wela restart w cheki services sttus",
    "check debin" : "cat /etc/debian_version",
    "check user in group" : "getent groups sudo/user42",
    "cret new user" : "sudo adduser user_name",
    "check rules pssword" : "chage - l user",
    "set rules to password" : "sudo nano /etc/pam.d/common-password , sudo nano /etc/login.defs",
    "creat group" : "sudo group evaluating",
    "check host name" : "hostname/hostnamectl",
    "change hostname" : "sudo hostctl set-hostname test       sudo nano /etc/hosts",
    "suo install " : "",
    "check ufw" : "",
    "check rules" : "sudo ufw status numbered",
    "delete rules" : "sudo ufw delete num",
    "cron" : "houwa wahed le programme li kaykhli l'ytlisteur bcah y executi wahed script automatiquemet fla dte li bgha houw",




}

while 1:
    x = str(input("what do you want know "))
    y = doc.get(x)
    print(y)
    print("-----------------------------------------------------")
    