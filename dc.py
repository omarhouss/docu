doc = {
    "systeme d'expolitation" : "Un système d'exploitation est le support qui permet de faire la liaison entre l'utilisateur ,une application et l'hardware de l'ordinateur",
    "kernel" : "c'est un espace memoire contenant les donnees principales du systeme d'exploitation , houwa li kay3ti l stysteme l'interface de programmation bch yste3ml lmateriel ",
    "virtualisation" : "houwa le fait de creer une ou plusieurs version logiciel sur une seul machine w les resources dyl dak machine kykounou divises mabin douk les os w les os kaykounou separe ela be3dyathoum b wahed lhaja katsema l'hyperviseur",
    "l'hyepirviseur" : "houwa softwer li kaykhlina n creyiw wVMs kaye3ti lkoule machine ses besoins de ressours , s'assure ano mtkounch binathpoum interaction wkynin jouj dyl anwa3e bare metal w host meetal , bare metale houwa li katkoun endou relation direct me#a hardwere w kyji fou9e mno os invite, wkyne host metale li kykoutoune fou9e mn os hote w 3ade kyji fou9ou os invite ",
    "Architecture" :"hya la structure generale inhernete lwahed systeme informatique , l'organisation dyl l'element de systeme soit logicel ou materielle ",
    "metadata" : "Les métadonnées sont des « données qui fournissent des informations sur d'autres données »,[1] mais pas sur le contenu des données, comme le texte d'un message ou l'image elle-même",
    "package manager" : "houwa wahed collection dyl programms li katautomatisi l process dyl instalation , configuration , suprrision dyl progams for a computer",
    "debian vs Centos" : "kayn fer9e f architecture , debian katsupoti MIPSel, MIPS64el and s390x ",
    "sudo" : "hya wahed la commande knsta3mlouha f les systeme d'exploitation de type unix kte3tina la possibilete bch nlosiw une commande en tant que administrateur de systeme ",
    "lvm" : "houwa logical volume manager houwa wahed logiciel wela methode li kate3ina la possibilte bch ngestioniw des espaces de stockage d'un odinateur f les systeme d'esxploitation de type unix ",
    "root" : "houwa le compte le plus puissant fwahed la machine sous debian le compte root ky(der ydir koulchi fdik la mchine houwa superutilisateur whouwa superviseur",
    "su" : "hya wahed lcommade kanste3mlouha bch ntchangaw l onther user wila derna hi su bouhdha kantconnektaw en tant que user",
    "apt" : "advanced package tool hya wahed la commande kanste3mlouha pour instaaler ,  update , remove packege on debian ",
    "aptitude" : "hya wahed front end advanced package tool li katzide user interface  w katsmeh l user bch y9lb ela package bch y instale w ysuprimihe",
    "apt vs aptitude" : "apt hya line commande bla GUI w aptitude katsuporte GU w aptitude is heigh level package manager l3eks dyl apt li hya low-level package manger wt9der tsete3ml mn taraf other heigh levl package manager "
    
    }

while 1:
    x = str(input("what do you want know "))
    y = doc.get(x)
    print(y)
    print("-----------------------------------------------------")
    