#!/bin/bash

# script per creare le repo di git in automatico all'inzio
# della gara e per mantenerle. Se runnato senza argomenti
# chiede quali delle cartelle nella root sono servizi e crea le repo
# in /root/repos. Se runnato con un argomento opera solo sulla repo fornita
# se incrontra una repo già inizializzata chiede all'utente se vuole aggiornarla 
# in production, e se sì pulla e rebuilda il servizio
# per clonare un servizio $servizio fai 
# git clone root@10.60.2.1:/root/repos/$servizio
# per pullare vai sulla /root/$servizio e pulla poi rebuilda

if [[ -z "$(command -v git)" ]]; then
    apt install git
fi;

if ! [[ -d /root/repos ]]; then
    mkdir /root/repos
fi

git config --global user.email "sus@sussone.com"
git config --global user.name "Gabibbo"
git config --global init.defaultBranch master

function create_repo() {
    file=$1
    base=`basename $file`

    bare="/root/repos/"$base

    if ! [[ -d $bare ]]; then
        mkdir $bare
        cd $bare
        git init --bare
        cd $file 
        git init
        git remote add origin $bare
        git add .
        git commit -m "init"
        git push -u origin master
        echo "=========================="
        echo "Creata repo per $base"
        echo "=========================="
    else
        echo "Esiste la repo per $base"
        read -p "Vuoi aggiornarla in production? [y/N] " yn
        if [[ $yn == "y" ]]; then
            echo "Aggiornata in repo in prod"
            cd $file
            git pull
            docker compose up --build -d
        fi
    fi
}

if [[ $# -eq 1 ]]; then
    if ! [[ -d $1 ]]; then
        echo "La cartella del servizio non esiste"
    fi

    create_repo `realpath $1`
fi
    

if [[ $# -eq 0 ]]; then
    for file in /root/*; do
        base=`basename $file`
        # ignora repos, tools, e snap
        if [[ -d $file && $base != "repos" && $base != "snap" && $base != "tools" ]] ; then
            read -p "$base è un servizio? [y/N] " yn
            if [[ $yn == "y" ]]; then
                create_repo $file                
            fi
        fi
    done
fi
