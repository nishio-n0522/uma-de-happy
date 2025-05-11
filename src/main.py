import csv
import json
from pathlib import Path

from schemas.race_config import RaceConfig
import check_gami

RACE_CONFIG_DIR = "race_configs"
BET_SELECTIONS_DIR = "bet_selection_files"

def load_config(config_file: str) -> RaceConfig:
    path = f"./{RACE_CONFIG_DIR}/{config_file}"
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return RaceConfig(**config)

def load_bet_selections_csv(bet_selections_csv: str):
    path = f"./{BET_SELECTIONS_DIR}/{bet_selections_csv}"
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        # 1行目はヘッダーなのでスキップ
        next(reader)
        # 2行目以降をリストに格納
        data = [row for row in reader]

    return data

def save_result(results):
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"results":results}, f, indent=2, ensure_ascii=False)
    
def main(config_file):
    race_config = load_config(config_file)
    data = load_bet_selections_csv(race_config.bet_selections_csv)

    gami_checker = check_gami.GamiChecker(race_config.number_of_starters, data)

    is_gami, min_payout, max_payout, results = gami_checker.check_gami()

    print("がみった?", is_gami)
    print("購入金額: ", gami_checker.my_total_bets)
    print("最低払い戻し額: ", min_payout)
    print("最大払い戻し額: ", max_payout)
    save_result(results)

if __name__=="__main__":
    # csvファイルの名前を指定
    race_config_file = "race_config_20250511.json"

    main(race_config_file)