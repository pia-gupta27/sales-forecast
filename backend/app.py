from flask import Flask, request, jsonify, send_file
import pandas as pd 
import pickle
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('form.html')

@app.route('/predict_sales', methods=['POST'])
    
def predict_sales():
    print(request.form)

    def convert_input(input_data):
        user_input = {
            'Item_Weight': int(input_data.get('Item_Weight')),
            'Item_Fat_Content': int(input_data.get('Item_Fat_Content')),
            'Item_Visibility': float(input_data.get('Item_Visibility')),
            'Item_MRP': int(input_data.get('Item_MRP')),
            'Outlet_Size': int(input_data.get('Outlet_Size')),
            'Outlet_Location_Type': int(input_data.get('Outlet_Location_Type')),
            'Outlet_Type': int(input_data.get('Outlet_Location_Type')), 
            'Outlet_Age': int(input_data.get('Outlet_Age', 0)),
        }

        # Assuming binary (0 or 1) for the presence of each item type
        item_types = [
            'Breads', 'Breakfast', 'Canned', 'Dairy', 'Frozen Foods', 'Fruits and Vegetables',
            'Hard Drinks', 'Health and Hygiene', 'Household', 'Meat', 'Others', 'Seafood',
            'Snack Foods', 'Soft Drinks', 'Starchy Foods'
        ]
        for item_type in item_types:
            user_input[f'Item_Type_{item_type}'] = int(input_data.get(f'Item_Type_{item_type}', 0))

        # Assuming binary (0 or 1) for the presence of each outlet identifier
        outlet_identifiers = [
            'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'
        ]
        for outlet_identifier in outlet_identifiers:
            user_input[f'Outlet_Identifier_{outlet_identifier}'] = int(input_data.get(f'Outlet_Identifier_{outlet_identifier}', 0))

        return user_input

    dummy_input = {
        'Item_Weight': 5,  # Assuming weight is between 5 to 20 units
        'Item_Fat_Content': 0,  # 0 for 'Low Fat', 1 for 'Regular'
        'Item_Visibility': 0.2,  # Assuming visibility is a value between 0.0 to 0.2
        'Item_MRP': 150,  # Assuming MRP is between 20 to 300 units
        'Outlet_Size': 2,  # 1 for 'Small', 2 for 'Medium', 3 for 'High'
        'Outlet_Location_Type': 1,  # Random integer between 1 to 3
        'Outlet_Type': 1,  # Random choice among 4 types
        'Outlet_Age': 15,  # Assuming outlet age is between 10 to 35 years
        # Assuming binary (0 or 1) for the presence of each item type
        'Item_Type_Breads': 1,
        'Item_Type_Breakfast': 0,
        'Item_Type_Canned': 0,
        'Item_Type_Dairy': 0,
        'Item_Type_Frozen Foods': 0,
        'Item_Type_Fruits and Vegetables': 0,
        'Item_Type_Hard Drinks': 0,
        'Item_Type_Health and Hygiene': 0,
        'Item_Type_Household': 0,
        'Item_Type_Meat': 0,
        'Item_Type_Others': 0,
        'Item_Type_Seafood': 0,
        'Item_Type_Snack Foods': 0,
        'Item_Type_Soft Drinks': 0,
        'Item_Type_Starchy Foods': 0,
        # Assuming binary (0 or 1) for the presence of each outlet identifier
        'Outlet_Identifier_OUT013': 0,
        'Outlet_Identifier_OUT017': 0,
        'Outlet_Identifier_OUT018': 0,
        'Outlet_Identifier_OUT019': 0,
        'Outlet_Identifier_OUT027': 1,
        'Outlet_Identifier_OUT035': 0,
        'Outlet_Identifier_OUT045': 0,
        'Outlet_Identifier_OUT046': 0,
        'Outlet_Identifier_OUT049': 0
    }

    user_input = convert_input(request.form)
    print(user_input)

    # Load the saved model from the file
    with open('BigMart_Sales_Model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    prediction = loaded_model.predict(pd.DataFrame([user_input]))

    return jsonify({'prediction': list(prediction)})   

if __name__ == '__main__':
    app.run(debug=True, port=3000)