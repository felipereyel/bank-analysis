import csv


def load_data(filename):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    return dataset


def generate_custom_dataset(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def get_categories_by_attribute(attribute, dataset):
    categories = []
    for i in range(len(dataset)):
        vector = dataset[i]
        category = vector[attribute]
        if (category not in categories):
            categories.append(category)
    return categories


def get_category_probability_by_class(attribute, value, dataset):
    count = 0
    for i in range(len(dataset)):
        vector = dataset[i]
        category = vector[attribute]
        if (category == value):
            count += 1
    category_count = {'Category': value, 'Probability': round(float(count) / len(dataset), 3)}
    return category_count


def get_all_category_probabilities_by_class(attribute, dataset):
    category_probability_column_x_yes = []
    category_coluna = get_categories_by_attribute(attribute, dataset)
    for element in category_coluna:
            category_probability_column_x_yes.append(get_category_probability_by_class(attribute, element, dataset))
    return category_probability_column_x_yes


def find_naive_bayes_category_probability(custom_dataset, column0, column1, column2, column3):

    category_probability_column0 = get_all_category_probabilities_by_class(0, custom_dataset)
    print('category_probability_column0: ', category_probability_column0)
    category_probability_column1 = get_all_category_probabilities_by_class(1, custom_dataset)
    print('category_probability_column1: ', category_probability_column1)
    category_probability_column2 = get_all_category_probabilities_by_class(2, custom_dataset)
    print('category_probability_column2: ', category_probability_column2)
    category_probability_column3 = get_all_category_probabilities_by_class(3, custom_dataset)
    print('category_probability_column3: ', category_probability_column3)


    column0_index = next((index for (index, d) in enumerate(category_probability_column0) if d["Category"] == column0), None)
    column1_index = next((index for (index, d) in enumerate(category_probability_column1) if d["Category"] == column1), None)
    column2_index = next((index for (index, d) in enumerate(category_probability_column2) if d["Category"] == column2), None)
    column3_index = next((index for (index, d) in enumerate(category_probability_column3) if d["Category"] == column3), None)

    return round((category_probability_column0[column0_index]['Probability'] * 
            category_probability_column1[column1_index]['Probability'] *
            category_probability_column2[column2_index]['Probability'] *
            category_probability_column3[column3_index]['Probability']) ,3)


def find_naive_bayes_class_probability(dataset, column4):
    category_probability_column4 = get_all_category_probabilities_by_class(4, dataset)
    print('category_probability_column4: ', category_probability_column4)

    column4_index = next((index for (index, d) in enumerate(category_probability_column4) if d["Category"] == column4), None)

    return round(category_probability_column4[column4_index]['Probability'] ,3)

def find_naive_bayes_overall_probability(dataset, column0, column1, column2, column3):

    class_probability_yes = find_naive_bayes_class_probability(dataset, 'Sim')
    class_probability_no = find_naive_bayes_class_probability(dataset, 'Nao')

    custom_dataset = generate_custom_dataset(dataset)
    dataset_class_yes = custom_dataset.get('Sim')
    dataset_class_no = custom_dataset.get('Nao')

    category_probability_yes = find_naive_bayes_category_probability(dataset_class_yes, column0, column1, column2, column3)
    category_probability_no = find_naive_bayes_category_probability(dataset_class_no, column0, column1, column2, column3)

    overall_probability = {'Sim': round(category_probability_yes * class_probability_yes, 3),
                           'Nao': round(category_probability_no * class_probability_no, 3)}

    return overall_probability


def main():
    file_name = '../dataset/tenis.data'
    dataset = load_data(file_name)

    overall_probability = find_naive_bayes_overall_probability(dataset, 'Ensolarado', 'Quente', 'Alta', 'Fraco')
    print(overall_probability)


main()