model_b = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100, input_length=X_train_padded.shape[1]),
    Bidirectional(LSTM(50, return_sequences=True)),
    Bidirectional(LSTM(50)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])