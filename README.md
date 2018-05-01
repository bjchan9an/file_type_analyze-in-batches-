# file_type_analyze-in-batches-
analyze files' type in a selected folder

## Dependent Libraries
there exist some useful packets to analyze the file's type,such as the 'filemagic'.However,it requires some extra libraries which make it a bit complex.So I finally choose the python packet——'filetype'.Only a command 'pip install filetype' to install and then you can start your work.

## Usage
I write this script to solve a CTF reverse game.I have got a large number of 'flag' files (after brute force), i'm sure the real flag file exist in these files,and maybe a '.jpg'.Then i need a script to find out.
