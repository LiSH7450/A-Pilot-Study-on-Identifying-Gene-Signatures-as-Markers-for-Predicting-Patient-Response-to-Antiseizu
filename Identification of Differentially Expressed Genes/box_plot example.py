# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

drug_naive = [12.31216771,12.11827075,12.20214692,12.49172309,12.43059996,12.33961886,12.57274629,12.16288677,12.23681178,12.28364729,12.25457301,12.14159403,12.29683859]
VA_R = [12.29969439,11.93237533,11.99553797,11.88789528,12.109045,12.40440506,12.28299796,11.81616041,11.73836143,11.91506088,11.6963357,12.10552697,12.00404973,11.82378105,12.05432801]
VA_N = [11.9578756,12.17127315,11.99845524,12.0107835,12.27851599,12.36261496,12.46725555,12.39700752]



def plot_sig(xstart,xend,ystart,yend,sig):
    x = np.ones((2))*xstart
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)
    
    x = np.arange(xstart,xend+0.1,xend-xstart)
    y = yend-0.1+0*x
    plt.plot(x,y,label="$y$",color="black",linewidth=1)

    x0 = (xstart+xend)/2-0.1
    y0=yend-0.17
    plt.annotate(r'%s'%sig, xy=(x0, y0), xycoords='data', xytext=(-15, +1),
                 textcoords='offset points', fontsize=11,color="black")
    x = np.ones((2))*xend
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)

def plot_sig_down(xstart,xend,ystart,yend,sig):
    x = np.ones((2))*xstart
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)
    
    x = np.arange(xstart,xend+0.1,xend-xstart)
    y = ystart+0*x
    plt.plot(x,y,label="$y$",color="black",linewidth=1)

    x0 = (xstart+xend)/2-0.1
    y0=ystart+0.02
    plt.annotate(r'%s'%sig, xy=(x0, y0), xycoords='data', xytext=(-15, +1),
                 textcoords='offset points', fontsize=11,color="black")
    x = np.ones((2))*xend
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)


box_1 = drug_naive
box_2 = VA_R
box_3 = VA_N

plt.style.use('default')
fig,ax = plt.subplots(figsize=(5,5),dpi=300) 
bplot = ax.boxplot([box_1, box_2,box_3], labels=["Drug naive","VPA responder","VPA non-responder"],
                   flierprops = {'marker':'o','markerfacecolor':'khaki','color':'black'},
                   patch_artist=True)
ax.set_ylabel('NCOA4', fontsize=15)
plt.xticks([1,2,3],["Drug naive","VPA responder","VPA non-responder"])

plot_sig(1,1.95,12.6,12.8,'p=0.0002')
plot_sig(2.05,3,12.6,12.8,'p=0.0365')
plot_sig_down(1,3,11.6,11.8,'p=0.2315')

plt.show()