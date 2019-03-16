for d in */ ; do
    echo "$d"
    rm -rf $d*.aux
    rm -rf $d*.fdb_latexmk
    rm -rf $d*.fls
    rm -rf $d*.log
    rm -rf $d*.synctex.gz
    rm -rf $d*.DS_STORE
done

rm -rf .DS_STORE