from cv19index import predict
import pandas as pd
from datetime import datetime
predict.do_run_claims("demographics.csv","claims.csv","predictions.csv","xgboost_all_ages",pd.to_datetime(datetime.today().isoformat()))