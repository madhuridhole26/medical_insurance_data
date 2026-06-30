import pickle
import json
import pandas as pd
import numpy as np
import config
from src.database import get_data_collection

class MedicalInsurence:
    def __init__(self):
        pass

    def load_model(self):
        with open(r"artifacts\linear_reg_med_ins.pkl","rb") as f:
            self.model=pickle.load(f)

    def load_col_data(self):
        with open(r"artifacts\med_ins_col_data.json","r") as f:
            self.input_columns=json.load(f)
            return self.input_columns

    def create_test_df(self):
        self.load_model()
        self.load_col_data()
        self.test_array=np.zeros((1,self.model.n_features_in_))

        self.test_array[0,0]=self.data["age"]
        self.test_array[0,1]=self.input_columns["gender"][self.data["gender"]]
        self.test_array[0,2]=self.data["bmi"]
        self.test_array[0,3]=self.data["children"]
        self.test_array[0,4]=self.input_columns['smoker'][self.data["smoker"]]

        region=f"region_{self.data["region"]}"
        region_index=self.input_columns["colNames"].index(region)

        self.test_array[0,region_index]=1

        self.test_df=pd.DataFrame(self.test_array,columns=self.model.feature_names_in_)


    def predict_charges(self,user_input_data):
        self.data = dict(user_input_data)
        print("DATA =", dict(user_input_data))
        print(user_input_data)
        self.data["age"]=int(self.data["age"])
        self.data["bmi"]=float(self.data["bmi"])
        self.data["children"]=int(self.data["children"])
        self.create_test_df()
        self.predicted_charges=np.around(self.model.predict(self.test_df),4)

        print("Predicted Charges:",self.predicted_charges)
        self.save_data_in_db()
        return self.predicted_charges[0]

    def save_data_in_db(self):
        self.input_data=self.data
        self.input_data["predicted_charges"]=self.predicted_charges[0]
        get_data_collection().insert_one(self.input_data)

    
