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
