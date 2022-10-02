# Load and preprocess mypersonality

    def prep_status_data(self):
        df = pd.read_csv('data/myPersonality/mypersonality_final.csv', encoding="ISO-8859-1")
        df = self.convert_traits_to_boolean(df)
        return df