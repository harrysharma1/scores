import matplotlib.pyplot as plt


scores = [6,9,7,5,9,7,8,9,10,9,7,9,10,7,6,4,6,8,9,7,8,7,5,8,7,7,8,3,8,7,8,3,7,8,8,7,8,5,7,7,5]
day = [i+1 for i in range(len(scores))]
plt.plot(day, scores, color='red', marker='o')
plt.title('Productivity', fontsize=14)
plt.xlabel('days (starting from 06-11-2023)', fontsize=14)
plt.ylabel('feeling of productivity', fontsize=14)
plt.ylim(0, 15)
plt.grid(True)
plt.show()
