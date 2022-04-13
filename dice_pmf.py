
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_pmf(m,n,c):
    '''mDn+c = 3D6+2
    m=1
    n=6
    c=2
    '''
    die_list = []
    for i in range(n):
        die_list.append([i+1,1/n])

    # print(die_list)

    final_list = die_list
    for _ in range(m-1):
        sub_list = []
        for i in final_list:
            for j in die_list:
                sub_list.append([i[0]+j[0],i[1]*j[1]])
        final_list = sub_list

    for ix,i in enumerate(final_list):
        final_list[ix][0] = i[0]+c

    test_list = [i[0] for i in final_list]
    # print(final_list)

    result_list = []
    for i in set(list(zip(*final_list))[0]):
        result_list.append([i,0])


    return [test_list, final_list, result_list]

# result_list
# sum(list(zip(*result_list))[1])

# graph_data = np.array([list(zip(*result_list))[0],list(zip(*result_list))[1]])
# plt.bar(x=graph_data[0], height=graph_data[1])
# plt.show()

# graph_data = np.array(result_list)
# plt.bar(x=graph_data[:, 0], height=graph_data[:, 1])
# plt.show()

# x=2
# n=6
# m=0

# graph_data = pd.DataFrame(final_list, columns=['total','percentage'])
# sns.displot(graph_data, x="total", binwidth=1)

# sns.displot(graph_data, x="total", y='percentage')#, binwidth=1)
# graph_data = pd.DataFrame(result_list, columns=['total','percentage'])
# sns.histplot(data=graph_data, x="total", stat='probability', discrete=True)

# x = pd.DataFrame(get_pmf(2,8,0), columns=['total','percentage'])
# y = pd.DataFrame(get_pmf(4,4,0), columns=['total','percentage'])
# x['name'] = 'x'
# y['name'] = 'y'
# df = pd.concat([x, y], ignore_index=True)
# sns.histplot(data=df, x="total", stat='probability', discrete=True, hue='name', multiple='layer', alpha=0.5)

x = pd.DataFrame(get_pmf(3,6,0)[0], columns=['total'])
y = pd.DataFrame(get_pmf(2,6,4)[0], columns=['total'])
x['name'] = '3D6'
y['name'] = '2D6+4'
df = pd.concat([x, y], ignore_index=True)
sns.histplot(data=df, x="total", stat='probability', discrete=True, hue='name', multiple='layer', common_norm = False, alpha=0.5)
plt.show()
sns.histplot(data=df, x="total", stat='probability', discrete=True, hue='name', multiple='dodge', common_norm = False, alpha=0.5)
plt.show()
# sns.histplot(data=x, x="total", stat='probability', discrete=True, color='r', alpha=0.5)
# sns.histplot(data=y, x="total", stat='probability', discrete=True, color='b', alpha=0.5)



fig, axes = plt.subplots(2,1, sharey=True, sharex=True)
# fig.set_size_inches(10,10)
# fig.tight_layout()
sns.histplot(data=x, x="total", stat='probability', discrete=True, alpha=0.5, color = sns.color_palette()[0], ax=axes[0])
axes[0].set_title('3D6')
sns.histplot(data=y, x="total", stat='probability', discrete=True, alpha=0.5, color = sns.color_palette()[1], ax=axes[1])
axes[1].set_title('2D6+4')
plt.show()
# need to change to have ticks for every number, possibly shared gridlines would help too

# sns.barplot(x='total', y='percentage', data=x, alpha=0.5, color='r', ax=axes[0])
# sns.barplot(x='total', y='percentage', data=y, alpha=0.5, color='b', ax=axes[1])

get_pmf(3,6,0)[0]