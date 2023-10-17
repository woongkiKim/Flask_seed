class DataCleansing:

    def __init__(self):

        ## 범주형 변수
        self.cat_cols = ['Sex', 'Embarked', 'Deck', 'Family_Size_Class', 'Title', 'Pclass']
        
    def preprocess(self, df):

        ## init으로 선언한 변수 사용하기
        print("🔥🔥🔥 self.cat_cols:", self.cat_cols)

        df['Fare'] = df['Fare'].astype(float)
        df['Age'] = df['Age'].astype(int)
        df['SibSp'] = df['SibSp'].astype(int)
        df['Parch'] = df['Parch'].astype(int)

        df['Cabin'].fillna('Z', inplace=True)

        return df