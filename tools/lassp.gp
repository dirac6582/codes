# ========================
# %file%
#
# ========================
# https://ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/paper_adv2.html
# Time-stamp: <2022-06-17 07:28:02 amanotomohito>


# output setting
set term pdfcairo enhanced # enhanced for latin
set output "test.pdf"


# if y2 axis is used ?
# http://blog.livedoor.jp/mwalker/archives/27403552.html
# set y2tics

# title
set title "mean 4-CV error"

# axis label
set xlabel "L1_ALPHA"
set ylabel "error"
# set y2label "y2"

# margin setting (if num is large, margin becomes large)
set lmargin 15 #left
set bmargin 5 #bottom


# plot
set logscale x
plot "TiO2223_cubic.cvscore" using 1:2  title "training",\
     "TiO2223_cubic.cvscore" using 1:4  title "validation"
