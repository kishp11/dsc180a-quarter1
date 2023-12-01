
def evaluate_model(model, dataset):
    test_accuracy = model.evaluate(dataset, batch_size=8)
    return test_accuracy

