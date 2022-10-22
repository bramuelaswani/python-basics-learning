import ipywidgets as widgets


def make_cnf_matrix(threshold):
    y_pred_proba=model.predict_proba(X_test)[:,-1]
    y_pred=y_pred_proba > threshold
    conf_matrix=confusion_matrix(y_test,y_pred)
    tn,fp,fn,tp=conf_matrix.ravel()
    print(f"profit: €{tp*100_000_000}")
    print(f"Losses: €{fp*250_000_000}")
    ConfusionMatrixDisplay.from_predictions(y_test,y_pred,colorbar=False)


thresh_widget = widgets.FloatLogSlider(min=0,max=1,value=0.5,step=0.5)
