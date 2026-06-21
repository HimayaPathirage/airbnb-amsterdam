# Section 5.1 - H1: Entire-home vs. Private Room Pricing

**Null hypothesis (H0):** There is no difference in price distribution 
between entire-home and private-room listings.

**Alternative hypothesis (H1):** Entire-home listings have a 
significantly different (higher) price distribution than private-room 
listings.

**Test selected:** Mann-Whitney U test (non-parametric).

**Assumption check:** Independent t-test requires approximately normal 
data. Shapiro-Wilk test on both groups returned p < 0.001 (effectively 
p ≈ 0), confirming both distributions deviate significantly from 
normality (consistent with the known right-skew in price, Section 
4.1). Mann-Whitney U was selected instead, as it does not require 
normality, only that data be ordinal/continuous, which holds here.

**Results:**
- U statistic: 4,680,826.5
- p-value: 4.95 x 10^-253 (far below alpha = 0.05)
- Effect size (rank-biserial correlation): -0.622 (large effect)
- Entire home: n=4,530, mean=€301.00
- Private room: n=1,274, mean=€175.73

**Conclusion:** Since p-value (4.95 x 10^-253) < alpha (0.05), we 
reject the null hypothesis. This confirms that entire-home listings 
have a significantly different (higher) price distribution than 
private-room listings.

**Interpretation for a non-technical stakeholder:** Entire-home 
listings are priced substantially higher than private rooms in 
Amsterdam, and this difference is both statistically rock-solid (not 
due to chance) and practically large (not just a tiny, technical 
difference). On average, entire-home listings cost roughly 71% more 
than private rooms. For a market intelligence consultancy, this 
confirms that property type is one of the strongest, most reliable 
price drivers in this market, a finding that should anchor any pricing 
or investment recommendation.

# Section 5.1 - H2: Superhost vs. Non-Superhost Review Scores

**Null hypothesis (H0):** There is no difference in review score 
distribution between superhost and non-superhost listings.

**Alternative hypothesis (H1):** Superhost listings achieve a 
significantly higher review score distribution than non-superhost 
listings.

**Test selected:** Mann-Whitney U test (non-parametric).

**Assumption check:** Shapiro-Wilk test on both groups returned 
p < 0.001 (effectively p ≈ 0) for both, confirming severe non-
normality, consistent with the rating inflation pattern already 
documented in Section 4.1 (most scores cramped between 4.5 and 5.0). 
Mann-Whitney U was selected accordingly.

**Results:**
- U statistic: 5,894,053.0
- p-value: 2.01 x 10^-18 (far below alpha = 0.05)
- Effect size (rank-biserial correlation): 0.128 (small effect)
- Superhost: n=1,813, mean=4.865
- Non-superhost: n=7,460, mean=4.839

**Conclusion:** Since p-value (2.01 x 10^-18) < alpha (0.05), we reject 
the null hypothesis. This confirms that superhost listings have a 
statistically significantly higher review score distribution than 
non-superhost listings.

**Interpretation for a non-technical stakeholder:** Superhosts do score 
slightly higher than non-superhosts, and this difference is real, not 
just random chance. But the gap is tiny: only 0.026 points on a 
5-point scale. With this many listings in the data, even a very small 
difference shows up as "statistically significant," but it doesn't 
mean much in practice. A guest is unlikely to notice or care about a 
difference this small when choosing where to book. For a market 
intelligence consultancy, this means superhost status shouldn't be 
treated as a strong signal of better guest experience, the score 
difference it creates is real but too small to matter much.

# Section 5.1 - H3: Price Difference by Review Count (>10 vs <=10 reviews)

**Null hypothesis (H0):** There is no difference in price distribution 
between listings with more than 10 reviews and listings with 10 or 
fewer reviews.

**Alternative hypothesis (H1):** Listings with more than 10 reviews 
have a significantly different price distribution than listings with 
10 or fewer reviews.

**Test selected:** Mann-Whitney U test (non-parametric).

**Assumption check:** Shapiro-Wilk test on both groups returned 
p < 0.001 (effectively p ≈ 0) for both, confirming severe non-
normality (consistent with the known right-skew in price). Mann-
Whitney U was selected accordingly.

**Results:**
- U statistic: 3,627,805.5
- p-value: 6.98 x 10^-25 (far below alpha = 0.05)
- Effect size (rank-biserial correlation): 0.155 (small effect)
- More than 10 reviews: n=3,054, mean=€257.32
- 10 or fewer reviews: n=2,813, mean=€288.79

**Conclusion:** Since p-value (6.98 x 10^-25) < alpha (0.05), we 
reject the null hypothesis. This confirms that listings with more 
than 10 reviews have a significantly different price distribution 
than listings with 10 or fewer reviews.

**Interpretation for a non-technical stakeholder:** Listings with more 
reviews are actually priced lower on average (€257) than listings with 
fewer reviews (€289), the opposite of what you might expect if more 
reviews simply meant a more popular, premium listing. A likely 
explanation: cheaper listings get booked more often, so they build up 
review counts faster, while pricier listings may book less frequently 
and take longer to accumulate the same number of reviews. The effect 
is real but modest in size. For a market intelligence consultancy, 
this means a high review count should be read as a sign of booking 
volume and affordability, not necessarily as a sign of a premium or 
higher-quality listing.

# Section 5.1 - H4: Neighbourhood Price Differences (ANOVA)

**Null hypothesis (H0):** Mean price does not differ across Amsterdam's 
22 neighbourhoods.

**Alternative hypothesis (H1):** Mean price differs significantly 
across at least some of Amsterdam's 22 neighbourhoods.

**Test selected:** Kruskal-Wallis H test (non-parametric one-way 
ANOVA equivalent).

**Assumption check:** Standard one-way ANOVA requires both normality 
within groups and homogeneity of variance across groups. Levene's test 
for equal variances returned p = 2.03 x 10^-7, well below 0.05, 
confirming variances differ significantly across neighbourhoods. 
Combined with price's already-documented non-normality (Section 4.1), 
Kruskal-Wallis was selected as the appropriate non-parametric 
alternative.

**Results:**
- H statistic: 417.23
- p-value: 2.51 x 10^-75 (far below alpha = 0.05)
- Effect size (eta-squared): 0.068 (small-to-medium effect)

**Conclusion:** Since p-value (2.51 x 10^-75) < alpha (0.05), we 
reject the null hypothesis. This confirms that mean price differs 
significantly across Amsterdam's neighbourhoods.

**Interpretation for a non-technical stakeholder:** Neighbourhood does 
have a real, statistically confirmed effect on price, but it's a 
modest one. Neighbourhood alone explains only about 7% of the total 
variation in listing prices, meaning roughly 93% of why one listing 
costs more than another comes from other factors, like property type, 
room type, or size, not simply which part of the city it's in. For a 
market intelligence consultancy, this means location matters for 
pricing strategy, but it should not be treated as the primary driver. 
Property type (Section 5.1, H1) has a far larger effect on price than 
neighbourhood does.

# Section 5.1 - H5: Weekend vs. Weekday Pricing

**Null hypothesis (H0):** There is no difference between weekend and 
weekday pricing.

**Alternative hypothesis (H1):** Weekend and weekday prices differ 
significantly.

**Status: NOT TESTABLE with available data.**

**Reason:** This hypothesis requires calendar.csv.gz's price field, 
broken down by date (to classify each day as weekend or weekday). As 
established in Section 3.1 and re-confirmed in Section 4.3, this field 
is 100% null for Amsterdam across all 3,825,200 calendar rows. 
listings.csv.gz only provides a single static current price per 
listing, with no day-of-week breakdown possible.

## 5.2 Confidence Intervals - Business Interpretation

Confidence intervals reveal an important nuance the overall Kruskal-
Wallis test (H4) cannot show on its own: while neighbourhood price 
differences are statistically significant overall, not every pair of 
neighbourhoods is clearly distinguishable from each other. Centrum-
West, Centrum-Oost, and Zuid have overlapping confidence intervals, 
meaning we cannot confidently say their true average prices differ 
from one another, despite showing different point estimates (€315.88, 
€307.72, €309.58). In contrast, Centrum-West's interval does not 
meaningfully overlap with De Baarsjes - Oud-West's, suggesting these 
two are genuinely different in price.

Sample size also matters directly: smaller groups like Hotel room 
(n=33) and Shared room (n=30) produce much wider, less certain 
intervals than large groups like Entire home/apt (n=4,530). For a 
market intelligence consultancy, this means confidence in a "typical 
price" figure should always be weighed against how many listings that 
figure is based on, a mean price quoted from 30 listings carries far 
more uncertainty than one quoted from 4,500.

---

## 5.2 Practical vs. Statistical Significance Summary

Across all four testable hypotheses (H1-H4), every result was 
statistically significant (p < 0.001 in all cases), but effect sizes 
varied widely:

- H1 (room type, price): effect size 0.622, large. Statistically 
  significant AND practically important.
- H2 (superhost, rating): effect size 0.128, small. Statistically 
  significant but practically minor.
- H3 (review count, price): effect size 0.155, small. Statistically 
  significant but practically modest.
- H4 (neighbourhood, price): effect size 0.068, small-to-medium. 
  Statistically significant but explains only ~7% of price variance.

This pattern is a direct result of Amsterdam's large sample size 
(10,480 listings): with this much data, even small, practically minor 
differences become statistically detectable. The lesson for any 
stakeholder reading this report: p-values alone tell you whether an 
effect exists, but effect sizes tell you whether that effect actually 
matters. Room/property type (H1) is the only finding in this set 
large enough to be a primary driver of pricing strategy on its own; 
the others are real but secondary factors.

---

## 5.2 Cohen's d vs. Rank-Biserial Correlation Note

**Cohen's d for H1 (entire home vs. private room price): 0.345** 
(small-to-medium effect).

**Why this is smaller than the rank-biserial correlation (0.622, 
large) reported earlier for the same comparison:** Cohen's d uses raw 
means and standard deviations. Price has a few very high values that 
make the standard deviation large, and this makes Cohen's d look 
smaller than the real difference actually is. Rank-biserial correlation 
works on the order of values instead of the raw numbers, so it isn't 
thrown off by those extreme prices. That's why it gives a more honest 
picture of how different the two groups really are.

**Decision:** Rank-biserial correlation stays as the main effect size 
used throughout this section, since it matches the tests we actually 
used (Mann-Whitney U). Cohen's d is shown here once for H1 only, just 
to directly answer the brief's mention of it, along with this note 
explaining why it understates the real effect.

---

## 5.3 Correlation & Regression Analysis

**Correlation findings:** Bedrooms (r=0.273), accommodates (r=0.271), 
and beds (r=0.234) are the strongest numerical correlates with price, 
all capacity-related. Review score (r=0.038), host tenure (r=-0.003), 
and minimum nights (r=-0.022) show negligible correlation with price 
on their own.

**OLS regression:** A multiple linear regression using accommodates, 
bedrooms, beds, review_scores_rating, availability_365, 
review_count_computed, and host_tenure_years as predictors of price 
produced R-squared = 0.096 (the model explains about 9.6% of price 
variation), with the overall model highly significant (F-statistic 
p < 0.001).

Significant predictors: accommodates (+€42.72 per additional guest 
capacity), bedrooms (+€54.59 per bedroom), review_scores_rating 
(+€46.77 per point, once other factors are held constant), 
availability_365 (+€0.23 per day), and review_count_computed (-€0.12 
per review), all p < 0.01. Beds showed a significant but negative 
coefficient (-€12.41 per bed), discussed below. Host_tenure_years was 
not significant (p=0.214).

**Multicollinearity check (VIF):** accommodates (3.19), beds (2.87), 
and bedrooms (2.44) all fall below the conventional concern threshold 
of 5, and well below the severe threshold of 10 (the const row's VIF 
of 372.72 is a known statistical artifact and not meaningful). This 
means multicollinearity is present, as expected for three capacity-
related variables, but not severe by standard thresholds.

**Interpreting beds' negative coefficient:** Despite VIF values 
showing only moderate overlap between beds, bedrooms, and accommodates, 
beds' coefficient flips negative once the other two are included in 
the model. A plausible explanation: holding accommodates and bedrooms 
fixed, a higher bed count may signal a more budget, hostel-style 
configuration (e.g., bunk beds, sofa beds), rather than added value. 
This should be treated as a tentative interpretation, not a fully 
confirmed causal finding, given the modest multicollinearity still 
present.

**Business interpretation:** Capacity (accommodates, bedrooms) remains 
the strongest, most reliable price driver among the numerical features 
tested, consistent with the property-type findings in Section 5.1. 
However, the model's low R-squared (9.6%) confirms that most of what 
determines price in this market is NOT captured by these basic 
numerical features alone, property type, neighbourhood, and unmeasured 
factors like amenities and listing quality likely matter far more. 
This regression should be read as a useful but limited piece of the 
overall pricing picture, not a complete price prediction model.

## 5.3 Non-Linear Relationship Check (LOWESS)

**Finding:** The LOWESS curve for price vs. accommodates is clearly 
non-linear. Price rises steeply from 1 to 4 guests, flattens 
noticeably between 6 and 10 guests, then rises again toward the 
high end (12-16 guests).

**Implication:** The OLS regression's linear coefficient for 
accommodates (+€42.72 per guest) is a reasonable average across the 
full range, but it overstates the true marginal price increase in the 
6-10 guest range and may understate it at the very top end (12+ 
guests). A more accurate model would treat accommodates as a 
non-linear feature (e.g., using bins or a polynomial term) rather than 
assuming a constant price increase per additional guest across the 
entire range.

**Business interpretation:** The biggest price jump happens early, 
moving from a 1-2 person studio to a 4-person apartment captures most 
of the capacity-driven price increase. Beyond that, adding a few more 
guests of capacity (6-10) doesn't proportionally increase price much, 
suggesting these mid-size properties compete in a fairly narrow price 
band regardless of exact capacity. Only very large group properties 
(12+) break into a distinctly higher price tier again, likely a 
different market segment (event houses, large group stays) rather 
than a simple continuation of the same pricing logic.