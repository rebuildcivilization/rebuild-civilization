# Frost Prediction

## Objective
Part of Weather Forecasting: Predicting frost timing from observable conditions, understanding cold air drainage, and protecting crops.

## Dependencies and prerequisites
Frost requires a specific combination of the following five conditions:

1. **Clear sky**: Clouds insulate the ground. A fully overcast night rarely produces frost even at cold temperatures. Even partial cloud cover can prevent frost on marginal nights.
2. **Calm wind**: Wind mixes warmer air from above down to the surface. Even 5-10 km/h of breeze can prevent frost. Dead calm is the critical factor.
3. **Cold surface temperature**: Ground radiates heat into space. Bare soil, short grass, and pavement cool fastest.
4. **Low humidity**: Dry air allows faster radiative cooling. However, very dry air produces black frost (invisible, more crop damage) rather than white frost.
5. **Long night**: More hours of darkness mean more cooling time. Frost season peaks near the equinoxes when nights are long but not yet at minimum temperatures.

Cold air is denser than warm air. After sunset, the ground cools the air in contact with it, causing cold air drainage (or katabatic flow), which pools in valleys and depressions.

## Material
### Cold Air Drainage
Cold air flows downhill after sunset, pooling in valleys, depressions, and behind obstacles. Effects include:
*   Valley floors can be 5-10°C colder than nearby hilltops.
*   A hollow behind a wall or hedgerow traps cold air.
*   Frost pockets form in the same locations year after year.
*   Hillside gardens midway up a slope often escape frost that kills valley crops.

### Frost Types
*   **White frost (Hoar frost)**: Forms when moisture in the air freezes on surfaces. Plants may survive light white frost because ice forms on the outside of leaves, and the latent heat released during freezing slows further cooling.
*   **Black frost**: Occurs when the air is too dry for visible ice (temperatures drop below freezing with no condensation). Plant cell water freezes internally, rupturing cell walls, causing leaves to turn black and collapse. It is more destructive because it offers no visual warning and no latent heat cushion.

### Frost Season Tracking
Reliable frost windows can be established over 3-5 years by tracking key dates:
*   Last spring frost (safe to transplant tender crops after this).
*   First fall frost (harvest deadline for frost-sensitive crops).
*   Average frost-free period (growing season length).
*   Coldest overnight temperature each winter (determines which perennials survive).

### Frost Protection Methods
*   **Row covers and mulch**: Trap enough radiated heat to keep surfaces 2-4°C warmer. Must be applied before sunset to trap daytime warmth.
*   **Watering before frost**: Wet soil holds more heat and releases it slowly. Water in the late afternoon on frost-risk days; freezing water releases latent heat (334 J/g) which can protect plant tissues.
*   **Smoke and smudge pots**: Smoke particles provide condensation nuclei and create a low canopy that traps radiated heat. Effective when built upwind of crops before dawn.
*   **Site selection**: Slopes facing the morning sun warm earliest. Mid-slope locations above cold air drainage lines get the least frost. South-facing slopes (in the Northern Hemisphere) accumulate more heat during the day.
*   **Thermal mass**: Large rocks, water containers, or stone walls absorb daytime heat and release it at night. A stone wall on the north side of a garden bed can raise minimum temperatures by 2-3°C.

## System
Weather forecasting based on observable conditions and understanding cold air drainage.

## Technology
Temperature drop method and extrapolation for timing predictions.

## Tools
*   Temperature drop calculation (Hourly drop rate).
*   Extrapolation (Multiplying the hourly drop rate by the number of hours until dawn).
*   Frost season tracking calendar.

## Process
### Predicting Frost Timing (The Evening Temperature Drop Method)
1. Note the temperature at sunset.
2. Check the temperature again one and two hours later.
3. Calculate the hourly drop rate.
    *   If the temperature drops more than 2°C per hour in the first two hours after sunset and the sky is clear: frost is very likely before dawn.
    *   If the drop rate is 1-2°C per hour: frost is possible, depending on how long the night lasts.
    *   If the drop rate is under 1°C per hour: frost is unlikely (cloud cover or wind is limiting cooling).
4. Extrapolation: Multiply the hourly drop rate by the number of hours until dawn. If the result brings the temperature below 0°C, expect frost (this provides a conservative estimate).

## Notes
- The source text indicates that reliable frost windows for a specific location can be established within 3-5 years by tracking historical data.
- The prediction methods provide a conservative estimate, as the actual cooling curve flattens as the temperature differential with the air decreases.
- Black frost is more destructive because it offers no visual warning and lacks the latent heat cushion found in white frost.
- The requirement for calm wind (dead calm being critical) is a key prerequisite for frost prevention.
