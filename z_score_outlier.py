import speech_recognition as sr
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore


def listen_for_values():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Please speak the values separated by 'space'")
            audio = recognizer.listen(source)

        try:
            values = recognizer.recognize_google(audio).split()
            # Attempt to convert values to floats, skip non-numeric values
            values = [float(val.strip()) for val in values if val.strip().replace('.', '', 1).isdigit()]

            if len(values) > 0:
                return values
            else:
                print("No valid numeric values detected. Please try again.")

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio. Please try again.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except ValueError:
            print("Non-numeric values detected. Please speak only numeric values.")


def find_outliers_zscore(values):
    z_scores = zscore(values)
    outliers = np.where(np.abs(z_scores) > 3)[0]
    return outliers


def find_outliers_iqr(values):
    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = np.where((values < lower_bound) | (values > upper_bound))[0]
    return outliers


def plot_graph(values, outliers, method):
    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(values)), values, color='blue', label='Data Points')
    plt.scatter(outliers, [values[i] for i in outliers], color='red', label='Outliers')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title(f'Outlier Detection using {method}')
    plt.legend()
    plt.show()


def main():
    values = listen_for_values()

    if values:
        outliers_zscore = find_outliers_zscore(values)
        outliers_iqr = find_outliers_iqr(values)

        print("Detected outliers using Z-Score at indices:", outliers_zscore)
        plot_graph(values, outliers_zscore, 'Z-Score')

        print("Detected outliers using IQR at indices:", outliers_iqr)
        plot_graph(values, outliers_iqr, 'IQR')


if __name__ == "__main__":
    main()
