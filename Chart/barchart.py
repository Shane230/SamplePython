import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML


values = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(values))
performance = [100, 80, 60, 40, 20, 10]
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, values)


plt.savefig('c://Python_Lessons//chart3.png')

graphs = ['c://Python_Lessons//chart3.png']

template = (''
    '<a href="{graph_url}" target="_blank">' 
        '<img src="{graph_url}.png">'        
    '</a>'
    '{caption}'                              
    '<br>'                                   
    '<a href="{graph_url}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">'
        'Click to comment and see the interactive graph'  
    '</a>'
    '<br>'
    '<hr>'                                   
'')

email_body = ''
for graph in graphs:
    _ = template
    _ = _.format(graph_url=graph, caption='')
    email_body += _

display(HTML(email_body))

