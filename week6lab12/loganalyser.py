import pandas as pd

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()

    def load_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
           
        for line in lines:
            try:
                round_part, rolls_part = line.strip().split(":", 1)
            except ValueError:
                continue

            rolls_dict = {}
            for part in rolls_part.split(","):
                part = part.strip()
                if " rolled " in part:
                    name, _, roll = part.partition(" rolled ")
                    rolls_dict[name] = int(roll)
                    if name not in self.player_names:
                        self.player_names.append(name)
            self.data.append(rolls_dict)
           
        # Convert list of dicts to DataFrame
        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1  # rounds starting from 1
        self.df.index.name = "Round"

mylog = LogAnalyser()
mylog.load_data("results.txt")
print(mylog.df.shape)