import sys, time
for i in range(2000):
    time.sleep(0.01)
    sys.stdout.write("\rProgress: {}%".format(str(i)))