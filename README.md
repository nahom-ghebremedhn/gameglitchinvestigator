# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Game Glitch Investigator is a number guessing game built with Streamlit. The app picks a secret number and you try to guess it. After each guess, a hint tells you to go higher or lower. Higher difficulty means a bigger range and more attempts, and you score more points for winning in fewer guesses.
- [x] The hints were backwards, and the secret was sometimes compared as text, so guesses were checked wrong. Hard mode was easier than Normal, invalid guesses used up attempts, and New Game didn't fully reset. Scoring was also inconsistent.
- [x] I corrected the hints and kept the secret as a number. I fixed the difficulty ranges, counted only valid guesses, and made New Game reset everything. I made scoring consistent and moved the game logic into logic_utils.py, where it's tested with pytest.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

The game starts on Normal difficulty: guess a number from 1 to 50 in 7 attempts. Open Developer Debug Info to see the secret number. In this example it is 37.

1. Guess 25. The hint says "Go HIGHER!" You have 6 attempts left and score is -5.
2. Guess 40. The hint says "Go LOWER!" You have 5 attempts left and score is -10.
3. Guess 35, then 37. The first hint says "Go HIGHER!" On 37 you win: balloons appear with "You won! The secret was 37. Final score: 55"
4. Typing abc or 60 shows an error and doesn't use up an attempt.
5. Click New Game 🔁, or change the difficulty in the sidebar, to get a new secret and reset your score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\bibia\OneDrive\Desktop\gameglitchinvestigator
plugins: anyio-4.15.1
collected 5 items

tests\test_game_logic.py .....                                           [100%]

============================== 5 passed in 0.07s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
