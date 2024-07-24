
def split_data(data_dict, train_to_rest_ratio, val_to_test_ratio, r_state):
    """
    Splits the data into train, test, validation sets
    """
    full_data = pd.DataFrame(data_dict, columns=["label", "music"])
    X_train, X_test_val, y_train, y_test_val = train_test_split(full_data.music, full_data.label, test_size=train_to_rest_ratio, random_state=r_state)
    X_test, X_val, y_test, y_val = train_test_split(X_test_val, y_test_val, test_size=val_to_test_ratio, random_state=r_state)
    return X_train, X_test, X_val, y_train, y_test, y_val
