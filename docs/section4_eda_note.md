# Section 4 — EDA Notes

---

## 4.1 Descriptive Statistics — Key Findings

- **Price:** Median €222/night is more representative than the mean 
  (€336.79), which is skewed upward by a small number of extreme/
  erroneous high prices. Market benchmarking should use median.
- **Capacity:** Market is dominated by small accommodations — median 
  2 guests, 1 bedroom, 1 bed. Large group properties are rare.
- **Rating inflation confirmed:** 75% of listings score 4.79+ out of 5. 
  Ratings provide very little differentiation between listings — most 
  guests rate generously regardless of actual experience quality.
- **Availability:** Median listing is available only 20 of 365 days — 
  most supply is effectively "closed" most of the year, though this 
  conflates genuine demand with host-side calendar blocking (known 
  caveat).
- **Reviews:** Strong power-law pattern (mean 47.8, median 10, max 
  5,097) — a small number of long-running listings dominate review 
  volume.

## 4.1 Price Distribution by Room/Property Type — Business Interpretation

Entire-home listings command roughly double the price of private rooms 
and triple that of shared rooms, with the highest pricing variance and 
the most extreme high-end outliers concentrated in this category. For 
a market operator, this suggests entire-home listings are where premium 
positioning and luxury pricing strategies actually play out — private 
and shared rooms compete primarily on a tighter, lower price band with 
limited room for premium differentiation. Houseboats/boats command a 
modest premium even over standard entire-place listings, reflecting 
their status as a distinctive, Amsterdam-specific draw — a host 
considering property type investment would see this as the strongest 
differentiator after basic capacity/room-type choice.

## 4.1 Price Distribution by Neighbourhood (Top 10) - Business Interpretation

Among the most heavily-supplied neighbourhoods, De Baarsjes - Oud-West, 
Centrum-West, and De Pijp - Rivierenbuurt sustain the highest median 
prices (around €240-250), showing that high listing density does not 
suppress pricing in Amsterdam's most popular districts; demand appears 
strong enough to support both volume and premium pricing simultaneously. 
By contrast, Bos en Lommer and Oud-Noord, despite similarly high listing 
counts, show noticeably lower and more tightly clustered prices, 
pointing to a more budget-oriented market segment. For an investor or 
host choosing where to list a new property, this suggests neighbourhood 
choice has a real, measurable impact on achievable price, independent 
of how saturated that market already is.

## 4.1 Listing Counts per Host (Power-Law Dynamics) - Business Interpretation

Amsterdam's Airbnb market is overwhelmingly composed of casual, 
single-property hosts: 93.7% of all hosts manage exactly one listing, 
together accounting for 82.3% of total supply. A small group of 
commercial-style operators exists at the other extreme (the largest 
single host manages 35 listings), but this group remains a minority 
of overall supply, around 6.3% of hosts controlling roughly 17.7% of 
listings. For a market intelligence consultancy, this means platform-
level dynamics in Amsterdam are still largely driven by individual, 
small-scale hosts rather than institutional or large commercial 
operators, which has implications for how regulation, host-support 
programs, or competitive analysis should be framed; policies aimed at 
"professional" operators would only directly affect a small minority 
of the market's actual supply base.

## 4.1 Review Score Distribution - Business Interpretation

Review scores in Amsterdam's Airbnb market show severe rating 
inflation: nearly all listings score between 4.5 and 5.0, with the 
median sitting at 4.92 out of 5. Scores below 4.0 are vanishingly 
rare. This means the rating system, as currently used by guests, 
provides very little practical ability to distinguish a "good" 
listing from a "great" one; nearly everyone scores in the top band 
regardless of true quality variation. For a market intelligence 
consultancy, this has a direct implication: review scores should not 
be used as a primary differentiator in any host or listing 
segmentation work. Review count and review text content are likely 
far more informative signals of actual guest experience than the 
numeric score itself, since the score has effectively become a 
near-universal "satisfactory" stamp rather than a genuine quality 
gradient.

## 4.1 Seasonal Availability Pattern - Business Interpretation

Amsterdam listings show a clear seasonal pattern: availability is 
highest in winter months (around 30-32% in January, February, 
November, December) and lowest during the summer tourist season 
(around 22-23% in June through August), with September showing the 
single lowest point (17.8%). This aligns with known tourism patterns, 
Amsterdam's peak visitor season drives higher booking activity and 
therefore lower open availability in summer, while winter sees hosts 
either renting less actively or blocking calendars for personal use. 
For a market operator, this means pricing strategies should expect 
tighter supply (and likely stronger pricing power) from June through 
September, with more competitive, open inventory in winter months. 
One caveat: since the data reflects a rolling 365-day window

---

## 4.2 Listing Density Map - Business Interpretation

Listing supply is heavily concentrated in central Amsterdam, with the 
darkest-shaded neighbourhood (the highest density tier, 1,808 listings) 
sitting directly in the historic city center. Density fades 
progressively outward toward the city's edges, where neighbourhoods 
show far fewer listings. For a market operator or new host considering 
where to enter the market, this confirms that central neighbourhoods 
are both the most competitive (highest supply) and, per the earlier 
price analysis, simultaneously the highest-priced areas; central 
positioning offers strong demand but also the most direct competition 
from other hosts.

## 4.2 Geographic Pricing Gradient - Business Interpretation

Distance from the city center shows essentially no linear correlation 
with price (r = 0.022). Visual inspection reveals why: the highest 
priced listings, including most premium and luxury-tier properties, 
cluster within the first 1-2km of the center, but plenty of low-priced 
listings exist in that same zone too, meaning price variation close to 
the center is driven by property type and quality rather than fine-
grained location. Beyond roughly 5-6km, the price range narrows and 
shifts lower overall, suggesting a loose outer boundary rather than a 
smooth pricing gradient. For a market intelligence consultancy, this 
means "distance from center" alone is a weak pricing predictor; 
property type, room type, and neighbourhood-specific factors (as shown 
in the earlier neighbourhood comparison) matter far more than simple 
proximity once a listing is already within Amsterdam's compact, 
walkable core.

## 4.2 Spatial Review Score Patterns - Business Interpretation

While most Amsterdam neighbourhoods cluster tightly within the 4.80-
4.88 range (consistent with the citywide rating inflation pattern 
found in Section 4.1), two neighbourhoods stand out as genuinely lower 
scoring: Bijlmer-Centrum (4.64 average, based on 61 rated listings) and 
Gaasperdam - Driemond (4.71 average, 57 rated listings). Both are 
located in Amsterdam's southeastern Bijlmer district, a residential 
area architecturally and demographically distinct from the historic 
city center. With sample sizes in the 50-60+ range, this gap is 
unlikely to be a statistical fluke. For a market intelligence 
consultancy, this suggests the Bijlmer area may have a genuine guest 
experience gap worth investigating further, whether driven by property 
condition, host responsiveness, or guest expectations mismatched to a 
less touristic residential area, rather than being explained away as 
random noise in an otherwise inflated rating system.

## 4.2 Property Type Geographic Clustering - Business Interpretation

Houseboat/Boat listings show a clear, non-random spatial pattern, 
tracing distinct linear and curved paths across the map rather than 
spreading evenly like most other property types. These patterns 
almost certainly correspond to Amsterdam's canal network, since 
houseboats can only be located on waterways, meaning the geography 
itself constrains where this property type exists. For a market 
intelligence consultancy, this means houseboat supply is structurally 
limited and cannot expand into arbitrary new neighbourhoods the way 
entire-place or private-room listings can; any analysis of growth 
potential for this category must account for a hard physical ceiling 
on available canal frontage, rather than treating it as a normal, 
expandable market segment.

---

## 4.3 Pricing Over the Calendar Year - Limitation

**Finding:** calendar.csv.gz's price and adjusted_price fields are 
100% null (0 non-null values out of 3,825,200 rows), confirmed again 
here. This was first identified in Section 3.1 and is a known dataset 
limitation (scraping artifact specific to this city/batch).

**Conclusion:** True seasonal pricing analysis (how nightly price 
itself changes month to month) cannot be performed with this dataset, 
since no source field captures price over time. listings.csv.gz only 
contains a single, current snapshot price per listing, not a 
historical or forward time series.

**Workaround attempted:** Section 4.1 already analyzed seasonal 
AVAILABILITY patterns (using the available t/f field), which serves 
as a partial proxy for demand intensity by month, even though it 
cannot speak to price itself. This is the closest substitute available 
within this dataset's constraints.

**Honest scope decision:** This specific bullet point is not fully 
achievable with the data as provided. Rather than fabricate a price-
over-time chart from unusable data, this limitation is documented 
directly, consistent with the assignment's emphasis on honest 
prioritization over completing every bullet point regardless of 
feasibility.

## 4.3 Review Volume Trends Over Time - Business Interpretation

Review volume, used here as a proxy for booking activity, shows strong, 
consistent year-over-year growth from 2010 through 2019 (7 reviews to 
nearly 50,000), reflecting Amsterdam's broader adoption of short-term 
rentals over the decade. This growth is sharply interrupted in 2020 
(down to 17,883, a clear COVID-19 travel collapse), with a partial 
recovery in 2021 still well below pre-pandemic levels. By 2022-2024, 
volume not only recovered but substantially exceeded 2019 levels, 
peaking at 85,885 reviews in 2024, suggesting Amsterdam's short-term 
rental demand is structurally larger post-pandemic than it was before 
it. The apparent drop in 2025 (64,756) should not be read as a genuine 
decline: since the dataset was scraped in September 2025, this figure 
reflects only a partial year and is not directly comparable to the 
full-year totals for prior years. For a market intelligence 
consultancy, the key takeaway is that Amsterdam's market has not just 
recovered from the pandemic but grown beyond its previous scale, 
demand-side fundamentals appear stronger now than at any prior point 
in the dataset's history.

## 4.3 Host Tenure vs. Price - Business Interpretation

Host tenure shows only a weak relationship with pricing. Newer hosts 
(0-2 years) show the lowest median price (€213), slightly below more 
established hosts (€222-232 across other tenure groups), which may 
reflect new hosts pricing more conservatively to attract initial 
bookings and reviews. However, the gap is modest, not dramatic, and 
there is no clear, continuously increasing trend with tenure; 5-10 
year and 10+ year hosts show nearly identical median pricing. For a 
market intelligence consultancy, this suggests host experience alone 
is not a strong driver of pricing strategy in this market; other 
factors (property type, location, host professionalism level) likely 
matter considerably more than simple time-on-platform.

## 4.3 Minimum Night Policies - Findings & Limitations

**Finding:** 71 listings (0.7% of total) require minimum stays over 30 
nights, with names like "Student Haven: Long-Term Retreat for 
Scholars" and "17th Century Monumental House with Garden" confirming 
these are genuine long-term/extended-stay rentals, not data errors. 
This represents a distinct market segment operating alongside the 
standard short-term tourist rental market (median minimum_nights of 
2-3 for the broader market).

**Limitation on seasonal analysis:** The bullet asks how minimum night 
policies shift across seasons or events. listings.csv.gz only provides 
a current snapshot of minimum_nights (plus minimum_minimum_nights/
maximum_minimum_nights, which capture a forward-looking range but not 
which specific months correspond to which values). A true month-by-
month breakdown would require pulling minimum_nights directly from 
calendar.csv.gz by date, which was not pursued further given time 
constraints and the modest expected analytical payoff relative to 
other priorities this week.

**Business interpretation:** The presence of a small but distinct 
long-term-stay segment (0.7% of listings) suggests some hosts use 
Airbnb as a flexible alternative to traditional long-term leasing, 
likely for reasons including avoiding standard tenant protection 
laws or seeking higher effective returns than long-term leases. This 
is a noteworthy edge case for a market intelligence consultancy to be 
aware of, but it represents a small enough share of supply that it 
should not be conflated with the core short-term rental market 
analysis the rest of this report focuses on.

---

## 4.4 Superhost Status and Property Type - Business Interpretation

The earlier finding that non-superhosts price higher on average than 
superhosts (Section 3.4) is explained by a confound: property type mix 
differs sharply between the two groups. Superhosts run a much higher 
share of private-room listings (36.7% vs. 7.8% for non-superhosts), 
the profile of an individually-managed, highly responsive host, while 
non-superhosts skew heavily toward entire-place listings (85.5%), 
often consistent with commercial or investment-style operations less 
focused on the responsiveness metrics superhost status requires. For 
a market intelligence consultancy, this means superhost status should 
not be interpreted as a direct price signal; it is better understood 
as a proxy for host management style (hands-on, responsive individual 
hosts vs. larger-scale commercial operators), with pricing differences 
driven by what they list, not by their service quality tier itself.

## 4.4 Professional vs. Casual Host Pricing - Business Interpretation

Single-listing (casual) hosts price higher on average (€275.75 median 
€227) than multi-listing (commercial) hosts (€260.69, median €189). 
Unlike the superhost finding, this is not fully explained by a single 
clean property-type confound: commercial hosts run a more diversified 
portfolio, including a meaningful share of hotel rooms (22.1%, vs. 
just 0.1% for casual hosts) and private rooms (32.4% vs. 8.9%), 
categories that individually price lower than entire-place listings. 
Casual hosts, by contrast, concentrate heavily in entire-place listings 
(87.3%), consistent with renting out their own home or a single 
higher-value investment property. For a market intelligence 
consultancy, this suggests commercial operators compete partly on 
volume and portfolio diversification across price tiers, rather than 
purely on premium per-unit pricing, while casual hosts effectively 
each represent a single, often higher-value listing with less 
portfolio flexibility.

## 4.4 Market Concentration (Cross-Reference to Section 4.1)

Already established in Section 4.1: 93.7% of hosts manage exactly one 
listing (82.3% of total supply), while the remaining 6.3% of hosts 
(multi-listing/commercial operators) control 17.7% of listings. This 
directly answers Section 4.4's market concentration question: supply 
is NOT concentrated in a small commercial elite; it remains 
predominantly an individual, small-scale hosting market, with 
commercial operators present but representing a clear minority of 
total inventory.