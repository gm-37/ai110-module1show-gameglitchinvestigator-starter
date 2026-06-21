from logic_utils import check_guess

def test_winning_guess():
     # If the secret is 50 and guess is 50, it should be a win
     result = check_guess(50, 50)
     assert "Win" in result

def test_guess_too_high():
     # If secret is 50 and guess is 60, hint should be "Too High"
     result = check_guess(60, 50)
     assert "Too High" in result

def test_guess_too_low():
     # If secret is 50 and guess is 40, hint should be "Too Low"
     result = check_guess(40, 50)
     assert "Too Low" in result

def test_too_high_hint_says_go_lower():
    # Regression: a guess above the secret used to say "Go HIGHER" (wrong).
    # When the guess is too high, the player must aim LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    # Regression: a guess below the secret used to say "Go LOWER" (wrong).
    # When the guess is too low, the player must aim HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_correct_guess_wins():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
