# imputer = SimpleImputer()
# imputer.fit(X_train)
ohe = OneHotEncoder(use_cat_names=True)
ohe.fit(X_train)
XT_train = ohe.transform(X_train)
# imputer = SimpleImputer()
# imputer.fit(X_train)
model = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    SimpleImputer(),
    # LinearRegression()
    Ridge()
)

model.fit(X_train, y_train)
