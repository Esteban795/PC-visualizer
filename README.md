# PC-visualizer
Repository to visualize your Pass Culture sales with matplotlib.

## What does it do ? 
It takes a CSV file (named `data.csv`) which you can download from the official Pass Culture's website, and displays the sales information it can find in here, such as 
- the total amount of money generated 
- how many sales for each offer. For example, if you hold exhibition, you can have different prices according to some rules you choose. This will automatically sort the reservations by theses prices and display the repartition (so you can get some feedback on which offer seems to work the best !)

## Requirements 
- A Python interpreter : I used 3.10.12
- Matplotlib : I used 3.9.2
- Pandas : I used 2.2.2

You can get them easily using 
```
pip install -r requirements.txt
```

## How to install it on your computer ? 

Just clone the repo on your computer using 
```
git clone https://github.com/Esteban795/PC-visualizer.git
``` 

Or download it directly, doesn't matter.

## How to run it ? 

Head inside the directory, download your CSV from Pass Culture's website and place it inside PC-visualizer, where the `main.py` file is.
Then just run the python file, using 
```
python3 main.py
``` 
or use the arrow in VSC.

## Open an issue if you can't make it run for any reason !