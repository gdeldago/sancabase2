#!/bin/bash
echo Agregando ...
git add .
echo .............
echo Haciendo commit ...
git commit -m "$1"
echo .............
echo Subiendo.....
git push origin master
echo ..... FIN
