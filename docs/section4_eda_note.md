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

