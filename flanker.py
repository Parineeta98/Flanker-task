import matplotlib.pyplot as plt
import interactive_figure

def showfixation():
    '''just an addition function to show the fixation point before flank'''
    interactive_figure.clear()
    plt.xlim(35,65)
    plt.ylim(49,51)
    plt.xticks([])
    plt.yticks([]) 
    plt.plot(50, 50, marker='P', color='k', markersize=28, markerfacecolor='k')
    interactive_figure.draw()
    interactive_figure.wait(interval=0.5)
    interactive_figure.clear()

def flanker(target,type):
    """
    Generate visual stimuli for a flanker task.

    Parameters:
    - type: str, the type of flanker search ('con', 'incon', or 'neu').
    - target: str, the presence of the target ('tri' or 'sq').

    Returns:
    None (plots and displays the visual stimuli).
    """

    #input check
    if type not in {'con', 'incon', 'neu'}:
        raise ValueError("Invalid type input")
    if target not in {'tri', 'sq'}:
        raise ValueError("Invalid target type input")
    
    if type == 'con':
        if target == 'tri':
            #congruent condition, triangle target 
            # Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(47.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
        
        elif target == 'sq':
            #congruent condition, square target 
            # Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='s', color='k', markersize=28, markerfacecolor='k')
            plt.plot(47.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
    
    elif type == 'incon':
         if target == 'tri':
            #incongruent condition, triangle target 
            # Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='^', color='k', markersize=28, markerfacecolor='k')
            plt.plot(47.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

         elif target == 'sq':
            #incongruent condition, square target 
            # Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='s', color='k', markersize=28, markerfacecolor='k')
            plt.plot(47.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='^', color='k', markersize=28, markerfacecolor='k', linewidth=0)
    
    elif type == 'neu':
        if target == 'tri':
            #neutral condition, triangle target 
            # Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='^', color='k', markersize=28, markerfacecolor='k')
            plt.plot(47.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)

        elif target == 'sq':
            #neutral condition, square target 
            #Set explicit axis limits
            plt.xlim(35,65)
            plt.ylim(49,51)
            plt.xticks([])
            plt.yticks([]) 
            # Plotting symbols 
            plt.plot(50, 50, marker='s', color='k', markersize=28, markerfacecolor='k')
            plt.plot(47.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(45, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(42.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(52.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(55, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
            plt.plot(57.5, 50, marker='_', color='k', markersize=28, markerfacecolor='k', linewidth=0)
    
    #just for temporary function check, mute it for successive interative figure
    #plt.show()

#tested all combo of target+type here, works well!
#flanker('tri','con')

