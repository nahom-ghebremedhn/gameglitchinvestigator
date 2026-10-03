# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
## Replies to #2
- The AI found that the hint messages in check_guess were backwards: a guess that was too high told the player "Go HIGHER!" It suggested swapping them so "Too High" shows "📉 Go LOWER!" and "Too Low" shows "📈 Go HIGHER!". I checked it by running pytest (the tests for too-high and too-low guesses passed) and by playing the game. With the secret visible in the Developer Debug panel, I guessed above and below it, and the hints sent me the right way.
- The AI suggested fixing the difficulty ranges by setting Normal to 1–100 and Hard to 1–200. I changed this to Normal 1–50 and Hard 1–100. Easy is only 1–20 and the attempt limits are close together (6/7/8), so jumping from 1–20 to 1–100 would have made Normal much harder than Easy. My ranges make each level a little harder than the one before. I checked my version by updating the tests for get_range_for_difficulty and running pytest. I also switched difficulties in the app and confirmed the "Guess a number between…" message and the secret in the debug panel used the new ranges.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

    I counted a bug as fixed only when two things were true: the pytest tests passed, and the game behaved correctly when I played it in Streamlit. While playing, I opened the Developer Debug Info panel to see the secret number, so I could check every hint, attempt count and score against it.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

    I ran pytest with test_too_high_guess_tells_player_to_go_lower and test_too_low_guess_tells_player_to_go_higher. They check both the outcome ("Too High"/"Too Low") and the hint message. Before the fix, the message part failed, which showed that the outcome was right but the hint pointed the wrong way. After I swapped the messages, all 5 tests passed.

- Did AI help you design or understand any tests? How?

    Yes. The AI pointed out that the original tests only checked the outcome, not the message, so they couldn't catch the backwards hints. It helped me write the two new tests that check the message too. It also explained that check_guess returns a pair (outcome, message), so a test has to check both parts.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
