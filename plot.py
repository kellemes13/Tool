import matplotlib.pyplot as plt


# Define a function to read data from a file and plot a graph
def plot_bw(title, file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        data = file.readlines()


    # Process data
    x = []
    y = []
    i=1
    for line in data:
        values = line.split(',')
        y.append(int(values[1])/1000*20)
        x.append(i)
        i=i+1


    # Plot the graph
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('time(sec)')
    plt.ylabel('MB/s')
    plt.title(title+': bandwidth')
    plt.show()


# Define a function to read data from a file and plot a graph
def plot_clat(title, file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        data = file.readlines()


    # Process data
    x = []
    y = []
    i=1
    for line in data:
        values = line.split(',')
        y.append(int(values[1])/1000/20)
        x.append(i)
        i=i+1


    if title == 'rw':
      y_div = [element / 1000 for element in y]
      y_slot = sorted(y_div)
      plt.ylabel('ms')
    else:
      y_slot = sorted(y)
      plt.ylabel('us')
   
    x_percentage = [element / i *100 for element in x]


    # Plot the graph
    plt.plot(x_percentage, y_slot)
    plt.grid(True)
    plt.xlabel('%')
    plt.title(title+': clat')
    plt.show()


    # Define a function to read data from a file and plot a graph
def plot_iops(title,file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        data = file.readlines()


    # Process data
    x = []
    y = []
    i=1
    for line in data:
        values = line.split(',')
        y.append(int(values[1])*20)
        x.append(i)
        i=i+1
       
    y_kiops = [element / 1000 for element in y]


    # Plot the graph
    plt.plot(x, y_kiops)
    plt.grid(True)
    plt.xlabel('time(sec)')
    plt.ylabel('IO')
    plt.title(title + ':K-IOPS')
    plt.show()


# sequential write
plot_bw('sw','/content/sw_bw.1.log')
# random write
plot_iops('rw','/content/rw_iops.1.log')
plot_clat('rw','/content/rw_clat.1.log')
# sequential read
plot_bw('sr','/content/sr_bw.1.log')
# random read
plot_iops('rr','/content/rr_iops.1.log')
plot_clat('rr','/content/rr_clat.1.log')














