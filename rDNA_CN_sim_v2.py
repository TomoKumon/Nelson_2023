import random 
import math
import numpy as np
import matplotlib.pyplot as plt

StemCellNumber = 10
NumberOfDivisions = 2 * 14 #12h per division, 14days

def CopyNumSim(mag,seg,use):
	for i in range(StemCellNumber):
		GSCrDNA = InitialCopyNumber
		SGrDNA = InitialCopyNumber
		for j in range(NumberOfDivisions):
			CopyNumberChange = np.random.choice([0, 1], 1, p=[1-mag, mag])
			if CopyNumberChange == 0:
				GSCrDNA += 0
				SGrDNA += 0
			else:
				SR = math.sqrt(GSCrDNA)
				delta = np.round(np.random.normal(SR, SR, 1))
				direction = np.random.choice([1, -1], 1, p=[seg, 1-seg])
				SGrDNA = int(GSCrDNA-(delta*direction))
				GSCrDNA += int(delta*direction)
				if SGrDNA < 0:
					SGrDNA = 0
				if GSCrDNA < 0:
					GSCrDNA = 0
			USCE = np.random.choice([0, 1], 15, p=[1-use, use])
			SR = math.sqrt(SGrDNA)
			delt = np.round(np.random.normal(SR, SR, 1))
			dire = int(np.random.choice([1, -1], 1))
			change = USCE*delt*dire
			SC01 = SGrDNA + change[1] + change[2] + change[4] + change[8]
			SC02 = SGrDNA + change[1] + change[2] + change[4] - change[8]
			SC03 = SGrDNA + change[1] + change[2] - change[4] + change[9]
			SC04 = SGrDNA + change[1] + change[2] - change[4] - change[9]
			SC05 = SGrDNA + change[1] - change[2] + change[5] + change[10]
			SC06 = SGrDNA + change[1] - change[2] + change[5] - change[10]
			SC07 = SGrDNA + change[1] - change[2] - change[5] + change[11]
			SC08 = SGrDNA + change[1] - change[2] - change[5] - change[11]
			SC09 = SGrDNA - change[1] + change[3] + change[6] + change[12]
			SC10 = SGrDNA - change[1] + change[3] + change[6] - change[12]
			SC11 = SGrDNA - change[1] + change[3] - change[6] + change[13]
			SC12 = SGrDNA - change[1] + change[3] - change[6] - change[13]
			SC13 = SGrDNA - change[1] - change[3] + change[7] + change[14]
			SC14 = SGrDNA - change[1] - change[3] + change[7] - change[14]
			SC15 = SGrDNA - change[1] - change[3] - change[7] + change[0]
			SC16 = SGrDNA - change[1] - change[3] - change[7] - change[0]
			SpermRDNA.append(SC01)
			SpermRDNA.append(SC02)
			SpermRDNA.append(SC03)
			SpermRDNA.append(SC04)
			SpermRDNA.append(SC05)
			SpermRDNA.append(SC06)
			SpermRDNA.append(SC07)
			SpermRDNA.append(SC08)
			SpermRDNA.append(SC09)
			SpermRDNA.append(SC10)
			SpermRDNA.append(SC11)
			SpermRDNA.append(SC12)
			SpermRDNA.append(SC13)
			SpermRDNA.append(SC14)
			SpermRDNA.append(SC15)
			SpermRDNA.append(SC16)
fly = 100
InitialCopyNumber = 200

data1 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.04,0.50,0.00)
	data1 += SpermRDNA

data2 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.04,0.80,0.00)
	data2 += SpermRDNA

data3 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.04,0.20,0.00)
	data3 += SpermRDNA

InitialCopyNumber = 100

data4 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.50,0.00)
	data4 += SpermRDNA

data5 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.80,0.00)
	data5 += SpermRDNA

data6 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.20,0.00)
	data6 += SpermRDNA

data7 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.00,0.50,0.50)
	data7 += SpermRDNA

data8 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.00,0.80,0.50)
	data8 += SpermRDNA

data9 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.00,0.20,0.50)
	data9 += SpermRDNA

data10 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.50,0.50)
	data10 += SpermRDNA

data11 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.80,0.50)
	data11 += SpermRDNA

data12 = []
for f in range(fly):
	SpermRDNA = []
	CopyNumSim(0.50,0.20,0.50)
	data12 += SpermRDNA

data = list([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12])

fig, ax = plt.subplots()

ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)

#ax.set_xlabel('Frequency of Increased rDNA Inheritance')
ax.set_ylabel('rDNA copy number')
ax.set_ylim(0, 400)


# add x-tick labels
xticklabels = ['50%', '80%', '20%', '50%', '80%', '20%', '50%', '80%', '20%', '50%', '80%', '20%']
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
ax.set_xticklabels(xticklabels)

# add horizontal grid lines
ax.yaxis.grid(True)
plt.axhline(100, color='r', alpha = 0.5)
plt.axhline(200, color='b', alpha = 0.5)

fig.set_size_inches(8, 8)
# show the plot
fig.savefig("rDNA_CN.pdf")
