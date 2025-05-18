import numpy as np


def readFileContent(filename, heartRate):
    # Create an empty list to hold the data for the numeric fields
    data = []
    
    # Time will be stored separately as it can't easily go into the NumPy array
    time = None

    with open(filename, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split("=", 1)

                # Store values in the array based on the key
                if key == "Time":
                    continue
                elif key == "Age":
                    data.append(int(value))
                elif key == "sex":
                    data.append(int(value))
                elif key == "cp":
                    data.append(int(value))
                elif key == "trestbps":
                    data.append(int(value))
                elif key == "chol":
                    data.append(int(value))
                elif key == "fbs":
                    data.append(int(value))
                elif key == "restecg":
                    data.append(int(value))
                elif key == "thalach":
                    data.append(int(value))  #to force the live heart rate reading instad.
                elif key == "exang":
                    data.append(int(value))
                elif key == "oldpeak":
                    data.append(float(value))
                elif key == "slope":
                    data.append(int(value))
                elif key == "ca":
                    data.append(int(value))
                elif key == "thal":
                    data.append(int(value))
                elif key == "done":
                    break

    # Convert list to numpy array for numerical fields
    

    data2 = np.array([[data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]]]).reshape(1, -1)
    
    # Return both the NumPy array and the time separately
    return data2
