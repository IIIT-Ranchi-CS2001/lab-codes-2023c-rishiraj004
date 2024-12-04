import matplotlib.pyplot as plt

# Data for Madhya Pradesh
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]

# Data for Rajasthan
rj_parties = ['INC', 'BJP', 'BSP', 'Others']
rj_seats = [69, 115, 2, 13]

mp_percent = [x / sum(mp_seats) * 100 for x in mp_seats]
rj_percent = [x / sum(rj_seats) * 100 for x in rj_seats]

# Pie Charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Madhya Pradesh Pie Chart
axs[0].pie(mp_percent, labels=mp_parties, autopct='%1.1f%%', explode=[0.03 if x == max(mp_percent) else 0 for x in mp_percent])
axs[0].set_title('Madhya Pradesh Seat Share')

# Rajasthan Pie Chart
axs[1].pie(rj_percent, labels=rj_parties, autopct='%1.1f%%', explode=[0.02 if x == max(rj_percent) else 0 for x in rj_percent])
axs[1].set_title('Rajasthan Seat Share')

plt.show()

# Bar Chart
x = range(len(mp_parties))  # Same parties in both states
width = 0.4
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - width / 2 for i in x], mp_seats, width=width, label='Madhya Pradesh', color='blue')
ax.bar([i + width / 2 for i in x], rj_seats, width=width, label='Rajasthan', color='orange')

# Adding labels and legend
ax.set_xticks(x)
ax.set_xticklabels(mp_parties)
ax.set_xlabel('Parties')
ax.set_ylabel('Seats Won')
ax.set_title('Assembly Elections 2023 Seat Distribution')
ax.legend()
plt.show()
