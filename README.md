Results browser in `./scores`

The key files in each dir `./scores/*/csvs` are:

- `analysis_outs.json`: correlation scores (shown only if p<.001) between different features and transfer success (eval chrF++)
- `chrf.csv`: evaluation chrF++ from training on each language X and testing on each language Y
- `heat_map_scores.png`: a visualization of the data in `chrf.csv` in a more understandable heat map form
- `dev_set_chrf_color.png`: plot with the untranslated chrF++ between X and Y dev sets on the x-axis and eval chrF++
- `lid_confusion_score_color.png`: like `dev_set_chrf_color.png`, but with LID confusion score between X and Y on the x-axis
- `phylogenetic_distance_color.png`: like `dev_set_chrf_color.png`, but with the inverse phylogenetic distance between X and Y on the x-axis
- `png_legend.md`: the legend for which colors represent which languages in the scatter plots, if needed for reference along with `chrf.csv`
- `tree.png`: a decision tree fit using the features in `analysis_outs.json` with the eval chrF++ as the objective value and (X,Y) pairs as data points
- `spbleu.csv`: like `chrf.csv`, but using SpBLEU instead of chrF++ (not used primarily for analysis in the paper)

The features listed in `analysis_outs.json` are listed here.

Creole-specific features:

- `is_related` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is a substrate or superstrate of Y, or another Creole language
- `is_substrate` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is a hypothesized substrate of Y
- `is_superstrate` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is a lexifier of Y
- `is_superstrate_or_related_creole` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is either Y's superstrate or a Creole language with the same substrate
- `is_creole` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is a Creole language like Y
- `has_common_superstrate` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is a Creole language with the same superstrate as Y
- `is_morphosyntactically_related` *FOR CREOLE LANGUAGE SETS ONLY*: whether X is either one of Y's substrates or a Creole language with substrates in the same language family as Y's substrates 

General features: 

- `in_pretrain`: whether X is one of the languages mBART-50 was trained on (nothing more than a rough approximation of resource-level in experiments that don't involve mBART-50)
- `same_script`: whether X and Y are written with the same script
- `dev_set_chrf`: the chrF++ between untranslated dev sets for X and Y
- `lid_confusion_score`: the probability that an LID model (fit on the language collection train data) gives a Y sentence of being X, on average
- `phylogenetic_distance`: the inverse of the number of edges to traverse from X to Y in the Glottolog tree (should probably have been named `phylogenetic_similarity`)
- `sentence_token_overlap`: average proportion of overlapping tokens between a Y sentence and its corresponding X sentence in their dev sets
- `devset_token_overlap`: proportion of shared tokens in X's and Y's entire dev sets
- `morphology_ratio`: absolute value of the log ratio between X's type-token ratio and Y's type-token ratio
- `fast_align_similarity`: inverse of the average proportion of reorderings between corresponding X and Y dev sentences aligned at the token level with fast-align
- `same_script_as_tgt`: whether X and Z have the same script
- `random_binary`: random integer 0 or 1 (control)
- `random_float`: random decimal number between 0 and 1 (control)

