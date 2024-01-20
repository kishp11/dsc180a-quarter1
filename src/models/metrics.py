import keras.backend as K
from keras.metrics import TruePositives, FalsePositives, TrueNegatives, FalseNegatives

tp = TruePositives()
fp = FalsePositives()
tn = TrueNegatives()
fn = FalseNegatives()

# true and false positives and negatives
def __TPTNFPFN(y_true, y_pred):
    return tp(y_true, y_pred), tn(y_true, y_pred), fp(y_true, y_pred), fn(y_true, y_pred)

# sensitivity/recall metric
def sens(y_true, y_pred):
    # Assuming binary classification
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    sens = true_positives/(true_positives + false_negatives + K.epsilon()) * 100 # K.epsilon() is a small constant that prevents divide by zero errors
    return sens

# specificity metric
def spec(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    spec = true_negatives/(true_negatives + false_positives + K.epsilon()) * 100
    return spec

# accuracy metric
def acc(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    acc = (true_positives + true_negatives)/(true_positives + false_positives + true_negatives + false_negatives + K.epsilon()) * 100
    return acc

# matthews correlation coefficient
def mcc(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    mcc = (((true_positives * true_negatives) - (false_negatives * false_positives)) / 
            K.sqrt((true_positives + false_negatives) * (true_negatives + false_positives) * (true_positives + false_positives) * (true_negatives + false_negatives)) + K.epsilon())
    return mcc
