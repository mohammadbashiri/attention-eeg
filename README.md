<h1 align="center"> AttentionEEG </h1>

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
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/stim1.png" alt="Fig1">
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
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/stim_all.png" alt="Fig1">
</p>

Below is an example of one complete sitmulus, including the timing information.

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/stim2.png" alt="Fig1">
</p>



## Electrophysiological Recording

Device:... .
Channels: Fp1, Fp2, F7, F3, Fz, F4, F8, FC5, FC1, FC2, FC6, T7, C3, Cz, C4, T8, CP5, CP1, CP2, CP6, P7, P3, Pz, P4, P8, O1, O2.
EOG: below left eye (horizontal EOG) and between two eyebrows (vertical EOG).
Electrode impedance were kept below 5 k\Omega.
Signal was bandpass filtered with cut-off frquencies of 1 and 20 Hz.
Sampling rate was 1000 Hz.
reference:... , and a ground was located on the forehead (Fpz position).
Offline averaging was performed by extracting overlapping epochs of the EEG beginning 200 ms before the first stimulus of each pair
and continuing for 800 ms poststimulus.
Signal rejection/correction was performed before averaging.
Trials with incorrect response (false alarms and misses) were excluded from analysis.



## Preliminary Results

### Motion attention effect (with color)

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/MotionColorFig.PNG" alt="Fig1">
</p>

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/MotionColorChanMeanFig.PNG" alt="Fig1">
</p>

### Motion attention effect (with shape)

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/MotionShapeFig.PNG" alt="Fig1">
</p>

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/MotionShapeChanMeanFig.PNG" alt="Fig1">
</p>

### Color attention effect

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/ColorFig.PNG" alt="Fig1">
</p>

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/ColorChanMeanFig.PNG" alt="Fig1">
</p>


### Shape attention effect

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/ShapeFig.PNG" alt="Fig1">
</p>

<p align="center">
	<br>
	<img src="https://github.com/mohammadbashiri93/AttentionEEG/blob/master/Fig/ShapeChanMeanFig.PNG" alt="Fig1">
</p>

## Installation procedure for PsychoPy and ratCAVE

1. 


psychopy keylist:
'return' (NOT 'enter')