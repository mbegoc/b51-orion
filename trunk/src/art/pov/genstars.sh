#!/bin/bash

#permet de regenerer les images.

if [ -z $1 ]
then
    SIZEY=60
else
    SIZEY=$1
fi



let SIZEX=$SIZEY+$SIZEY/3

#l'utilisation du channel alpha donne des resultats desastreux
#Output_Alpha=true

ls -1 *.pov | while read line; do NEWNAME=$(echo ${line} | sed 's/.pov$/.png/'); povray Input_File_Name=${line} Output_File_Name=$NEWNAME Output_File_Type=N Antialias=true Height=$SIZEY Width=$SIZEX DISPLAY=false; done

#separe en deux lignes pour un peu plus de clarte...
ls -1 *.png | while read line; do NEWNAME=$(echo ${line} | sed 's/.png$/.jpg/'); convert $line $NEWNAME; done

rm *.png


exit 0