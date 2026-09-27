# Month 1 summary.

## Question
>Where are schools actually located across Kwara state, and how complete is OSM coverage of them by ward?

## Operation
spatial joined the kwara wards with the school points using the 'join attribute by location(summary) to ascertain the schools each ward holds.

## Expected
I expected an uneven distribution, more schools in the urban ilorin wards.

## Got
193 wards, with Yashikira II ward, baruten LGA recording the highest schools count of 17 which was quite unexpected for a non urban area. Many wards showed zero mapped schools.

## What surprised me
what surprised me was when i verify the highest school count by hand, I learned that Yashikira II ward holds the highest school which is in the rural area. I had expected the urban side to hold the highest school count.

## Limitations, stated plainly
- The OSM school datas hold less data for this project. most of the school points were not recorded.
- 164 of 193 wards returned null, meaning no OSM schools were found within them. Only 29 wards have mapped school coverage.

## What i still need
- An official government registry to compare against OSM counts.
Population data per ward to calculate schools.