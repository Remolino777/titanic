def safe_transform(encoder, values):
    transformed_values = []
    for item in values:
        try:
            transformed_values.append(encoder.transform([item])[0])
        except ValueError:
            # Asigna un valor específico para valores no vistos, por ejemplo, -1
            transformed_values.append(-1)
    return transformed_values