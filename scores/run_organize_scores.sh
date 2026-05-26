#!/bin/bash

FNS=( 
scores/scratch/bible_bible_ind_4k
scores/scratch/bible_bible_vie_4k
scores/scratch/bible_bible_eng_4k
scores/scratch/bible_bible_ces_4k
scores/scratch/bible_bible_rus_4k
scores/scratch/bible_bible_jpn_4k
scores/scratch/bible_bible_ind_8k
scores/scratch/bible_bible_vie_8k
scores/scratch/bible_bible_eng_8k
scores/scratch/bible_bible_ces_8k
scores/scratch/bible_bible_rus_8k
scores/scratch/bible_bible_jpn_8k
scores/scratch/burmo-qiangic_eng
scores/scratch/philippine_eng
scores/scratch/italic_eng
scores/scratch/east_bantu_eng
scores/scratch/indo-aryan_eng
scores/scratch/semitic_eng
scores/scratch/turkic_eng
scores/scratch/bible_bible_hui_20k
scores/scratch/bible_bible_quz_20k
scores/scratch/parac20k_ell
scores/scratch/parac5k_ell
scores/scratch/parac3k_ell
scores/scratch/parac1k_ell
scores/scratch/parac300_ell
)

for fn in ${FNS[@]}; do
    myfn=${fn//scores\//}
    python3 organize_scores.py --dir $myfn/jsons
    outdir=$myfn/csvs
    ls $outdir/*.csv 
    ls $outdir/score.csv
    git add -f $outdir/*.csv
    echo "git added"
    echo ""
done

echo ""
echo done

