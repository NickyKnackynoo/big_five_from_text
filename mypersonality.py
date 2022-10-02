
trait_score_dict = {
            'O': 'sOPN',
            'C': 'sCON',
            'E': 'sEXT',
            'A': 'sAGR',
            'N': 'sNEU',
            'Openness': 'sOPN',
            'Conscientiousness': 'sCON',
            'Extraversion': 'sEXT',
            'Agreeableness': 'sAGR',
            'Neuroticism': 'sNEU'
            }



# Load and preprocess mypersonality

def prep_status_data():
    df = pd.read_csv(path, encoding="ISO-8859-1")
    return df


def prep_data(trait, regression=False, model_comparison=False):
        df_status = self.prep_status_data()
        # df_essay = self.prep_essay_data()

        tfidf = TfidfVectorizer(stop_words='english', strip_accents='ascii')


            # result = tfidf.fit_transform(df_status['STATUS']).todense()

            # If need data to compare models
            if model_comparison:
                X = tfidf.fit_transform(df_status['STATUS'])
                # X = np.nan_to_num(np.column_stack((result, df_status[other_features_columns])))
            # Data to fit production model
            else:
                X = df_status['STATUS']


                y_column = self.trait_score_dict[trait]
            else:
                y_column = self.trait_cat_dict[trait]
            y = df_status[y_column]

        return X, y