X_test = pd.read_csv("data/mexico-city-test-features.csv")
print(X_test.info())
X_test.head()


y_test_pred = pd.Series(model.predict(X_test))
y_test_pred.head()


coefficients = model.named_steps["ridge"].coef_

features = model.named_steps["ridge"].intercept_
feature_names = model.named_steps["onehotencoder"].get_feature_names()

feat_imp = pd.Series(coefficients, index=feature_names)

feat_imp
