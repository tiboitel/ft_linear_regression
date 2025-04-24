
# 🛠️ ft_linear_regression — From Zero to 🚗 Price Hero

Welcome, ashen one. You've stumbled upon the *ft_linear_regression* project — the saga of one lonely Python script trying to predict used car prices based solely on how far they’ve been driven. No sci-fi libraries. No black-box sorcery. Just shadow math, madness, and mileage.

> "Life is meaningless, but a Peugeot with 240,000 km is worth precisely €3,650. That’s what your model tells me. The absurd never stood a chance."
— _Camus, if he’d survived and learned Python_

So if you ever looked at a rusty 200k-kilometer car and whispered, *"How much are you worth, really?"* — this one’s for you.

---

## 📦 Installation

Before you embark on this beautiful, soul-crushing journey, install the dependencies:

```bash
pip install -r requirements.txt
```
 
>   ***Pro tip**: Use a virtual environment. Otherwise your machine might file a lawsuit for dependency abuse.*

---

## 🚦 Quickstart

**Train the model:**
```python
python3 train.py
```

Sit back, relax, and watch your machine learn what life has already taught you — more mileage = less money.

**Make a prediction:**
```python
python3 predict.py
```

Type in a car’s mileage. Get an estimated price. Panic at how accurate it is.

**Visualize the magic:**
```python
    python3 plot.py
```
   See the data. See the line. Understand your own fate.

## 🧠 How It Works (The Non-Boring Way)
### 🧪 Step 1: Training the Model

In train.py, we make the model learn from the truth buried in a CSV of past car sales:

 - Normalize the mileage so your model doesn’t get intimidated by big
   numbers.
   
  - Start with a dumb guess (a flat line).
   
   - Slowly adjust that line by figuring out how wrong the guesses are and fixing them — step by painful step.
   
   - Save the learned formula into models/model.json.

No libraries. No mercy. Just raw numpy, pandas, and brain work.

### 🔮 Step 2: Making Predictions

In predict.py, you whisper your car’s mileage into the void, and the model speaks back — with a price.

 - Behind the scenes:
   
 -  It grabs the trained values.
   
  - Normalizes your input like a boss.
   
   - Applies the sacred formula it learned from the ancients (aka your
   training run).
   
   - Prints the predicted price with more confidence than your last
   relationship.

### 📊 Step 3: Plotting the Pain

In plot.py, we:

 - Plot your data points (every sad little car).
   
  - Draw the regression line (the oracle of used car value).
   
   - Make it look decent with labels and all that jazz.

Sit and admire the curve of capitalism.

### 🧾 File Structure
```
├── data/
│   └── data.csv          # The holy scripture of km and price
├── models/
│   └── model.json        # The saved wisdom of your AI monk
├── train.py              # The temple of learning
├── predict.py            # Ask your modern pythia
├── plot.py               # Visual art for your linear gradient descent regression
├── requirements.txt      # Dependencies. Blame them when it breaks
└── README.md             # You're here. Congrats!
```

## 🗿 Final Words

This project is proof that you don’t need TensorFlow to make machines think — just grit, sweat, and numpy (*optional but, no one like to normalize data and write standard deviation*).

So go ahead, predict some prices. Plot some lines. Break some hearts.

And remember:

>   "*The mileage may vary, but the good car is the one you love.*" - Captain Falcon

## 📝 License

Licensed under the Entropy of the Void. You can use, modify, and break this code however you want — just don’t blame me when it starts replying with existential questions. 

## 🧙 Author

[](https://github.com/tiboitel/ft_ping/blob/main/README.md#️-author)

Written by [tiboitel](https://github.com/tiboitel), Python sorcerer initiate learning forbidden ML magic. 

----------

If you enjoyed this, wait to see the day I tackle neural networks to see a new era of softened brains ready to devour themselves.

See you Space Cowboy 🤠 🚀

