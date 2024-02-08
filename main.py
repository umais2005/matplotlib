import re
from matplotlib import pyplot as plt 
def clean_lines(file):
    for index,line in enumerate(open(file)):
        if index>1 and index <11:
            line = line.strip()
            fields = re.split(r"\s+",line,5)[:5]
            yield fields
Dates = []
PredictedValues = []
HighValues = []
LowValues = []

for record in clean_lines("Predict.txt"):
    # print(record)
    date = record[0]+" "+record[1]
    Dates.append(date)
    PredictedValues.append(float(record[2]))
    HighValues.append(float(record[3]))
    LowValues.append(float(record[4]))
# print(Dates)
plt.plot(Dates,PredictedValues,color="#00FF00",label="Predicted")
plt.plot(Dates,HighValues ,color="#0000FF",label="Highs")
plt.plot(Dates,LowValues,color="#FF0000",label="Lows")

plt.legend()
plt.title("Sunspots Prediction")
plt.xlabel("Date (YYYY MM)")
plt.ylabel("Sunspot Number")
plt.grid(True)
plt.tight_layout()
plt.show()