from src.features.build_datasets import vectorize

def evaluate_model(model, dataset):
    # Evaluate model on provided dataset and get test accuracy
    test_accuracy = model.evaluate(dataset, batch_size=8)
    return test_accuracy

def predict_from_file(model, filepath):
    # vectorize sequence data from the dataset file
    vectors = vectorize(filepath)

    # Make predictions from model
    predictions = model.predict(vectors)

    # Convert probability predictions to binary labels (0 or 1) based on a threshold of 0.5
    return [1 if p > 0.5 else 0 for p in predictions]
