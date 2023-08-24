import statistics,math

# [150345833.333,0.7019,783.333]
data1 = [200000000,200,0]
data2 = [37500,2000,0.0957]

# to return the upper three quartiles
pearsons_coefficient = statistics.correlation(data1, data2)
print("The pearson's coefficient of the x and y inputs are: \n", pearsons_coefficient)


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_covariance(data1, data2):
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)
    covariance = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)
    return covariance


def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    standard_deviation = variance ** 0.5
    return standard_deviation


def calculate_pearson_correlation(data1, data2):
    covariance = calculate_covariance(data1, data2)
    standard_deviation1 = calculate_standard_deviation(data1)
    standard_deviation2 = calculate_standard_deviation(data2)
    correlation = covariance / (standard_deviation1 * standard_deviation2)
    return correlation


# Example usage

correlation = calculate_pearson_correlation(data1, data2)
print("Pearson Correlation Coefficient:", correlation)
