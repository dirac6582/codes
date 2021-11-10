# required executables and pseudopotentials
BIN_LIST="pw.x ph.x" 
#PSEUDO_LIST="Si.pz-vbc.UPF Al.pz-vbc.UPF Cu.pz-d-rrkjus.UPF Ni.pz-nd-rrkjus.UPF"

echo $PREFIX

echo " "
echo   executables directory: $BIN_DIR
echo   pseudo directory:      $PSEUDO_DIR
echo   checking that needed directories and files exist...\c


# check for directories
for DIR in "$BIN_DIR" "$PSEUDO_DIR" ; do
    if test ! -d $DIR ; then
        echo
        echo "ERROR: $DIR not existent or not a directory"
        echo "Aborting"
        exit 1
    fi
done


# check for executables
for FILE in $BIN_LIST ; do
    if test ! -x $BIN_DIR/$FILE ; then
        echo
        echo "ERROR: $BIN_DIR/$FILE not existent or not executable"
        echo "Aborting"
        exit 1
    fi
done

# # check for pseudopotentials
# for FILE in $PSEUDO_LIST ; do
#     if test ! -r $PSEUDO_DIR/$FILE ; then
#        echo
#        echo "Downloading $FILE to $PSEUDO_DIR...\c"
#             $WGET $PSEUDO_DIR/$FILE $NETWORK_PSEUDO/$FILE 2> /dev/null
#     fi
#     if test $? != 0; then
#         echo
#         echo "ERROR: $PSEUDO_DIR/$FILE not existent or not readable"
#         echo "Aborting"
#         exit 1
#     fi
# done

echo
echo " done"
echo
