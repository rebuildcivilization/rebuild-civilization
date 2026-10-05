# Lightning Distance | Survival Wiki

## Objective
To calculate lightning distance, track storm movement, and make shelter decisions.

## Dependencies and prerequisites
*   The ability to see a lightning flash.
*   The ability to hear thunder.

## Material
### The Flash-to-Bang Method
Light travels effectively instantly (reaches you in microseconds). Sound travels at roughly 343 meters per second at sea level.

**Distance Conversion:**
*   Divide by 3 for distance in kilometers.
*   Divide by 5 for distance in miles.

**Distance Table:**
| Seconds | Distance (km) | Distance (miles) |
| :---: | :---: | :---: |
| 3 | 1.0 | 0.6 |
| 5 | 1.7 | 1.0 |
| 10 | 3.3 | 2.0 |
| 15 | 5.0 | 3.0 |
| 20 | 6.7 | 4.0 |
| 25 | 8.3 | 5.0 |
| 30 | 10.0 | 6.0 |

### Shelter Decision Guidelines
*   **Under 30 seconds (10 km / 6 miles):** Begin moving toward shelter. Lightning can strike up to 15 km from the storm center.
*   **Under 15 seconds (5 km / 3 miles):** You should already be in shelter. If not, take immediate action: crouch low in a depression, stay away from tall objects and water.
*   **Under 5 seconds (1.7 km / 1 mile):** Extremely dangerous. Do not move from shelter. Assume the lightning position: crouch on the balls of your feet, feet together, hands over ears, head down.
*   **Simultaneous flash and bang (0 seconds):** The strike was within 100 meters of you. Stay in shelter.

### Storm Structure Indicators
*   **Frequent intra-cloud lightning:** The storm is building or at peak intensity.
*   **Cloud-to-ground strikes increasing:** The storm is mature and at its most dangerous phase, accompanied by heavy rain, hail, and strong winds.
*   **Flashes becoming less frequent, counts getting longer:** The storm is weakening and/or moving away.
*   **30-minute rule:** Do not resume outdoor activity until 30 minutes after the last thunder.

### Tracking Storm Direction
1.  Note the lightning flash location (compass direction or reference landmark).
2.  Record the flash-to-bang time.
3.  Wait for the next flash in approximately the same part of the sky.
4.  Record the new flash-to-bang time.

**Interpretation of Trends:**
*   **Count getting shorter:** Storm is approaching. Seek shelter now.
*   **Count staying the same:** Storm is moving parallel to you. Stay alert but not in immediate danger.
*   **Count getting longer:** Storm is moving away. Continue monitoring but risk is decreasing.

**Direction Tracking:** If the flash position moves from your right to your left over successive strikes, the storm is moving in that direction.

## System
The system utilizes flash-to-bang timing to calculate lightning distance, track storm movement, and inform shelter decisions.

## Technology
*   Flash-to-bang timing.
*   Quartz (mentioned in the creation details).

## Tools
*   A timer/counting mechanism for the flash-to-bang method.
*   Compass or reference landmarks for direction tracking.

## Process
### Flash-to-Bang Procedure
1.  See a lightning flash.
2.  Immediately start counting seconds ("one-thousand-one, one-thousand-two...").
3.  Stop counting when you hear the thunder.
4.  Calculate distance by dividing the seconds by 3 (for km) or by 5 (for miles).

### Storm Tracking Procedure
1.  Perform multiple measurements over time.
2.  Note lightning flash location.
3.  Record flash-to-bang time.
4.  Wait for the next flash in the same sky area.
5.  Record the new flash-to-bang time.
6.  Interpret the trend of the counts (shorter = approaching; longer = moving away).

### Accuracy and Refinement
*   **Temperature:** Temperature affects sound speed (e.g., 0C = 331 m/s; 30C = 349 m/s). The difference is about 5% and is not significant for safety decisions.
*   **Altitude:** At 2000m elevation, add roughly 10% to the distance estimate due to lower air density.
*   **Wind:** A strong wind can shift the estimate by 10-15%. If the storm is upwind and approaching, the flash-to-bang count overestimates the true distance; err on the side of caution.
*   **Multiple Strokes:** The most accurate reading comes from the time between the first lightning flash and the first sound of thunder.
*   **Rolling Thunder:** Long, rolling thunder indicates a long lightning channel (possibly several km). The first crack gives the distance to the nearest point.

### Observation Methods
*   **Night Observation:** Easier to track as flashes from storms 100+ km away can be seen. Begin timing when thunder becomes audible (roughly 15-20 km range depending on terrain).
*   **Day Observation:** Use the direction of cloud buildup and darkening sky to supplement flash-to-bang timing.

### Teaching
Practice counting during distant storms when there is no immediate danger to make the counting automatic when a storm approaches unexpectedly.

## Notes
*   **Key Message:** "If you can hear thunder, you can be struck by lightning." The counting method indicates the time remaining, not absolute safety.
*   **Accuracy Caveat:** The 'divide by 3 for km' rule works well enough across all normal temperatures.
*   **Wind Correction:** Wind shifts estimates by 10-15%. If the storm is upwind, the estimated distance is too large, meaning the storm is closer.
*   **Material Source:** The core methodology relies on the relationship between light speed (instantaneous) and sound speed (measurable over time).
