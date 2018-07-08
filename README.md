# Learning Python!!

### Installing Python:
Python 2.7 already comes with Macs. I ended up installing Python 3.7.

### Python2 vs Python3:
From a really basic understanding, Python2 has better support of libraries from the community since it has been around for longer. Python3 is newer and better supported, but there is less community library support.

### Setting up Python3

In order to use Python3, we have to always type in `python3` in the terminal to access it. Typing in `python` will default to the stock 2.7 installed on the mac.
In order to change this, we need to edit the bash profile:
`$ nano ~/.bash_profile` will show the file that has the path assignment that allows python to work. We can add a line:
`alias python=python3`
ctrl + x will close this prompt. From here on out, `python` will now use the newest python version.

### TDD and unittest

I spent around 20 minutes browsing through the official documentation for unittest. Due to the limited time I have, I decided to go onto youtube to see how to use unittest.

Using the files `test_calc.py` and `calc.py`, I followed [this video](https://www.youtube.com/watch?v=6tNS--WetLI&t=379s)to get a basic understanding of how it works. I've annotated over the `test_calc.py` file, taking notes that I can refer back to without re-watching the video.
