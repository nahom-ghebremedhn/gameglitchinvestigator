

def get_range_for_difficulty(difficulty: str):   #FIX: Refactored logic into logic_utils.py using agent mode       
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":            #FIX: Fixed Hard range being easier than Normal
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str, low: int | None = None, high: int | None = None): #FIX: Refactored logic into logic_utils.py using agent mode
    """
    Parse user input into an int guess.

    If low and high are given, guesses outside [low, high] are rejected.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()       #FIX: Added whitespace stripping and out-of-range rejection using agent mode
    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret): #FIX: Refactored logic into logic_utils.py using agent mode
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:      #FIX: Swapped backwards hint messages (Too High -> Go LOWER) with AI help

            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int): #FIX: Refactored logic into logic_utils.py using agent mode
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # First-attempt win earns 100; each extra attempt costs 10 (min 10).   #FIX: Fixed win-points formula and made wrong guesses always cost 5 using agent mode
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # Any wrong guess costs the same, regardless of attempt parity. #FIX: Fixed win-points formula and made wrong guesses always cost 5
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
