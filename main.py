from art import logo, vs
from game_data import data
import random
import json
import logging
from pathlib import Path
from typing import Dict, Tuple, List, Optional


Account = Dict[str, object]


def get_random_account(exclude: Optional[Account] = None) -> Account:
  """Return a random account distinct from exclude (if provided)."""
  account = random.choice(data)
  while exclude and account == exclude:
    account = random.choice(data)
  return account


def format_account(tag: str, account: Account) -> str:
  """Human-readable line for an account comparison."""
  return f"{tag}: {account['name']}, a {account['description']} from {account['country']}"


def validate_data() -> None:
  if not isinstance(data, list) or not data:
    raise ValueError("Data list is empty or not a list")
  required = {"name", "follower_count", "description", "country"}
  for idx, entry in enumerate(data):
    if not required.issubset(entry.keys()):
      missing = required - set(entry.keys())
      raise KeyError(f"Data entry {idx} missing keys: {missing}")
    if not isinstance(entry['follower_count'], (int, float)):
      raise TypeError(f"Follower count for entry {idx} is not numeric")


HIGH_SCORE_FILE = Path(".highscore.json")


def load_high_score(path: Path = HIGH_SCORE_FILE) -> int:
  if not path.exists():
    logging.debug("High score file does not exist; returning 0")
    return 0
  try:
    with path.open("r", encoding="utf-8") as f:
      data_obj = json.load(f)
    hs = int(data_obj.get("high_score", 0))
    logging.debug("Loaded high score %s", hs)
    return hs
  except Exception as e:
    logging.warning("Failed to load high score (%s); resetting to 0", e)
    return 0


def save_high_score(score: int, path: Path = HIGH_SCORE_FILE) -> None:
  try:
    with path.open("w", encoding="utf-8") as f:
      json.dump({"high_score": score}, f)
    logging.debug("Saved high score %s", score)
  except Exception as e:
    logging.error("Failed to save high score %s (%s)", score, e)


def compare_followers(account_a: Account, account_b: Account, choice: str) -> Tuple[bool, bool, bool, bool]:
  """Evaluate user's choice.

  Returns (is_correct, auto_advance, picked_a, tie).
  - is_correct: was the user's selection correct (ties count as correct)
  - auto_advance: True if tie triggered automatic advancement
  - picked_a: True if user chose A
  - tie: True if follower counts were equal
  """
  picked_a = (choice == 'a')
  a_followers = account_a['follower_count']
  b_followers = account_b['follower_count']
  if a_followers == b_followers:
    return True, True, picked_a, True
  if picked_a:
    return a_followers > b_followers, False, True, False
  return b_followers > a_followers, False, False, False


def play_round() -> Tuple[int, List[Tuple[str, str]]]:
  score: int = 0
  history: List[Tuple[str, str]] = []  # (account_a_name, account_b_name)
  account_a: Account = get_random_account()
  account_b: Account = get_random_account(exclude=account_a)

  while True:
    print(format_account("Compare A", account_a))
    print(vs)
    print(format_account("Against B", account_b))

    history.append((account_a['name'], account_b['name']))
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

    if choice not in {"a", "b"}:
      print("Invalid input. Round ended.")
      break

    is_correct, auto_advance, picked_a, tie = compare_followers(account_a, account_b, choice)
    if not is_correct:
      print(f"You lost. Final score: {score}.")
      break
    score += 1
    if tie:
      print(f"Tie on follower count. Auto-correct! Score: {score}.")
    else:
      print(f"You're right! Current score: {score}.")
    if picked_a:
      account_b = get_random_account(exclude=account_a)
    else:
      account_a = account_b
      account_b = get_random_account(exclude=account_a)

  return score, history


def play() -> None:
  print(logo)
  high_score: int = load_high_score()
  all_history: List[List[Tuple[str, str]]] = []  # aggregate history across rounds

  while True:
    score, history = play_round()
    if score > high_score:
      high_score = score
      save_high_score(high_score)
      logging.info("New high score: %s", high_score)
    all_history.append(history)
    print(f"Round complete. Score: {score}. High score: {high_score}.")
    show_hist = input("Show this round's account pairs? (y/n): ").strip().lower()
    if show_hist == 'y':
      for i, (a_name, b_name) in enumerate(history, start=1):
        print(f" {i}. A={a_name} vs B={b_name}")
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
      print("Thanks for playing!")
      break


if __name__ == "__main__":
  try:
    logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s %(levelname)s %(message)s",
      handlers=[
        logging.FileHandler("game.log"),
        logging.StreamHandler()
      ]
    )
    validate_data()
    play()
  except (KeyboardInterrupt, EOFError):
    print("\nSession interrupted. Goodbye.")
  except Exception as e:
    print(f"Startup error: {e}")
