class GamiChecker:
    def __init__(self, nubmer_of_starters: int, my_bets: list[list]):
        self.number_of_starters = nubmer_of_starters
        self.my_bets = my_bets

        self.my_total_bets = self.get_total_bets()

    def check_gami(self):
        # self.number_of_starersが出走数とするとき、
        # 3着以内の馬の全て組み合わせに対して、処理を実行する

        results = []
        is_gami = False
        min_payout = 9999999999999999999999999999999999
        max_payout = 0

        for i in range(self.number_of_starters):
            for j in range(self.number_of_starters):
                if i == j:
                    continue

                for k in range(self.number_of_starters):
                    if i == k or j == k:
                        continue

                    win_numbers = [i+1, j+1, k+1]
                    payout = 0
                    is_hit = False
                    

                    for my_bet in self.my_bets:
                        bet_type = my_bet[0]
                        selections_str: str = my_bet[1]
                        bet_selection = [int (selection) for selection in selections_str.split("-")]
                        odds = float(my_bet[2])
                        odds_us = float(my_bet[3])
                        bet_amount = int(my_bet[4])

                        if (self.check_hit(bet_type, bet_selection, win_numbers)):
                            payout += odds * bet_amount
                            is_hit = True

                    if payout < self.my_total_bets:
                        is_gami = True

                    if payout != 0 and min_payout > payout:
                        min_payout = payout

                    if max_payout < payout:
                        max_payout = payout

                    if is_hit:
                        results.append({
                            "win_numbers": win_numbers,
                            "my_total_bets": self.my_total_bets,
                            "payout": payout
                        })

        return is_gami, min_payout, max_payout, results



                
    def check_hit(self, bet_type: str, bet_selection: list, win_numbers: list):
        if bet_type == "単勝":
            return bet_selection[0] == win_numbers[0]
        elif bet_type == "複勝":
            return bet_selection[0] in win_numbers
        elif bet_type == "馬連":
            return set(bet_selection[:2]) == set(win_numbers[:2])
        elif bet_type == "ワイド":
            return bet_selection[0] in win_numbers and bet_selection[1] in win_numbers
        elif bet_type == "馬単":
            return bet_selection[:2] == win_numbers[:2]
        elif bet_type == "三連複":
            return set(bet_selection) == set(win_numbers)
        elif bet_type == "三連単":
            return bet_selection == win_numbers
        
    def get_total_bets(self):
        total_bets = 0
        for my_bet in self.my_bets:
            total_bets += int(my_bet[4])
        return total_bets