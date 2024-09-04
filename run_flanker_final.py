import matplotlib.pyplot as plt
import numpy as np
import random 
import time
import interactive_figure 
import flanker
from PyQt5.QtWidgets import QApplication, QInputDialog

def main():
    """the main function to run practice trials, the main Flanker task, and data collection"""
    participant_number = get_participant_number() #to get participant IDs
    interactive_figure.create()
    interactive_figure.fullscreen()
    practice_loop() #to run practice trials
    run_experiment(participant_number) #to run main experiment
    end_text = "Great! \n You have finished the Flanker task!"
    show_feedback(end_text) #to mark end of experiment
    interactive_figure.close()

def get_participant_number():
    '''to create participant IDs'''
    app = QApplication([])
    participant_number, ok = QInputDialog.getInt(None, "Input", "Enter participant number:")
    app.quit()
    return participant_number if ok else None

def rand_target():
    '''randomize the input of flanker target'''
    given_target = ['tri','sq']
    random_target = random.choice(given_target)
    return random_target

def rand_type():
    '''randomize the input of flanker type'''
    given_type = ['con','incon','neu']
    random_type = random.choice(given_type)
    return random_type

# for practice trials' flanker input, to make sure that every combination is presented twice
def check_practice_counter(target,type,practice_counters):
    '''this function is to check if the counter for specific target-type combination has reached 2 in practice tests,
    input: 
    target and type are randomly chosen according to rand_ functions,
    practice_counters is the list of counters for each combination during practice '''
    target_index = ['tri','sq'].index(target)
    type_index = ['con', 'incon', 'neu'].index(type)
    #The .index(): find the index of the first occurrence of a value in a list. 
    if practice_counters[target_index, type_index] < 2: #if this combination has not yet appeared twice
        return True # Combination is valid and can be presented
    else:
        return False # Combination has reached the limit, skip it
    
# for flanker's input generation, to make sure every task-symbol combination is shown 20 times
def check_counter(target,type,counters):
    '''this function is to check if the counter for specific target-type combination has reached 20 in flanker task,
    and then to stop generating this combination after 20 trials
    input: 
    target and type are randomly chosen by according rand_ functions thus no input checks added here,
    counters is the list of counters for each combination (2X3) during the actual task '''
    target_index = ['tri','sq'].index(target)
    type_index = ['con', 'incon', 'neu'].index(type)
    #The .index(): find the index of the first occurrence of a value in a list. 
    if counters[target_index, type_index] < 20: #if this combination has not yet received 20 valid responses
        return True # Combination is valid and can be presented
    else:
        return False # Combination has reached the limit, skip it

def show_feedback(feedback_text):
    '''this function is to present a feedback text (string) depending on the context and subject's response'''
    interactive_figure.clear()
    plt.xlim(35,65)
    plt.ylim(49,51)
    plt.xticks([])
    plt.yticks([]) 
    plt.text(50, 50, feedback_text, ha='center', va='center', fontsize = 24)
    interactive_figure.draw()
    interactive_figure.wait_for_interaction()

def show_interval():
    '''this function is to present a blank screen interval between trials'''
    interactive_figure.clear()
    plt.xlim(35,65)
    plt.ylim(49,51)
    plt.xticks([])
    plt.yticks([]) 
    interactive_figure.draw()
    interactive_figure.wait(interval=1)

def is_valid_keypress(key):
    '''this is a input-check function to make sure the key press is only what we asked for: a and l'''
    if key in {'a','l'}:
        return True
    else:
        return False 

def is_correct(target, key):
    """Checks whether the pressed key corresponds to the stimulus:
    'a' for target triangle, 'l' for target sqaure
    inputs are actually being checked in this function"""
    if (target == 'tri' and key == 'a') or (target == 'sq' and key == 'l'):
        return True
    else:
        return False

# a function to save trial data to a CSV file, based on Julia example code:
def save_data(participant_num, trial_num, targets, types, key, RT, accuracy):
    """Saves the data of a visual search task to csv
    these inputs are all data from each trial, and they are all lists so input check is not so useful here"""

    combined_data = [participant_num, trial_num, targets, types, key, RT, accuracy] # list of lists/nested list
    combined_data = list(map(list, zip(*combined_data))) # transposes data (so that there is one var per column)
    
    filename = f"flanker_participant_{participant_num[0]}.csv"
    
    # Save the list to a CSV file
    np.savetxt(filename, combined_data, delimiter=',', fmt='%s', header='participant_number, trial_number, target, type, key, reaction_time, accuracy', comments='')

def practice_trials():
    '''a demo of one practice program, runs 12 trials in total
    output the number of correct trials out of the 12 trials'''
    # create the layout
    interactive_figure.clear()
    plt.xlim(35,65)
    plt.ylim(49,51)
    plt.xticks([])
    plt.yticks([]) 

    # welcome texts
    welcome_text = 'Thank you for taking the Flanker task! \n \n Before starting: \n Position yourself at arms length from the monitor \n and try to maintain this viewing distance throughout the experiment \n \n Press any key to start practice trials.' 
    show_feedback(welcome_text)

    # show instructions
    instruction_text = "The objective of the Flanker task is to focus on \n the shape displayed in the middle of the screen. \n \n A black cross is presented before each trial for fixation, \n please stare at the center of the screen throughout the task.\n \n If the shape is a triangle, press key 'A'. \n If the shape is a square, press key 'L'. \n \n You will now do some practice trials to get familiar with the task!\n Press any key to continue."
    show_feedback(instruction_text)

    # ready to start practice
    start_practice_text = "Practice trials start! \n Press any key to continue."
    show_feedback(start_practice_text)
    interactive_figure.clear()

    # start practice trials
    # a small counters' list for practice: we decide to show each combination twice, so 12 trials in total (the condition to pass practice is to have 9 correct trials out of 12 total trials, see in practice_loop)
    practice_trial_num=0
    practice_counters = np.zeros((2,3),dtype=int)
    correct_num = 0

    while practice_trial_num < 12: # when not all trials are done, repeat the loop
        
        # randomize the stimuli type
        target = rand_target()
        type = rand_type()

        # if show all combinations twice, end of practice
        if all(counter == 2 for counter in practice_counters.flatten()):
            break

        # if haven't shown all combinations twice, keep on presenting, increment in the counter and total trial number
        if check_practice_counter(target, type, practice_counters):
            target_index = ['tri', 'sq'].index(target)
            type_index = ['con', 'incon', 'neu'].index(type)
            practice_counters[target_index, type_index] += 1
            practice_trial_num += 1

            # show fixation for 0.5s
            flanker.showfixation()

            # show flanker stimulus for 2.5s
            flanker.flanker(target, type)
            interactive_figure.wait_for_interaction(interval=2.5)
            last_keypress = interactive_figure.last_keypress
            # show blank screen for 1s
            show_interval()

            # only add 1 when the reponse in made within 2.5s and response correct
            if is_correct(target, last_keypress):
                correct_num += 1
            # otherwise the correct_num stays the same
            else:
               correct_num += 0
            interactive_figure.clear()
        else:
            continue
    return correct_num

def practice_loop():
    '''this is a loop of practice trials, with the condition of 75% accuracy to stop the loop'''
    correct_trial_num= practice_trials()
    while correct_trial_num < 9:
        #accuracy too low: show negative feedback, try again
        negative_feedback_text = "Sorry! Maybe you did not understand the instructions.\n Let’s go back to the start again.\n This time please read the instructions carefully. \n Make sure you understand what you’re asked to do in this task. \n Don’t be defeated! This is just a practice. Let’s try again!"
        show_feedback(negative_feedback_text)
        # repeat the practice
        correct_trial_num = practice_trials()
    #pass the practice test: show good job 
    positive_feedback_text1 = "Great! You got it right! \n  \n When the target was triangle, the correct response was: A. \n When the target was sqaure, the correct response was: L."
    show_feedback(positive_feedback_text1)
    #show end of practice
    positive_feedback_text2 = "End of practice! \n Start the task when you're ready. "
    show_feedback(positive_feedback_text2)
    interactive_figure.clear()
            
def run_experiment(participant_number):
    """Run our experiment."""
    """this is the actual flanker task program: to present the stimuli multiple times throughout the test
    until the 'end condition' is met: 20 trials for all target + type combinations
    meanwhile collect data for each trial, and store them in a csv file
    input: participant number (int)
    output: a whole data file containing all info from each trial in the task:
    participant #, trial #, target type, condition type, reaction time, accuracy"""

    # total trial number counter (needs to be reset as 0 once it reaches 60, take a rest):
    trial_number = 0

    # counters for trials of different combinations (limit is 20):
    # Initialize counters for each combination of target and type
    # Using a 2D list to represent counters
    # Each row corresponds to a target, and each column corresponds to a type
    # updated after trials and checked by a 'check_counter' function to exclude 20-trial combination
    counters = np.zeros((2,3),dtype=int)

    # Create the layout for this figure.
    plt.xlim(35,65)
    plt.ylim(49,51)
    plt.xticks([])
    plt.yticks([]) 

    # Display the starting text at the center of the figure
    start_text = "Press any key to start the task!"
    show_feedback(start_text)

    # Clear the figure.
    interactive_figure.clear()

    # Create lists to note the parameters of each trial, to store data
    participant_num = []
    trial_num =[]
    types =[]
    targets = []
    key =[]
    RT =[]
    accuracy=[]

    # Main loop for the experiment
    while trial_number < 60: # 60 is the limit where subjects are suggested to rest, repeat until all counters reach 20
        # randomize the stimulus type
        target = rand_target()
        type = rand_type()

        # if show all combinations are shown 20 times -> end of task
        if all(counter == 20 for counter in counters.flatten()):
            break

        if check_counter(target, type, counters): # if not 20 for each counter yet, keep showing stimulus -> continue experiment

            # part1: present stimulus
            # show fixation for 0.5s
            flanker.showfixation()

            # show flanker stimulus for 2.5s, record time and key
            flanker.flanker(target, type)
            start_time = time.time()
            interactive_figure.wait_for_interaction(interval=2.5)
            end_time = time.time()
            last_keypress = interactive_figure.last_keypress

            # show blank screen interval for 1s
            show_interval()

            # part2: counter increment, record and store data
            # if response is made within the limit of 2.5s
            if last_keypress is not None:
                #record the RT
                reaction_time = end_time - start_time
                
                # if the keypress is invalid, not 'A' or 'L', this trial does not count
                if not is_valid_keypress(last_keypress):
                    reaction_time = -1
                    correctness = -1
                
                # if the keypress is vaild, increment in the according counter
                else:
                    if is_correct(target, last_keypress):
                        target_index = ['tri', 'sq'].index(target)
                        type_index = ['con', 'incon', 'neu'].index(type)
                        counters[target_index, type_index] += 1
                        correctness = 1
                    else:
                        target_index = ['tri', 'sq'].index(target)
                        type_index = ['con', 'incon', 'neu'].index(type)
                        counters[target_index, type_index] += 1
                        correctness = 0
            
            # if no response is made within 2.5s, do not count this trial
            else:
               # The case where the timeout occurred
               reaction_time = -1
               correctness = -1
            
            interactive_figure.clear()
            trial_number += 1

            # add values to the lists for later data storage in csv file
            
            participant_num.append(participant_number)
            trial_num.append(trial_number)
            targets.append(target)
            types.append(type)
            targets.append(target)
            key.append(last_keypress)
            RT.append(reaction_time)
            accuracy.append(correctness)

            # when total trial number reaches 60, take a break
            if trial_number % 60 == 0:
               # show break text
               rest_text = "Brilliant! 60 Trials are done!\n Take a rest as long as you want. \n When you're ready, press any key to continue the test."
               show_feedback(rest_text)
               # change the trial number to restart the loop for flanker task
               trial_number = 0
            interactive_figure.clear()

        else:
          continue
        
        # Save trial data to a CSV file  
        save_data(participant_num, trial_num, targets, types, key, RT, accuracy)

if __name__ == "__main__":
    main()

