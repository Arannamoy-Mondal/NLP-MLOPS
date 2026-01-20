with mlflow.start_run():
    # perform hyperparam tuning
    grid_search=hyperparamer_tuning(X_train=X_train,y_train=y_train,param_grid=param1)
    
				# get the best model
    best_model=grid_search.best_estimator_
    
				# evaluate the best model
    y_pred=best_model.predict(X_test)
    mse=mean_squared_error(y_train,y_test)
    mlflow.log_param("best params n_estimators: ",grid_search.best_params_['n_estimators'])
    mlflow.log_param("best params max_depth: ",grid_search.best_params_['max_depth'])
    mlflow.log_param("best params min_samples_split: ",grid_search.best_params_['min_samples_split'])
    mlflow.log_param("best params min_sample_leaf: ",grid_search.best_params_['min_sample_leaf'])
    mlflow.log_metric("accuracy (mse): ",mse)

				# tracking uri
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
    tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
    if tracking_url_type_store!='file':
							mlflow.sklearn.log_model(best_model,"model",registered_model_name="Best randomforest model")
    # hello
	else:
       mlflow.sklearn.log_model(best_model,"model",signature=signature)
						