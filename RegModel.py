import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('StudyExam.csv')

def loss_function(m, b, points):
    for point in points:
        x = point.StudyHours 
        y = point.ExamScore 

        totalError += (y -  (b + m * x)) ** 2
    return totalError / len(points)

def gradient_descent(m_now, b_now, L, points):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for point in range(n):
        x = points.iloc[point].StudyHours
        y = points.iloc[point].ExamScore

        m_gradient += -(2/n) * ( x * ( y - ( b_now + m_now * x ) ) )
        b_gradient += -(2/n) * ( ( y - ( b_now + m_now * x ) ) )
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

def predict(m, b, input):
    prediction = b + input * m

    return max(0, min(prediction, 20))


#main function : 
m = 0
b = 0
L = 0.0001
generations = 20000

for i in range(generations):
    if( i%50 == 0 ):
        print(f'Generation : {i}\nm = {m}\nb = {b}')
        m, b = gradient_descent(m, b, L, data)

print(m, b)

X = int(input("Donner le nombre d'heures : "))

prediction = predict(m, b, X)
print(f'the prediction for {X} hours of study is : {prediction}')

plt.scatter(data.StudyHours, data.ExamScore, color='black')
plt.plot(list(range(0, 40)), [ b + m * x for x in range(0, 40) ], color='red')
plt.show()