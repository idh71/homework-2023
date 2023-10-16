import pickle

# Open the file in binary read mode
with open('model1.bin', 'rb') as f_out1:
    # Load the pickled object (your model) from the file
    model = pickle.load(f_out1)
    
with open('dv.bin', 'rb') as f_out2:
    # Load the pickled object (your model) from the file
    dv = pickle.load(f_out2)    

client = {"job": "retired", "duration": 445, "poutcome": "success"}
client = dv.transform(client)
pred = model.predict_proba(client)[:, 1]

print(pred)