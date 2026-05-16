# Problem 3. Primality Testing
# MIT 6.1200J Problem Set 5

import math


# ── Part (a): Fermat witness ───────────────────────────────────────────────────
#
# Claim: If the Fermat test returns Composite for (n, a), then n is composite.
#
# Proof (by contrapositive):
#   Assume n is prime.  We show the test never returns Composite.
#
#   Pick any a with 1 ≤ a ≤ n-1.  Since n is prime, gcd(a, n) = 1.
#   By Fermat's Little Theorem, a^{n-1} ≡ 1 (mod n).
#   So the test always gets result 1 and returns "I don't know" — never Composite.
#
#   Contrapositive: if the test returns Composite, then n is not prime,
#   i.e. n is composite.  □

print("Part (a) — Fermat test")
print()
print("Carmichael numbers: composite, but Fermat test fooled for all a coprime to n.")

def fermat_test(n, a):
    return pow(a, n - 1, n) == 1

for c, factoring in [(561, "3·11·17"), (1105, "5·13·17"), (1729, "7·13·19")]:
    tested  = [a for a in range(2, c) if math.gcd(a, c) == 1]
    fooled  = [a for a in tested if fermat_test(c, a)]
    print(f"  n = {c} = {factoring}: Fermat says 'I don't know' for "
          f"{len(fooled)}/{len(tested)} coprime a values")

print()
print("  (The only possible Fermat witnesses for a Carmichael number are")
print("   values sharing a common factor with n — as hard to find as factoring.)")


# ── Part (b): Square roots of 1 mod p ─────────────────────────────────────────
#
# Claim: If p is prime and x^2 ≡ 1 (mod p), then x ≡ ±1 (mod p).
#
# Proof:
#   x^2 ≡ 1  (mod p)
#   ⟺  x^2 - 1 ≡ 0  (mod p)
#   ⟺  (x - 1)(x + 1) ≡ 0  (mod p)
#   ⟺  p | (x - 1)(x + 1).
#
#   Since p is prime, by Lemma 9.4.2 (Euclid's Lemma):
#       p | (x - 1)   or   p | (x + 1).
#   Case 1: p | (x-1)  ⟹  x ≡  1  (mod p).
#   Case 2: p | (x+1)  ⟹  x ≡ -1  (mod p).
#
#   So the only square roots of 1 mod p are +1 and -1.  □
#
# (Contrast: for composite n, there can be four or more square roots of 1,
#  e.g. mod 8: {1, 3, 5, 7} all satisfy x^2 ≡ 1.  This gap is exactly what
#  Miller-Rabin exploits.)

print()
print("Part (b) — square roots of 1")
print()
print(f"  {'n':>5}  {'type':>10}  roots of x² ≡ 1 (mod n)")
print("  " + "─" * 42)
for n in [5, 7, 11, 13, 17, 8, 15, 35, 105]:
    roots = [x for x in range(n) if pow(x, 2, n) == 1]
    kind  = "prime" if all(n % i for i in range(2, n)) and n > 1 else "composite"
    print(f"  {n:>5}  {kind:>10}  {roots}")


# ── Part (c): Miller-Rabin ─────────────────────────────────────────────────────
#
# Setup: write n-1 = 2^e * k  (k odd).  Build the squaring sequence:
#   x_0 = a^k,  x_1 = x_0^2, ...,  x_e = a^{n-1}  (all mod n).
# Return Composite if:
#   (C1)  x_e ≢ 1  (mod n),  OR
#   (C2)  some consecutive pair has x_{i+1} ≡ 1 but x_i ≢ ±1  (mod n).
#
# Claim: returning Composite ⟹ n is composite.
#
# Proof (by contrapositive — assume n is prime, show test returns "I don't know"):
#
#   n prime ⟹ a^{n-1} ≡ 1 (mod n) by Fermat, so x_e = 1 and (C1) is never triggered.
#
#   Now look at the squaring sequence x_0, ..., x_e = 1.
#   Let i be the *first* index with x_i ≡ 1 (mod n).
#
#   If i = 0: x_0 = a^k ≡ 1, and there is no earlier pair → (C2) not triggered.
#
#   If i > 0: x_{i-1}^2 = x_i ≡ 1 (mod n).
#     By part (b) (n is prime), x_{i-1} ≡ ±1 (mod n).
#     So the pair (x_{i-1}, x_i) has x_i ≡ 1 and x_{i-1} ≡ ±1 → (C2) not triggered.
#     For all j < i-1 we have x_j ≢ 1, so (C2) cannot fire there.
#
#   In both cases the test returns "I don't know" — never Composite.
#   Contrapositive: Composite ⟹ n is not prime.  □

def miller_rabin_once(n, a):
    """True = 'I don't know', False = definitely Composite."""
    if n < 2:  return False
    if n == 2: return True
    if n % 2 == 0: return False
    e, k = 0, n - 1
    while k % 2 == 0:
        e += 1
        k //= 2
    x = pow(a, k, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(e - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False   # triggered (C1) or (C2)

def is_prime_naive(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n**0.5) + 1))

print()
print("Part (c) — Miller-Rabin test")
print()
print(f"  {'n':>6}  {'MR (all a<30)':>15}  {'actually':>10}  match?")
print("  " + "─" * 42)
for n in [5, 7, 11, 13, 17, 341, 561, 1105, 1729, 15, 49, 101, 997]:
    mr_says_prime = all(miller_rabin_once(n, a) for a in range(2, min(n, 30)))
    verdict  = "prob. prime"  if mr_says_prime else "composite"
    actually = "prime"        if is_prime_naive(n) else "composite"
    match    = "✓" if (mr_says_prime == is_prime_naive(n)) else "✗"
    print(f"  {n:>6}  {verdict:>15}  {actually:>10}  {match}")
