# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
First time I ran the game, it was so messy and complicated to understand. It looked to have a lot of errors which some of them didn't even make sense. It made me confused when I first tried to play the game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  I noticed that the hints lied. It said go lower when you needed to go higher and vice versa. The second bug I noticed was that the difficulty levels were wrong. For example, Hard had a smaller range (1–50) than Normal (1–100), so Hard was actually easier.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 (secret above 50) | "Go HIGHER!" | "Go LOWER!" | None |
| abc | "That is not a number." and no attempt used | Error shown, but an attempt was used up | None |
| Switch difficulty to Hard | A wider range than Normal | Range was 1–50, smaller than Normal's 1–100 | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
## Replies to #2
- The AI found that the hint messages in check_guess were backwards: a guess that was too high told the player "Go HIGHER!" It suggested swapping them so "Too High" shows "Go LOWER!" and "Too Low" shows "Go HIGHER!". I checked it by running pytest (the tests for too-high and too-low guesses passed) and by playing the game. With the secret visible in the Developer Debug panel, I guessed above and below it, and the hints sent me the right way.
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

  Streamlit reruns the whole Python script whenever the user interacts with the app, like clicking a button. Session state lets the app remember information, such as a score or user input, between those reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to reuse the habit of doing things one at a time. The CodePath approach of checking off each step once you're done with it really helped me keep track of what I was doing.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would rely less on AI-generated code. Even though I was able to identify most bugs, there were a few that only the AI found. Next time I want to find more bugs on my own.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I used to think AI-generated code was perfect with no bugs. However now I am able to see that AI also needs humans to function properly.
