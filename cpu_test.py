import time

time_list = []
start_time = time.time()

for i in range(50000):
    time_list.append(time.time() - start_time)
    
file_name = "scenarios3 cpu_test.csv"
f = open(file_name, "w")
for i in range(len(time_list)):
    f.write(str(i) + ", " + format(time_list[i], ".8f") + "\n")
    # print(str(i) + ", " + str(time_list[i]) + "\n")
f.close()
