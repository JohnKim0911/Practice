import pandas as pd


class Record:

    def __init__(self):
        self.data = pd.read_csv("./data/record.csv")
        self.name = self.data["Name"].to_list()
        self.score = self.data["Score"].to_list()
        self.stage = self.data["Stage"].to_list()
        self.record_dict = {
            "Name": self.name,
            "Score": self.score,
            "Stage": self.stage
        }
        self.df = None
        self.df_dict = {}
        self.user_index = None

    def update_record(self, name, score, stage):
        self.name.append(name)
        self.score.append(score)
        self.stage.append(stage)

    def save_df_to_csv(self):
        self.df = pd.DataFrame(self.record_dict)
        self.df = self.df.sort_values("Score", ascending=False, ignore_index=True)
        self.df.index += 1
        self.df = self.df[:10]  # Only save up to the 10th rank
        self.df.to_csv("./data/record.csv")

    def update_df_dict(self):
        index_start = self.df.index.start
        index_end = self.df.index.stop
        self.df_dict["Rank"] = [index for index in range(index_start, index_end)]
        self.df_dict["Name"] = self.df["Name"].to_list()
        self.df_dict["Score"] = self.df["Score"].to_list()
        self.df_dict["Stage"] = self.df["Stage"].to_list()

    def check_user_rank(self, name, score, stage):
        # return the rank of the user
        if name in self.df_dict["Name"]:
            self.user_index = (self.df.index[
                (self.df['Name'] == name) &
                (self.df['Score'] == score) &
                (self.df['Stage'] == stage)][0])
