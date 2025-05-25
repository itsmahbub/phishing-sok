import matplotlib.pyplot as plt
import numpy as np

unique_phishing_detected = {
    '2020': {'Q1': 164.772, 'Q2': 146.994, 'Q3': 571.764, 'Q4': 637.302},
    '2021': {'Q1': 611.877, 'Q2': 616.939, 'Q3': 730.372, 'Q4': 888.585},
    '2022': {'Q1': 1025.968, 'Q2': 1097.811, 'Q3': 1270.883, 'Q4': 1350.037},
    '2023': {'Q1': 1624.144, 'Q2': 1286.208, 'Q3': 999.956, 'Q4': 1077.501},
    '2024': {'Q1': 963.994, 'Q2': 877.536, 'Q3': 932.923, 'Q4': 989.123}
}

phishing_reported = {
    "2020": 241.342,
    "2021": 323.972,
    "2022": 300.497,
    "2023": 298.878,
    # "2024": 0
}

cybercrime_reported = {
    "2020": 791.790,
    "2021": 847.376,
    "2022": 800.944,
    "2023": 880.418,
    # "2024": 0
}

cybercrime_losses = {
    "2020": 4.2,
    "2021": 6.9,
    "2022": 10.3,
    "2023": 12.5,
    # "2024": 0
}


# Prepare data for plotting
years = list(unique_phishing_detected.keys())
unique_phishing_detected_total = [np.sum(list(unique_phishing_detected[year].values())) for year in years]
phishing_reported_values = list(phishing_reported.values())
cybercrime_reported_values = list(cybercrime_reported.values())
cybercrime_losses_values = list(cybercrime_losses.values())

# Plot first graph: Unique Phishing Detected and Phishing Reported
plt.figure(figsize=(10, 6))
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(years, unique_phishing_detected_total, label='Unique Phishing Detected', marker='o', color='blue')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Unique Phishing Detected (in thousands)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
years = list(phishing_reported.keys())
ax2.plot(years, phishing_reported_values, label='Phishing Reported', marker='o', color='red')
ax2.set_ylabel('Phishing Reported (in thousands)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Unique Phishing Detected and Phishing Reported (2020-2024)', fontsize=14)
plt.tight_layout()  # Automatically adjust layout to prevent cutting off labels
plt.savefig('phishing-detected-and-complaints.png')


# Plot second graph: Cybercrime Reported and Losses
plt.figure(figsize=(10, 6))
fig, ax1 = plt.subplots(figsize=(10, 6))

years = list(cybercrime_reported.keys())
ax1.plot(years, cybercrime_reported_values, label='Cybercrime Reported', marker='o', color='blue')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cybercrime Reported (in thousands)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
years = list(cybercrime_losses.keys())
ax2.plot(years, cybercrime_losses_values, label='Cybercrime Losses (in billions)', marker='o', color='red')
ax2.set_ylabel('Cybercrime Losses (in billions)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Cybercrime Reported and Losses (2020-2024)', fontsize=14)
plt.tight_layout()  # Automatically adjust layout to prevent cutting off labels
plt.savefig("cybercrime-complaints-and-losses.png")


# Plot
plt.figure(figsize=(10, 6))
fig, ax1 = plt.subplots(figsize=(10, 6))

# plt.figure(figsize=(10, 6))
years = list(unique_phishing_detected.keys())
ax1.plot(years, unique_phishing_detected_total, marker='o', label='Unique Phishing Detected')

years = list(phishing_reported.keys())
ax1.plot(years, phishing_reported_values, marker='o', label='Phishing Reported')

years = list(cybercrime_reported.keys())
ax1.plot(years, cybercrime_reported_values, marker='o', label='Cybercrime Reported')

# Labels and Title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Count (in thousands)', fontsize=12)
ax1.tick_params(axis='y', labelcolor='black')

ax2 = ax1.twinx()
years = list(cybercrime_losses.keys())
ax2.plot(years, cybercrime_losses_values, label='Cybercrime Losses (in billions)', marker='o', color='red')
ax2.set_ylabel('Cybercrime Losses (in billions)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Trends in Phishing and Cybercrime (2020-2024)')

ax1.legend()
# ax2.legend()
plt.tight_layout()  # Automatically adjust layout to prevent cutting off labels
# Show Plot
plt.savefig('phishing-cybercrime-trend.png')
