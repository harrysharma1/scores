import matplotlib.pyplot as plt

csv_file = open('score.csv','r')
score = (csv_file.read().split(","))
scores =[]
for i in score:
    if i.isdigit():
        scores.append(int(i))

day = [i+1 for i in range(len(scores))]
plt.plot(day, scores, color='red', marker='o')
plt.title('Productivity', fontsize=14)
plt.xlabel('Days (starting from 06-11-2023)', fontsize=14)
plt.ylabel('Productivity rating', fontsize=14)
plt.ylim(0, 15)
plt.grid(True)


plt.savefig("Figure_1.png")
