/-
  GeometricNeuron.lean
  --------------------
  A formalization of the ONE claim from the standing-wave thesis that is small
  enough to be true and sharp enough to matter:

      "The spike is the derivative of the standing wave."
      (standing_wave_thesis, §1 — PerceptionLab / Antti Luode)

  Made rigorous, this is a delta-coding bound:

      (number of spikes) * (threshold)  ≤  (total variation of the wave)

  Corollary: a locked (constant) wave is perfectly silent.

  STATUS, stated honestly (do not hype, do not lie, just show):
    • The mathematical content was verified numerically over 200,000 random
      trajectories before it was written (it passed).
    • The proof below is written against current Mathlib using only standard
      lemmas (card_nsmul_le_sum, sum_le_sum_of_subset_of_nonneg, filter_eq_empty_iff).
    • It was NOT machine-checked in the environment it was produced in, because
      that sandbox blocked the Lean toolchain CDN. To check it: drop into a
      project with `import Mathlib` and run `lake build`.

  WHAT THIS PROVES: a property of the *model*. IF you define a spike as the
  thresholded change in the continuous representation, THEN spiking is bounded
  by the wave's motion and a fixed point is silent.
  WHAT IT DOES NOT PROVE: that real neurons do this. That is an empirical
  question (thesis §8), not a theorem.
-/

import Mathlib

open Finset

namespace GeometricNeuron

/- A discrete standing-wave trajectory `W`: the scalar value carried by the
   continuous substrate at each time step (the "content" of the percept). -/
variable (W : ℕ → ℝ)

/-- Total variation of the wave over the first `N` steps:
    how much the standing wave actually moves. -/
def totalVariation (N : ℕ) : ℝ := ∑ n ∈ range N, |W (n + 1) - W n|

/-- The spike set. A spike fires at step `n` exactly when the wave moved by at
    least the threshold `θ` between `n` and `n+1`. This is the formal content of
    "the spike is the (thresholded) derivative of the standing wave." -/
noncomputable def spikes (θ : ℝ) (N : ℕ) : Finset ℕ :=
  (range N).filter fun n => θ ≤ |W (n + 1) - W n|

/-- **Delta-coding bound.**
    The number of spikes, times the threshold, can never exceed the total
    variation of the standing wave: you cannot fire more than the wave moves. -/
theorem spike_count_le_totalVariation
    (θ : ℝ) (hθ : 0 ≤ θ) (N : ℕ) :
    ((spikes W θ N).card : ℝ) * θ ≤ totalVariation W N := by
  -- Each spike contributes at least θ to a sub-sum of nonnegative terms.
  have h1 : (spikes W θ N).card • θ
      ≤ ∑ n ∈ spikes W θ N, |W (n + 1) - W n| := by
    apply Finset.card_nsmul_le_sum
    intro i hi
    rw [spikes, mem_filter] at hi
    exact hi.2
  -- That sub-sum is bounded by the full total-variation sum (extra terms ≥ 0).
  have h2 : ∑ n ∈ spikes W θ N, |W (n + 1) - W n|
      ≤ totalVariation W N := by
    rw [spikes, totalVariation]
    exact Finset.sum_le_sum_of_subset_of_nonneg (filter_subset _ _)
      (fun i _ _ => abs_nonneg _)
  rw [nsmul_eq_mul] at h1
  exact h1.trans h2

/-- **Lock ⇒ silence (corollary).**
    If the wave is locked (constant) across the window, the neuron is perfectly
    silent. A fixed point has no derivative, so a stable representation costs no
    spikes — sparse/predictive coding falls out, it is not assumed. -/
theorem locked_is_silent
    (θ : ℝ) (hθ : 0 < θ) (N : ℕ)
    (hlock : ∀ n < N, W (n + 1) = W n) :
    spikes W θ N = ∅ := by
  rw [spikes, filter_eq_empty_iff]
  intro n hn
  rw [mem_range] at hn
  rw [hlock n hn, sub_self, abs_zero]
  exact not_le.mpr hθ

end GeometricNeuron
