# Pythonista-Scene-OpenGL-fire-demo
This is an experiment with OpenGL in Pythonista’s Scene module that renders a shifting color from orange to black on each particle over its lifetime. 

## Requirements
You will need the Pythonista app for iOS to use this code. The Scene module is specific to iOS devices. All the modules needed come with the app. 

I have encountered issues with certain Scene code on older devices so I can't confirm that it will work on your specific device. 

## Motivation
I was experimenting with particle effects and putting some object oriented code to good use by making a particle class.

The Scene module uses nodes to handle representing objects and graphics. Even the game scene itself is a node and all corresponding objects in a scene are nodes as well. There then a few subclasses of nodes, mainly SpriteNode and ShapeNode, which are used to create the game objects, each with their own specific properties attached like position, scale, etc. 

I wanted to create torches that used circles (or in this case an ellipse technically) for the fire/smoke particles that would then shrink, gradually turn black and fade.

In my naive implementation I simply updated all of these properties on each node but I was running into extremely slow output:
![IMB_kNoEZO](https://github.com/user-attachments/assets/563ce201-1a6f-43f3-95d7-3a792b40a195)

to be continued
