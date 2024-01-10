from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render
from django.http import HttpResponse
import time
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the tokenizer
with open('./savedModels/tokenizer.pkl', 'rb') as tokenizer_file:
    loaded_tokenizer = pickle.load(tokenizer_file)

# Load the model
loaded_model = load_model('./savedModels/model_weights.h5')

def predict(request):
    return render(request, 'index.html')

def predict_single(input_address):
    processed_input = loaded_tokenizer.texts_to_sequences([input_address])
    padded_input = pad_sequences(processed_input, maxlen=3)
    prediction = loaded_model.predict(padded_input)
    return prediction

def User(request):
    input_address = request.GET['address']

    # Measure execution time before parallelization
    start_time_before = time.time()

    # Single prediction (non-parallelized)
    prediction_single = predict_single(input_address)

    end_time_before = time.time()
    execution_time_before = end_time_before - start_time_before
    

    # Using ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=2) as executor:
        start_time_parallel = time.time()


        futures = [executor.submit(predict_single, input_address) for _ in range(2)]
        # Wait for all threads to complete
        predictions_parallel = [future.result() for future in futures]

        end_time_parallel = time.time()
        execution_time_parallel = end_time_parallel - start_time_parallel
        

    final_prediction_parallel = sum(predictions_parallel) / len(predictions_parallel)

    if final_prediction_parallel < 0.5:
        result = 'Not Cairo governorate'
    else:
        result = 'Cairo governorate'

    print(final_prediction_parallel)
    print(f"Execution time before parallelization: {execution_time_before} seconds")
    print(f"Execution time with 2 threads: {execution_time_parallel} seconds")
    return render(request, 'user.html', {'res': result, 'cf': final_prediction_parallel , 'T': execution_time_parallel , 't': execution_time_before})

