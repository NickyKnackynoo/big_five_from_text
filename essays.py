





    def prep_essay_data(self):
        df_essays = pd.read_csv('data/personality-detection-my-copy/essays.csv', encoding="ISO-8859-1")
        df_mairesse = pd.read_csv('data/personality-detection-my-copy/mairesse.csv', encoding="ISO-8859-1", header=None)


        df_mairesse.columns = ['#AUTHID'] + self.LIWC_features

        df = df_essays.merge(df_mairesse, how = 'inner', on = ['#AUTHID'])

        # add word count (WC) column
        df['WC'] = df['TEXT'].str.split().str.len()

        df = self.convert_traits_to_boolean(df)

        return df