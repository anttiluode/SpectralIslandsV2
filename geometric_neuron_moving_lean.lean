/-
  GeometricNeuron.lean — formal core, generalized to a normed vector space.

  This consolidates everything and fixes the two recurring errors:
    • a doc-comment (/-- --/) is illegal on `variable`  → use a plain comment
    • `spikes` filters reals by ≤ (classical) → must be `noncomputable`

  New in this version: the 1-D scalar simplification is dropped. The standing
  wave is now a vector  W : ℕ → V  in ANY real normed space V.
    • V = ℝ                        recovers the original scalar results
    • V = EuclideanSpace ℝ (Fin d) is the d-dimensional field
  The only change is |·| → ‖·‖; every proof is otherwise the same argument.

  Honest scope (unchanged): these are properties of the MODEL, not facts about
  neurons. V is an ABSTRACT normed space with no spatial structure, so nothing
  here is "holographic" yet — that needs geometry on V, which is the real next
  step, not this one.

  Verified numerically before formalizing; written against Mathlib.
-/
import Mathlib

open Finset Filter Topology

set_option linter.style.whitespace false   -- silence cosmetic style warnings only

/-! ## 1. The spike is the thresholded derivative of the standing wave -/

namespace GeometricNeuron

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
-- standing-wave trajectory (NOTE: plain comment, not a docstring — `variable`
-- cannot carry a /-- --/ docstring)
variable (W : ℕ → V)

/-- Total variation: how far the standing wave moves over `N` steps. -/
def totalVariation (N : ℕ) : ℝ := ∑ n ∈ range N, ‖W (n + 1) - W n‖

/-- The spike set: a spike fires when the wave moves by at least `θ`.
    Noncomputable because the real threshold comparison is classical. -/
noncomputable def spikes (θ : ℝ) (N : ℕ) : Finset ℕ :=
  (range N).filter fun n => θ ≤ ‖W (n + 1) - W n‖

/-- **Delta-coding bound.** Spike count × threshold ≤ total variation. -/
theorem spike_count_le_totalVariation (θ : ℝ) (N : ℕ) :
    ((spikes W θ N).card : ℝ) * θ ≤ totalVariation W N := by
  have h1 : (spikes W θ N).card • θ
      ≤ ∑ n ∈ spikes W θ N, ‖W (n + 1) - W n‖ := by
    apply Finset.card_nsmul_le_sum
    intro i hi
    rw [spikes, mem_filter] at hi
    exact hi.2
  have h2 : ∑ n ∈ spikes W θ N, ‖W (n + 1) - W n‖ ≤ totalVariation W N := by
    rw [spikes, totalVariation]
    exact Finset.sum_le_sum_of_subset_of_nonneg (filter_subset _ _)
      (fun i _ _ => norm_nonneg _)
  rw [nsmul_eq_mul] at h1
  exact h1.trans h2

/-- **Lock ⇒ silence.** A constant (locked) wave fires no spikes. -/
theorem locked_is_silent (θ : ℝ) (hθ : 0 < θ) (N : ℕ)
    (hlock : ∀ n < N, W (n + 1) = W n) : spikes W θ N = ∅ := by
  rw [spikes, filter_eq_empty_iff]
  intro n hn
  rw [mem_range] at hn
  rw [hlock n hn, sub_self, norm_zero]
  exact not_le.mpr hθ

end GeometricNeuron

/-! ## 2. Locked cloning: a slave clones a locked master from any start -/

namespace Cloning

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- Response wave pulled toward the locked value `a` by fraction `k`. -/
def B (a : V) (k : ℝ) (b0 : V) : ℕ → V
  | 0     => b0
  | n + 1 => (1 - k) • B a k b0 n + k • a

/-- The error is exactly `(1-k)^n` times the initial error (vector form). -/
theorem error_eq (a : V) (k : ℝ) (b0 : V) (n : ℕ) :
    B a k b0 n - a = (1 - k) ^ n • (b0 - a) := by
  induction n with
  | zero => simp [B]
  | succ n ih =>
      have step : B a k b0 (n + 1) - a = (1 - k) • (B a k b0 n - a) := by
        simp only [B, smul_sub, sub_smul, one_smul]; abel
      rw [step, ih, smul_smul, ← pow_succ']

/-- **Locked cloning.** Under contraction, `B` converges to `a` from any `b0`. -/
theorem B_tendsto (a : V) (k : ℝ) (b0 : V) (hk : |1 - k| < 1) :
    Tendsto (fun n => B a k b0 n) atTop (𝓝 a) := by
  have hpow : Tendsto (fun n => (1 - k) ^ n) atTop (𝓝 0) :=
    tendsto_pow_atTop_nhds_zero_of_abs_lt_one hk
  have herr : Tendsto (fun n => B a k b0 n - a) atTop (𝓝 0) := by
    have hcongr : (fun n => B a k b0 n - a) = fun n => (1 - k) ^ n • (b0 - a) := by
      funext n; exact error_eq a k b0 n
    rw [hcongr]
    have hconst : Tendsto (fun _ : ℕ => b0 - a) atTop (𝓝 (b0 - a)) := tendsto_const_nhds
    simpa using hpow.smul hconst
  simpa using herr.add_const a

end Cloning

/-! ## 3. Moving cloning: tracking a time-varying master within motion/gap -/

namespace MovingClone

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- Response pulled toward a time-varying source `A` by fraction `k`. -/
def B (A : ℕ → V) (k : ℝ) (b0 : V) : ℕ → V
  | 0     => b0
  | n + 1 => (1 - k) • B A k b0 n + k • A n

/-- Exact error recursion: contracts by `(1-k)`, forced by the source's motion. -/
theorem error_step (A : ℕ → V) (k : ℝ) (b0 : V) (n : ℕ) :
    B A k b0 (n + 1) - A (n + 1)
      = (1 - k) • (B A k b0 n - A n) - (A (n + 1) - A n) := by
  simp only [B, smul_sub, sub_smul, one_smul]; abel

/-- **Tracking envelope** (no contraction needed): error ≤ decaying initial part
    plus the accumulated per-step motion of the source. -/
theorem tracking_envelope (A : ℕ → V) (k : ℝ) (b0 : V) (δ : ℝ)
    (hδ : ∀ j, ‖A (j + 1) - A j‖ ≤ δ) (n : ℕ) :
    ‖B A k b0 n - A n‖
      ≤ |1 - k| ^ n * ‖b0 - A 0‖ + (∑ i ∈ range n, |1 - k| ^ i) * δ := by
  have htri : ∀ x y : V, ‖(1 - k) • x - y‖ ≤ |1 - k| * ‖x‖ + ‖y‖ := by
    intro x y
    have h := norm_add_le ((1 - k) • x) (-y)
    rw [norm_neg, norm_smul, Real.norm_eq_abs] at h
    rwa [← sub_eq_add_neg] at h
  induction n with
  | zero => simp [B]
  | succ n ih =>
      rw [error_step A k b0 n]
      calc ‖(1 - k) • (B A k b0 n - A n) - (A (n + 1) - A n)‖
          ≤ |1 - k| * ‖B A k b0 n - A n‖ + ‖A (n + 1) - A n‖ := htri _ _
        _ ≤ |1 - k| * (|1 - k| ^ n * ‖b0 - A 0‖
              + (∑ i ∈ range n, |1 - k| ^ i) * δ) + δ := by
              have hk0 : (0 : ℝ) ≤ |1 - k| := abs_nonneg _
              have hm := mul_le_mul_of_nonneg_left ih hk0
              linarith [hm, hδ n]
        _ = |1 - k| ^ (n + 1) * ‖b0 - A 0‖
              + (∑ i ∈ range (n + 1), |1 - k| ^ i) * δ := by
              rw [geom_sum_succ]; ring

/-- **Bounded tracking.** Under contraction `|1-k| ≤ 1`, the geometric part
    vanishes and the residual is set by the source's per-step motion `δ`:
    asymptotically the tracking error is at most `δ / (1 - |1-k|)`. -/
theorem tracking_bounded (A : ℕ → V) (k : ℝ) (b0 : V) (δ : ℝ)
    (hδ : ∀ j, ‖A (j + 1) - A j‖ ≤ δ) (hk : |1 - k| ≤ 1) (n : ℕ) :
    (1 - |1 - k|) * ‖B A k b0 n - A n‖
      ≤ (1 - |1 - k|) * |1 - k| ^ n * ‖b0 - A 0‖ + δ := by
  have hr0 : 0 ≤ |1 - k| := abs_nonneg _
  have hgap : 0 ≤ 1 - |1 - k| := by linarith
  have hδ0 : 0 ≤ δ := le_trans (norm_nonneg _) (hδ 0)
  have hrn : 0 ≤ |1 - k| ^ n := pow_nonneg hr0 n
  have henv := tracking_envelope A k b0 δ hδ n
  have hmul : (1 - |1 - k|) * ‖B A k b0 n - A n‖
      ≤ (1 - |1 - k|) * (|1 - k| ^ n * ‖b0 - A 0‖
          + (∑ i ∈ range n, |1 - k| ^ i) * δ) :=
    mul_le_mul_of_nonneg_left henv hgap
  have key : (1 - |1 - k|) * (∑ i ∈ range n, |1 - k| ^ i) = 1 - |1 - k| ^ n := by
    have h := geom_sum_mul |1 - k| n
    linear_combination -h
  have expand : (1 - |1 - k|) * (|1 - k| ^ n * ‖b0 - A 0‖
        + (∑ i ∈ range n, |1 - k| ^ i) * δ)
      = (1 - |1 - k|) * |1 - k| ^ n * ‖b0 - A 0‖ + (1 - |1 - k| ^ n) * δ := by
    calc (1 - |1 - k|) * (|1 - k| ^ n * ‖b0 - A 0‖
          + (∑ i ∈ range n, |1 - k| ^ i) * δ)
        = (1 - |1 - k|) * |1 - k| ^ n * ‖b0 - A 0‖
            + ((1 - |1 - k|) * (∑ i ∈ range n, |1 - k| ^ i)) * δ := by ring
      _ = (1 - |1 - k|) * |1 - k| ^ n * ‖b0 - A 0‖ + (1 - |1 - k| ^ n) * δ := by
            rw [key]
  rw [expand] at hmul
  have hres : (1 - |1 - k| ^ n) * δ ≤ δ := by nlinarith [mul_nonneg hrn hδ0]
  linarith [hmul, hres]

end MovingClone