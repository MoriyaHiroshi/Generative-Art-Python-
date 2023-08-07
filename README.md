# Generative-Art-Python-
This program generates abstract art using the Python language.

For my program, I used the Pillow library and the random module. You can check out the documentation for Pillow here: https://pillow.readthedocs.io/en/stable/

I wanted my program to make a simple abstract artwork using lines of various colors. Here is a breakdown of the code that got the result.

Setting Up The Image

Before you start drawing, you need to create an image. This can be done by initialising a variable to Image.new().
Between the parentheses, you need to fill in 3 parameters. They are Mode, Size and Color.
For mode I chose RGB as I was familiar with it. I subsequently made the size of the image to be 500 x 500 and gave the image a background color of black.

Setting Up The Lines

In order to draw a line on the image, you would need to identify two points on the image. Since I wanted the lines to be random across the image, I created two random points using .randint() and placed them in a tuple to denote the x value and the y value. You would notice that there is a variable called padding_px that I have used. I created it so as to contain the lines within the boundaries of the image, this was a design choice on my part.

Overlay

This step is not exactly necessary as you can draw directly on the image you have initialised. But If you want to utilise an overlay to control the design of your artwork, this is how you can do it.
All you have to do is create a new variable and initialise it to Image.new(), remember to use the same set of parameters as the one you created earlier.

Drawing The Lines

Artwork produced from my code.


![example 1](https://github.com/MoriyaHiroshi/Generative-Art-Python-/assets/101780253/a8abf9a1-ac86-448e-8b41-da0cff0fc990)
![example 2](https://github.com/MoriyaHiroshi/Generative-Art-Python-/assets/101780253/452db4c8-6928-41f7-8c96-c7fe1438a07b)
![example 3](https://github.com/MoriyaHiroshi/Generative-Art-Python-/assets/101780253/d3a775db-c316-4e12-aac8-9662728c4741)
