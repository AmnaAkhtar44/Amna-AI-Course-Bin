import pandas as pd
import numpy as np
import sklearn.preprocessing

df = pd.read_csv('Week4/EncodingCategoricalData.csv')
print(df.head())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['class_encoded'] = le.fit_transform(df['class'])

print("Class labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['class', 'class_encoded']].head())
from sklearn.preprocessing import OneHotEncoder

categorical_cols = ['buying', 'maint',
                    'doors', 'persons', 'lug_boot', 'safety']
ohe = OneHotEncoder(sparse_output=False)

ohe_array = ohe.fit_transform(df[categorical_cols])
print("OHE feature names:", ohe.get_feature_names_out(categorical_cols))

ohe_df = pd.DataFrame(
    ohe_array, columns=ohe.get_feature_names_out(categorical_cols))
df_ohe = pd.concat([df.reset_index(drop=True), ohe_df], axis=1)
print(df_ohe.head())

from sklearn.preprocessing import OrdinalEncoder

ordinal_cols = ['safety']
categories_order = [['low', 'med', 'high']]

oe = OrdinalEncoder(categories=categories_order)
df['safety_ord'] = oe.fit_transform(df[['safety']])

print(df[['safety', 'safety_ord']].head())

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

ordinal_features = ['safety']
ordinal_categories = [['low', 'med', 'high']]

nominal_features = ['buying', 'maint', 'doors', 'persons', 'lug_boot']

preprocessor = ColumnTransformer(
    transformers=[
        ('ord', OrdinalEncoder(categories=ordinal_categories), ordinal_features),
        ('nom', OneHotEncoder(sparse_output=False), nominal_features)
    ]
)

features = ordinal_features + nominal_features
X = df[features]
X_prepared = preprocessor.fit_transform(X)

print("Transformed shape:", X_prepared.shape)

final_df = pd.DataFrame(
    np.hstack([X_prepared, df[['class_encoded']].values]),
    columns = list(preprocessor.get_feature_names_out()) + ['class_encoded']
)
print(final_df.head())


