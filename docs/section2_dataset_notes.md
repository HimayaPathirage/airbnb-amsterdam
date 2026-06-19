# Section 2 — Dataset Familiarization Notes
## Amsterdam, Inside Airbnb

---

## File: listings.csv.gz

**Shape:** 10,480 rows × 79 columns

### Column Groups Identified

| Category Name | Short Description | Core Columns |
| :--- | :--- | :--- |
| **Identifiers & Metadata** | Internal system tracking codes. They help keep everything unique and traceable. | `id`, `listing_url`, `scrape_id`, `last_scraped`, `source`, `calendar_updated`, `calendar_last_scraped`, `license` |
| **Listing Content** | Public advertising texts and details that guests see when browsing. | `name`, `description`, `neighborhood_overview`, `picture_url`, `amenities` |
| **Host Info** | Profile attributes, performance metrics, and trust badges relating to the property owner. | `host_id`, `host_name`, `host_since`, `host_response_rate`, `host_is_superhost` |
| **Location** | Geographic coordinates and neighborhood tracking attributes. | `neighbourhood`, `neighbourhood_cleansed`, `neighbourhood_group_cleansed`, `latitude`, `longitude` |
| **Property Attributes** | Physical design features, room types, and layout capacity rules. | `property_type`, `room_type`, `accommodates`, `bathrooms`, `bedrooms`, `beds` |
| **Pricing & Booking Rules** | Financial costs and reservation rules set by the host for booking. | `price`, `minimum_nights`, `maximum_nights`, `instant_bookable` |
| **Availability** | Rolling calendar vacancy schedules showing when the property is open. | `has_availability`, `availability_30/60/90/365`, `availability_eoy` |
| **Reviews & Demand** | Historical customer feedback counts and overall satisfaction scores. | `number_of_reviews`, `review_scores_*`, `reviews_per_month` |
| **Derived & Estimated** | Modeled performance metrics calculated by Inside Airbnb to estimate bookings. | `estimated_occupancy_l365d`, `estimated_revenue_l365d` |
| **Host Portfolio** | Total property counts managed by the same account to find commercial operators. | `calculated_host_listings_count*` |

**Key null findings:**
- `neighbourhood_group_cleansed` — 100% null (unusable for Amsterdam, will drop)
- `calendar_updated` — 100% null (unusable, will drop)
- `host_neighbourhood` — 73.4% null
- `neighbourhood` (raw) — 50.5% null
- `neighborhood_overview` — 50.5% null
- **`price` — 43.95% null.** Observation only — no fix applied yet.
  - Also stored as text with currency symbol, e.g. `"$132.00"`, dtype = object, 
    not numeric. Will require cleaning before any price-based analysis (Section 3.2).
- `estimated_revenue_l365d` — also 43.95% null, identical rate to `price` — 
  suggests revenue is only estimated when a price exists. To be confirmed.
- `estimated_occupancy_l365d` — 0% null, range 0–255 days, looks usable as-is.

---

## File: calendar.csv.gz

**Shape:** 3,825,200 rows × 7 columns

**Columns:** listing_id, date, available, price, adjusted_price, minimum_nights, maximum_nights

**Key findings:**
- `listing_id` confirmed as foreign key → listings.id
- `available` is t/f string flag. Distribution: f = 2,839,532 (74.2%), 
  t = 985,668 (25.8%)
- **`price` and `adjusted_price` are 100% null across all 3.8M rows** — 
  unusable for revenue calculation regardless of availability status.
  (See decisions_log.md for the decision taken on this.)

---

## File: reviews.csv / reviews.csv.gz
**Shape:** ~501,084 rows (consistent with reviews.csv summary) × 6 columns

**Columns:** listing_id, id, date, reviewer_id, reviewer_name, comments

**Key findings:**
- `listing_id` confirmed as foreign key → listings.id
- `id` is the primary key for individual reviews
- `comments` contains free-text guest reviews — raw material for any 
  NLP/sentiment work in Section 7 (optional)
- Review text quality varies — some single short sentences, others 
  detailed paragraphs. Worth noting as a limitation for any automated 
  text analysis (signal quality is uneven).
- No reviewer-side identifying info beyond name and ID — no demographic 
  or location data on reviewers.

---

## File: neighbourhoods.csv
**Shape:** 22 rows × 2 columns

**Columns:** neighbourhood_group, neighbourhood

**Key findings:**
- `neighbourhood_group` is 100% null — Amsterdam has no two-level 
  hierarchy, just 22 flat neighbourhood names. This is consistent with 
  `neighbourhood_group_cleansed` also being 100% null in listings.csv.gz 
  (same underlying reason, not two separate bugs).
- Verified: all 22 neighbourhood names match exactly between 
  neighbourhoods.csv and listings.csv.gz's neighbourhood_cleansed column. 
  Zero mismatches in either direction — clean join key, no fuzzy 
  matching needed.

---

## File: neighbourhoods.geojson
**Structure:** GeoJSON FeatureCollection, 22 features (matches the 22 
neighbourhoods exactly)

**Each feature contains:**
- `geometry` — polygon boundary coordinates for the neighbourhood
- `properties.neighbourhood` — name, matches the join key used in 
  listings.csv.gz and neighbourhoods.csv
- `properties.neighbourhood_group` — always None (third confirmation 
  that Amsterdam has no neighbourhood grouping hierarchy)

**Use case:** Ready for geospatial visualization (Folium/GeoPandas) in 
Section 4.2 without further cleaning.

---

## Data Dictionary Cross-Check — Columns Requiring Special Interpretation

1. **availability_365** — Rolling 365-day forward window from scrape date 
   (not a fixed calendar year). Low availability is ambiguous: could mean 
   high demand (booked) OR host-blocked dates. Cannot distinguish the two 
   from this field alone.

2. **calculated_host_listings_count (and its 3 room-type variants)** — 
   These are Inside Airbnb's own recalculation at scrape time, not 
   Airbnb's official host portfolio count. Split by entire home/private/
   shared room type.

3. **minimum_minimum_nights / maximum_minimum_nights / minimum_maximum_nights 
   / maximum_maximum_nights** — These look 365 days FORWARD in the calendar 
   to find the smallest/largest minimum-night and maximum-night rules a 
   host has set across the year. They are NOT duplicates of minimum_nights/
   maximum_nights (the current static rule) — easy to misinterpret as 
   redundant columns without checking the dictionary.

4. **instant_bookable** — Boolean, but officially documented as "an 
   indicator of a commercial listing." Worth using as a proxy signal in 
   host segmentation analysis (Section 4.4), not just a booking-flow flag.

5. **host_response_time / host_response_rate** — No official definition 
   provided in the data dictionary (unlike host_acceptance_rate, which is 
   defined as "the rate at which a host accepts booking requests"). 
   Interpreting these by name/convention only.

---

   ## Dataset Limitations

1. **Estimates, not ground truth.** estimated_occupancy_l365d and 
   estimated_revenue_l365d are modeled using Inside Airbnb's own 
   methodology (the "San Francisco Model"), which assumes a fixed review 
   rate (e.g., 50%) to convert review counts into estimated bookings. 
   This conversion rate is itself debated in research (different studies 
   use 30.5%–72%). These figures should be treated as directional 
   estimates, not measured revenue.

2. **Point-in-time snapshot, not continuous data.** The entire dataset 
   reflects a single scrape date (2025-09-11 for this file). It is not 
   a live feed — bookings, cancellations, and price changes happening 
   after this date are not captured.

3. **Calendar price field is unusable.** calendar.csv.gz's price/
   adjusted_price columns are 100% null for Amsterdam (3.8M rows) — a 
   scraping/data-collection artifact specific to this city/batch. 
   Revenue analysis must rely on listings.csv.gz's pre-computed 
   estimated_revenue_l365d instead.

4. **No guest-side data.** There is no demographic, location, or 
   booking-date information about guests — only review text and 
   reviewer name/ID. This prevents any analysis of who is actually 
   booking, beyond what can be inferred from review language.

5. **No actual financial data.** No real revenue, fees, or operating 
   cost data exists — all monetary figures are either the host's listed 
   price (sometimes missing) or Inside Airbnb's modeled estimate.

6. **Review undercounting.** Not every guest leaves a review, so 
   number_of_reviews and reviews_per_month understate actual bookings. 
   Combined with the review-rate assumption above, this compounds 
   uncertainty in any demand-side estimate.

7. **High missingness in several fields.** price (43.95%), neighbourhood 
   raw field (50.5%), neighborhood_overview (50.5%), host_neighbourhood 
   (73.4%) — see schema notes above for full detail.

8. **Single scrape, no historical trend within this file.** While 
   reviews.csv spans ~15 years (2010–2025) via review dates, listings.
   csv.gz itself only reflects the current state — there is no historical 
   record of past price changes or past availability for a listing.

---

   ## Assumptions About Ambiguous Fields

1. **price = NaN will be treated as "no price set," not "free listing."** 
   43.95% of listings.csv.gz rows have null price. Assumption: these are 
   listings where the host hasn't published a public price (possibly 
   inactive, paused, or requiring direct inquiry) — not literally $0. 
   These rows will be excluded from price-based statistics rather than 
   imputed with 0 or the mean, to avoid distorting price distributions.

2. **availability_365 will not be used alone as a "demand" signal.** 
   Per the official data dictionary, low availability can mean either 
   high demand (booked) or the host manually blocking dates. Assumption: 
   availability_365 will only be interpreted alongside number_of_reviews 
   or estimated_occupancy_l365d, never in isolation, when discussing 
   demand.

3. **estimated_revenue_l365d and estimated_occupancy_l365d are modeled 
   estimates, not actuals.** They will be labeled as such in all 
   visualizations and report text (e.g., "estimated revenue," never just 
   "revenue") to avoid implying these are confirmed transaction figures.

4. **neighbourhood (raw) field will be ignored in favor of 
   neighbourhood_cleansed.** The raw neighbourhood field is 50.5% null 
   and free-text (host-entered); neighbourhood_cleansed is Inside 
   Airbnb's standardized version with 0% null and verified 1:1 matching 
   against neighbourhoods.csv. All neighbourhood-level analysis will use 
   neighbourhood_cleansed exclusively.

5. **host_neighbourhood will not be used for analysis.** At 73.4% null 
   and self-reported by hosts (not standardized), this field is too 
   unreliable for any location-based grouping. It will be documented as 
   excluded.

6. **neighbourhood_group_cleansed and calendar_updated will be dropped 
   entirely.** Both are 100% null for Amsterdam — confirmed dead columns, 
   not worth carrying through any pipeline.

7. **review counts will be treated as a lower-bound proxy for bookings, 
   not an exact count.** Per Inside Airbnb's own published methodology, 
   not every guest leaves a review (their model assumes roughly a 50% 
   review rate when estimating bookings from reviews). Any demand 
   analysis using review counts will explicitly caveat this.

8. **minimum_minimum_nights / maximum_minimum_nights / 
   minimum_maximum_nights / maximum_maximum_nights will be treated as 
   calendar-derived forward-looking ranges, not duplicates of 
   minimum_nights/maximum_nights.** Per the official data dictionary, 
   these look 365 days into the future across the calendar, while 
   minimum_nights/maximum_nights reflect the current static rule. Both 
   will be kept, used for different purposes (current rule vs. policy 
   volatility over the year).

---

   ## Business Domain Context

This dataset represents the short-term rental marketplace in Amsterdam 
as visible on Airbnb at the time of scraping (2025-09-11). Three core 
entities make up the business model:

**Listing** — A single rental unit (an entire apartment, a private room, 
or a shared room) that a host has published on the platform for guests 
to book. Each listing has its own price, location, capacity, amenities, 
and booking rules (minimum/maximum nights, instant booking availability). 
A listing is the unit of supply in this marketplace — it's what guests 
search for, compare, and ultimately book.

**Host** — The person or entity that owns/manages one or more listings. 
Hosts range from individuals renting out a single spare room casually, 
to commercial operators managing dozens of properties as a business 
(visible via calculated_host_listings_count). Host attributes — response 
rate, acceptance rate, superhost status, verification status — function 
as trust signals that influence a guest's booking decision, similar to 
a seller's reputation score in any marketplace.

**Review** — Feedback left by a guest after a stay, tied to a specific 
listing. Reviews serve two roles in this business: (1) a trust/quality 
signal for future guests deciding whether to book, and (2) the closest 
available proxy for actual booking activity, since the dataset contains 
no direct transaction or revenue data. A listing with many recent 
reviews is generally inferred to be actively booked, though this is an 
imperfect signal (see Assumptions, point 7).

**Neighbourhood** — The geographic grouping (22 distinct areas in 
Amsterdam) used to segment the city for location-based analysis. It 
functions as the "market" or "submarket" lens through which pricing, 
density, and demand patterns are typically compared — similar to how a 
real estate analyst would segment a city into districts.

Together, these entities support the core questions a market 
intelligence consultancy would ask: Where is supply concentrated? Who 
controls that supply (casual hosts vs. commercial operators)? How is it 
priced? And how does guest demand (via reviews and estimated occupancy) 
respond to location, price, and host behavior?