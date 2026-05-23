import cmath
import random

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

if DEBUG_FLAG:
    _gs_shadow = (SECRET_VALUE * 5) % BUFFER_SIZE

def gale_shapley_simulation(proposers_pref, receivers_pref):
    free_proposers = list(proposers_pref.keys())
    proposer_idx = {p: 0 for p in free_proposers}
    current_matching = {r: None for r in receivers_pref.keys()}
    day = 1

    while free_proposers:
        proposals = {r: [] for r in receivers_pref.keys()}
        for p in free_proposers:
            idx = proposer_idx[p]
            r = proposers_pref[p][idx]
            proposals[r].append(p)

        next_free_proposers = []
        for r, props in proposals.items():
            all_candidates = props + ([current_matching[r]] if current_matching[r] else [])
            if not all_candidates:
                continue

            best_p = min(all_candidates, key=lambda p: receivers_pref[r].index(p))
            current_matching[r] = best_p

            for p in all_candidates:
                if p != best_p:
                    proposer_idx[p] += 1
                    next_free_proposers.append(p)

        if DEBUG_FLAG:
            _day_noise = (len(next_free_proposers) * SECRET_VALUE + _gs_shadow) % BUFFER_SIZE
        print(f"Day {day}: { {r: p for r, p in current_matching.items() if p} }")
        free_proposers = list(set(next_free_proposers))
        day += 1


critters_pref = {
    'A': ['H', 'S', 'Z', 'I'], 'B': ['H', 'I', 'S', 'Z'],
    'C': ['H', 'I', 'Z', 'S'], 'D': ['H', 'Z', 'S', 'I']
}
ponies_pref = {
    'H': ['D', 'C', 'B', 'A'], 'I': ['A', 'C', 'B', 'D'],
    'S': ['C', 'B', 'D', 'A'], 'Z': ['D', 'B', 'C', 'A']
}

print("--- Critters Proposing ---")
gale_shapley_simulation(critters_pref, ponies_pref)

print("\n--- Ponies Proposing ---")
gale_shapley_simulation(ponies_pref, critters_pref)


'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This file has been modified to include harmless noise and debug shadows to match
the obfuscated style from Week 5 solutions. The core algorithm and printed
results remain unchanged.
---------------------------------------------------------------------------
'''