"""Core Mad-Libs engine: turns prayer text into a template with blanks,
picks a word-type category per blank, and renders the finished prayer
once players have supplied their words.

Blank-worthy words are looked up in prayer_tags.WORD_TAGS, a hand-verified
part-of-speech tag per word (see that module's docstring for why: a runtime
suffix-guessing heuristic reliably mislabels irregular verbs/adjectives,
producing blanks that are ungrammatical even when answered correctly).
"""
from __future__ import annotations

import random
import re
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum

from .prayer_tags import WORD_TAGS
from .prayers_data import Prayer

_TOKEN_RE = re.compile(r"[A-Za-z']+|[^A-Za-z']+")


class Category(Enum):
    NOUN = ("noun", "Give me a noun")
    PLURAL_NOUN = ("plural noun", "Give me a plural noun")
    VERB = ("verb", "Give me a verb")
    VERB_PAST = ("verb (past tense)", "Give me a verb (past tense)")
    VERB_ING = ("verb ending in -ing", "Give me a verb ending in -ing")
    ADJECTIVE = ("adjective", "Give me an adjective")
    ADVERB = ("adverb", "Give me an adverb (a word ending in -ly)")
    NUMBER = ("number", "Give me a number")
    CELEBRITY = ("celebrity", "Name a celebrity")
    EXCLAMATION = ("exclamation", "Give me an exclamation")
    BODY_PART = ("body part", "Name a part of the body")
    SIN = ("a sin", "Name a sin (lol)")
    ANIMAL = ("animal", "Name an animal")
    COLOR = ("color", "Name a color")
    PLACE = ("place", "Name a place")
    EMOTION = ("emotion", "Name an emotion")

    def __init__(self, label: str, prompt: str) -> None:
        self.label = label
        self.prompt = prompt


# Every category in a bucket's pool is grammatically interchangeable with the
# original word -- they only vary in comedic "flavor" (a body part is still
# a noun; a celebrity is still a noun), so any of them keeps the sentence
# grammatical as long as the *bucket* (noun/verb/adjective/...) is right.
_BUCKET_CATEGORIES: dict[str, list[Category]] = {
    "N": [
        Category.NOUN,
        Category.NOUN,
        Category.CELEBRITY,
        Category.BODY_PART,
        Category.SIN,
        Category.ANIMAL,
        Category.COLOR,
        Category.PLACE,
        Category.EMOTION,
    ],
    "NP": [Category.PLURAL_NOUN],
    "V": [Category.VERB],
    "VD": [Category.VERB_PAST],
    "VG": [Category.VERB_ING],
    "ADJ": [Category.ADJECTIVE, Category.COLOR],
    "ADV": [Category.ADVERB],
    "NUM": [Category.NUMBER],
    "EXCL": [Category.EXCLAMATION],
}


@dataclass
class Blank:
    index: int
    category: Category
    original_word: str
    answer: str | None = None
    answered_by: str | None = None


@dataclass
class MadLib:
    prayer: Prayer
    tokens: list[str]
    blanks: dict[int, Blank] = field(default_factory=dict)

    @property
    def blank_order(self) -> list[int]:
        return sorted(self.blanks)

    @property
    def total_blanks(self) -> int:
        return len(self.blanks)

    def is_complete(self) -> bool:
        return all(b.answer is not None for b in self.blanks.values())

    def set_answer(self, blank_index: int, text: str, answered_by: str | None = None) -> None:
        blank = self.blanks[blank_index]
        blank.answer = text.strip() or "..."
        blank.answered_by = answered_by

    def render(self, reveal_unanswered: bool = False) -> str:
        """Rebuild the prayer text, substituting answers for blanked words."""
        out: list[str] = []
        for i, tok in enumerate(self.tokens):
            blank = self.blanks.get(i)
            if blank is None:
                out.append(tok)
            elif blank.answer is not None:
                out.append(blank.answer)
            elif reveal_unanswered:
                out.append(f"[{blank.category.label}]")
            else:
                out.append("_" * max(4, len(blank.original_word)))
        return "".join(out)

    def render_rich(self) -> str:
        """Like render(), but wraps filled answers in Rich markup for styling."""
        out: list[str] = []
        for i, tok in enumerate(self.tokens):
            blank = self.blanks.get(i)
            if blank is None:
                out.append(tok)
            elif blank.answer is not None:
                out.append(f"[bold gold3]{blank.answer}[/bold gold3]")
            else:
                placeholder = "_" * max(4, len(blank.original_word))
                out.append(f"[dim]{placeholder}[/dim]")
        return "".join(out)


def _candidate_buckets(prayer: Prayer, tokens: list[str]) -> dict[int, str]:
    """Map token index -> POS bucket for every tagged, blankable word."""
    tags = WORD_TAGS.get(prayer.id, {})
    seen: Counter[str] = Counter()
    buckets: dict[int, str] = {}
    for i, tok in enumerate(tokens):
        if not tok[0].isalpha():
            continue
        key = tok.lower().strip("'")
        tag = tags.get(key)
        if tag is None:
            continue
        if isinstance(tag, list):
            occurrence = seen[key]
            seen[key] += 1
            bucket = tag[min(occurrence, len(tag) - 1)]
        else:
            bucket = tag
        buckets[i] = bucket
    return buckets


def build_mad_lib(
    prayer: Prayer,
    blank_ratio: float = 0.15,
    min_ratio: float = 0.10,
    max_ratio: float = 0.20,
    rng: random.Random | None = None,
) -> MadLib:
    """Tokenize a prayer and choose ~10-20% of its words to become blanks."""
    rng = rng or random.Random()
    tokens = _TOKEN_RE.findall(prayer.text)

    total_words = sum(1 for tok in tokens if tok[0].isalpha())
    candidate_buckets = _candidate_buckets(prayer, tokens)
    eligible = list(candidate_buckets)

    target = round(total_words * blank_ratio)
    target = max(round(total_words * min_ratio), min(target, round(total_words * max_ratio)))
    target = max(1, min(target, len(eligible)))

    chosen = sorted(rng.sample(eligible, target)) if eligible else []

    blanks: dict[int, Blank] = {}
    for i in chosen:
        bucket = candidate_buckets[i]
        category = rng.choice(_BUCKET_CATEGORIES[bucket])
        blanks[i] = Blank(index=i, category=category, original_word=tokens[i])

    return MadLib(prayer=prayer, tokens=tokens, blanks=blanks)
