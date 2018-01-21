# AttentionEEG

## :page_with_curl: Expeirment Description 

This is an attention-related experiment in which you are required to respond when you have detected a stimulus with 
specific features. There are two objects in this experiment (i.e., circle and square), that could appear with two different 
color (i.e., red and blue). <br/>
This experiment involves 20 blocks, each containing 50 stimuli. In each stimulus, you would see two flashes. In the first 
flash, a specific shape appears with a specific color. In the second flash, the object moves either to left or to right. 
Thus, as you can imagine, the object has a spatial feature (movement to left or right) and two semantic feature (shape and color)
In the beginning of each block, you would be asked to attend to specific movement (either left or right) and a specific semantic 
feature (either shape or color). For instance, if you are asked to attend to shape, and attend to circle going to left; you would 
only care about circles that moved to left (w.r.t to first flash). Note that in this case you are only asked about the shape, hence, 
you should ignore the color and ONLY attend to shape. On the other hand, if you are asked about color, you should ignore shape.

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/dev/Fig/stim1.png" alt="Fig1">
</p>

Within the attended feature (specific movement and specific color/shape), there are two variants (Standard and Target). 
These two differ in the timing between the two flashes. The so-called Standard stimuli have shorter time between the two
flashes (50 ms), and the Target stimuli has a longer time (150 ms). You are always required to press the SPACE button when 
you detect a ***Target*** stimulus.

As an example, you would be asked in the beginning of the block to “attend to color, blue to right”. Then, you be presented 
with 50 stimuli. Within these 50 stimuli, you would, once a while, observe a blue object that moves to the right.  However, 
some of them have a shorter time between two flashes (standard stimulus), and some of them longer (target stimulus). You are 
supposed to press SPACE only when you detect the longer one. To make sure you have understood this concept, before stating the 
experiment we would go through 5 minutes of training.

The figure below illustrates the four possible stimuli (square/circle and red/blue) with two example of each trial mode (i.e.,
motion-shape and motion-color).

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/dev/Fig/stim_all.png" alt="Fig1">
</p>

Below is an example of one complete sitmulus, including the timing information.

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/dev/Fig/stim2.png" alt="Fig1">
</p>


## Installation procedure for PsychoPy and ratCAVE

1. 


psychopy keylist:
'return' (NOT 'enter')