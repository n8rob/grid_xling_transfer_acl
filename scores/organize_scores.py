import json, glob, re, os, argparse, pdb 

from tqdm import tqdm 
import pandas as pd 

def create_latex_table(
    dir_="apics_apics/jsons",
    format_str="train_{}_test_{}_into_{}_scores.json"
):
    # make regex_str and grep_str 
    regex_str = r'' + format_str.format(
        '([a-z]{3}[a-z]?[0-9]*\_?[A-Z]*[a-z]*)\+?[a-z]*[0-9]*\_?[A-Z]*[a-z]*',
        '([a-z]{3}[a-z]?[0-9]*\_?[A-Z]*[a-z]*)',
        '([a-z]{3}[a-z]?[0-9]*\_?[A-Z]*[a-z]*)',
    )
    fn_regex = re.compile(regex_str)
    grep_str = format_str.format('*', '*', '*')
    json_paths = glob.glob(
        os.path.join(dir_, grep_str)
    ) 

    # Loop 
    chrf_dict = {}
    spbleu_dict = {}
    # pdb.set_trace() 
    for json_path in tqdm(json_paths):
        train_src_lang = fn_regex.search(json_path)[1]
        test_src_lang = fn_regex.search(json_path)[2]
        tgt_lang = fn_regex.search(json_path)[3]

        with open(json_path, 'r') as f:
            score_data = json.load(f)
        
        if train_src_lang not in chrf_dict: 
            chrf_dict[train_src_lang] = {}
            spbleu_dict[train_src_lang] = {} 
        
        chrf_dict[train_src_lang][test_src_lang] = score_data[
            'chrF++'
        ]
        spbleu_dict[train_src_lang][test_src_lang] = score_data[
            'SpBLEU'
        ]
    
    # Sort dicts to make dfs 
    sorted_keys = list(chrf_dict.keys())
    sorted_keys.sort() 
    for key in sorted_keys:

        sorted_ks = list(chrf_dict[key].keys())
        sorted_ks.sort()
        chrf_dict[key] = {
            k: chrf_dict[key].get(k, '-') for k in sorted_ks
        }
        spbleu_dict[key] = {
            k: spbleu_dict[key].get(k, '-') for k in sorted_ks
        }
    chrf_dict = {key: chrf_dict[key] for key in sorted_keys}
    spbleu_dict = {key: spbleu_dict[key] for key in sorted_keys}
    # Make pandas dfs  
    chrf_df = pd.DataFrame(chrf_dict)
    spbleu_df = pd.DataFrame(spbleu_dict)

    dir_parent = os.path.split(dir_)[0]
    out_csv_dir = os.path.join(dir_parent, 'csvs')
    if not os.path.exists(out_csv_dir):
        os.makedirs(out_csv_dir)
    out_chrf_csv = os.path.join(out_csv_dir, 'chrf.csv')
    out_spbleu_csv = os.path.join(out_csv_dir, 'spbleu.csv')
    chrf_df.to_csv(out_chrf_csv)
    spbleu_df.to_csv(out_spbleu_csv)
    print("See", out_csv_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # REQUIRED ARGS 
    parser.add_argument("--dir", type=str, default="apics_apics/jsons")

    args = parser.parse_args()
    print(args)

    create_latex_table(dir_=args.dir)
