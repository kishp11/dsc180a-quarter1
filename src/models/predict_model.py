from src.features.build_datasets import vectorize

def evaluate_model(model, dataset):
    test_accuracy = model.evaluate(dataset, batch_size=8)
    return test_accuracy

def predict_from_file(model, filepath):
    vectors = vectorize(filepath)
    predictions = model.predict(vectors)
    return [1 if p > 0.5 else 0 for p in predictions]