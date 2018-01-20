from psychopy import visual, core, event, parallel, monitors  # import some libraries from PsychoPy
from experiment import Experiment, DataLogger
import numpy as np


# initialize parallel port
port = parallel.ParallelPort(0xDC00)

# exp and subject spcecifications
subject_name = 'Abdallah'
session_no = '01'
no_of_blocks = 10
no_of_trials = 4  # per block
block_counter = 0

# initialize a DataLogger object
data_logger = DataLogger(subject_name=subject_name, session_no=session_no, no_of_blocks=no_of_blocks, no_of_trials=no_of_trials)

# create a window
mywin = visual.Window((1920, 1200), screen=1, monitor="testMonitor", units="deg",color=(.9, .9, .9))

for blocks in range(no_of_blocks):

    if block_counter % 2 == 0:
        exp = Experiment(win=mywin, trials_no=no_of_trials, mode='motion-shape')
    else:
        exp = Experiment(win=mywin, trials_no=no_of_trials, mode='motion-color')

    # randomize shapes and left and right movements with having a fixed number  of left and rights
    # shape
    flash1_shape = exp.randomize2val(0, 1).astype(int)  # 1: circle, 0: square
    flash2_shape = exp.randomize2val(0, 1).astype(int)  # 1: circle, 0: square

    # left/right
    shift_val = 2.5
    lr = exp.randomize2val(shift_val, -shift_val)

    # color
    flash1_color = exp.randomize2str('red', 'blue')
    flash2_color = exp.randomize2str('red', 'blue')

    # type
    prob_target = .25
    prob_std = .75
    stim_type = exp.randomize2type(3, prob_std, 9, prob_target)  # delay (frames), probability, delay (frames), probability

    # get randomized target value, depending on the experiment mode
    feature1, feature2 = exp.getRandAttendedFeature(('red', 'blue'), (0, 1), (shift_val, -shift_val))

    if feature1 == 'red' or feature1 == 'blue':
        feature1Text = feature1
    elif feature1 == 0:
        feature1Text = 'square'
    elif feature1 == 1:
        feature1Text = 'circle'

    if feature2 == -2.5:
        feature2Text = 'left'
    else:
        feature2Text = 'right'
    space = " "
    attended_feature_text = (feature1Text, 'to', feature2Text)
    attended_feature_text_joined = space.join(attended_feature_text)


    # log the information for this trial
    data_logger.update(block_counter, exp.mode, flash1_shape, flash2_shape, flash1_color, flash2_color, lr, stim_type,
                           feature1, feature2)

    print('blocks left:', no_of_blocks-block_counter, attended_feature_text_joined)
    # print(str(feature1), feature1Text, str(feature2), feature2Text, attended_feature_text_joined)


    # welcoming message and introduction
    if block_counter == 0:
        exp.welcome_msg1.draw()
        exp.welcome_msg2.draw()
        exp.welcome_msg3.draw()
        exp.welcome_msg4.draw()
        exp.welcome_msg5.draw()
        mywin.flip()
        event.waitKeys(keyList='right')  # wait for subject to press right arrow key
        event.clearEvents()

    # display the instructions
    exp.instruct1_msg.draw()
    exp.attended_feature.setText(attended_feature_text_joined)
    exp.attended_feature.pos = (0, -1.5)
    exp.attended_feature.bold = True
    exp.attended_feature.draw()
    mywin.flip()

    # press right arrow key to continue
    event.waitKeys(keyList='right')

    # marker - block start (after the subject decided to proceed)
    port.setData(exp.block_start)

    # wait for 2 seconds for subject get ready and then start
    for frame in range(120):
        exp.fixat.draw()
        mywin.flip()

    # start of the trial
    for trial in range(exp.trials_no):

        # randomization takes effect here
        obj_disp = exp.getrand_obj(flash1_shape[trial])
        mv_shift = (lr[trial], 0)  # 0 because the change is only in x direction

        # Set the initial condition (we can have a res et function/method here)
        obj_disp.pos = exp.getrand_pos()
        position = obj_disp.pos
        obj_disp.fillColor = flash1_color[trial]

        # marker - flash1
        port.setData(exp.flash1_start_Non)

        # flash 1 (duration = 33ms)
        for frame in range(2):
            exp.fixat.draw()
            obj_disp.draw()
            mywin.flip()
            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)

        for frame in range(stim_type[trial]):  # SOA
            exp.fixat.draw()
            mywin.flip()
            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)

        # Implement the changes between two flashes
        if exp.mode == 'motion-color':
            obj_disp = exp.getrand_obj(flash2_shape[trial])
            obj_disp.fillColor = flash1_color[trial]  # color must stay the same

        else:
            obj_disp = exp.getrand_obj(flash1_shape[trial])  # object must stay the same
            obj_disp.fillColor = flash2_color[trial]  # color should change

        # shift is always there
        obj_disp.pos = position
        obj_disp.pos += mv_shift

        # marker - flash 2
        port.setData(exp.flash2_start)

        if event.getKeys(keyList='space'):
            print('SPACE was pressed!')
            port.setData(exp.response_marker)

        # flash 2 (duration = 33ms)
        for frame in range(2):
            exp.fixat.draw()
            obj_disp.draw()
            mywin.flip()
            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)


        for frame in range(np.random.randint(15, 45)):  # ITI
            exp.fixat.draw()
            mywin.flip()
            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)

        if event.getKeys(keyList='space'):
            print('SPACE was pressed!')
            port.setData(exp.response_marker)

    event.clearEvents()

    block_counter += 1
    if block_counter == no_of_blocks:
        exp.closing_msg.draw()
        mywin.flip()
        event.waitKeys(keyList='right')  # press right arrow key to exit

# save logged data
filepath = '../../datalog/'
data_logger.save(filepath=filepath)

# cleanup
mywin.close()
core.quit()

