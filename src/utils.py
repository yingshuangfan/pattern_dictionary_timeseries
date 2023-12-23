### Discretization using

def uniform_quantization(samples, min_value, max_value, num_bins):
    bin_size = (max_value - min_value) / num_bins

    discretized_samples = []
    for sample in samples:
        sample = max(min(sample, max_value), min_value)
        bin_index = int((sample - min_value) / bin_size)
        discretized_value = min_value + bin_size * (bin_index + 0.5)
        discretized_value = round(discretized_value, 6)
        discretized_samples.append(discretized_value)

    return discretized_samples

real_valued_samples = [1.2, 2.5, 3.7, 4.1, 5.6, 6.8, 7.9, 8.0, 9.1, 10.2]

min_val = min(real_valued_samples)
max_val = max(real_valued_samples)
number_of_bins = 10

# Discretize the samples
discretized_series = uniform_quantization(real_valued_samples, min_val, max_val, number_of_bins)
print(discretized_series)